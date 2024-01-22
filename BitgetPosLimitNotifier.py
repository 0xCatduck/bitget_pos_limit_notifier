# -*- coding: utf-8 -*-
# @Project : BitgetPosLimitNotifier
# @Date    : 2024-01-21 20:00:00(UTC+8)
# @Author  : 0xCatduck
# @Link    : https://github.com/0xCatduck

import requests
import json
from tkinter import Tk, messagebox, Label, Entry, Button, Text
import webbrowser
import time
import pygame
import os
import sys

# 全局變量
current_symbol = ""
current_time = ""
last_pos_limit = 0
timer = None
is_first_check = True


def fetch_pos_limit(symbol):
    try:
        response = requests.get(f"https://api.bitget.com/api/v2/mix/market/contracts?productType=USDT-FUTURES&symbol={symbol}USDT")
        data = json.loads(response.text)
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for item in data["data"]:
            return round(float(item["posLimit"]) * 100, 2), current_time
    except Exception as e:
        messagebox.showerror("錯誤", f"無法從API獲取數據: {e}")
    return 0, ""

def update_pos_limit_label(symbol, pos_limit, current_time):
    pos_limit_label.config(text=f"目前 {symbol} 倉位限制: {pos_limit}%\n更新時間：[{current_time}]")

def check():
    global last_pos_limit, current_symbol, timer, current_time, is_first_check
    if not current_symbol:
        return

    pos_limit, current_time = fetch_pos_limit(current_symbol)
    update_pos_limit_label(current_symbol, pos_limit, current_time)

    # 只有在非第一次查詢且倉位限制發生變化時才觸發警告
    if not is_first_check and pos_limit != last_pos_limit:
        # 播放警鈴聲音
        play_alert_sound()
        messagebox.showwarning("警告", f"{current_symbol} posLimit 的值變化為 {pos_limit}%")
    
    last_pos_limit = pos_limit
    is_first_check = False  # 更新布林變量，表示已經不是第一次查詢了

    timer = root.after(10000, check)

def update_symbol():
    global current_symbol, timer, is_first_check
    if timer:
        root.after_cancel(timer)
    current_symbol = symbol_entry.get().upper()
    is_first_check = True
    check()

def play_alert_sound():
    # 初始化 pygame 的混音器
    pygame.mixer.init()

    # 獲得執行檔案的目錄
    if getattr(sys, 'frozen', False):
        # 如果是打包後的執行檔，使用 _MEIPASS
        base_path = sys._MEIPASS
    else:
        # 如果不是打包後的執行檔，則直接使用 __file__ 屬性
        base_path = os.path.dirname(os.path.abspath(__file__))

    # 建立 alert.mp3 檔案的絕對路徑
    alert_sound_path = os.path.join(base_path, 'alert.mp3')

    # 載入並播放警鈴聲音文件
    pygame.mixer.music.load(alert_sound_path)
    pygame.mixer.music.play()

    # 等待音樂播放完畢
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)



def open_link(event):
    webbrowser.open("https://www.bitget.com/zh-TW/futures/introduction/position-limit")

# GUI部分
root = Tk()
root.title("Bitget倉位限制偵測器")
root.option_add("*Font", "標楷體")
root.geometry("320x280")

symbol_label = Label(root, text="交易對(例如UMAUSDT則輸入UMA)")
symbol_label.pack()

symbol_entry = Entry(root)
symbol_entry.pack()

update_button = Button(root, text="更新", command=update_symbol)
update_button.pack()

pos_limit_label = Label(root, text="")
pos_limit_label.pack()

# 使用 Text 組件顯示包含超連結的文字
pos_limit_explain_label = Text(root, height=6, width=40, wrap="word")
pos_limit_explain_label.insert("end", "此程式主要用於偵測倉位限制發生變化，每當發生變化時會彈窗通知。倉位限制為單主帳戶，含子帳號可能為2~3倍，具體請參考")
pos_limit_explain_label.insert("end", "BG官網", "link")
pos_limit_explain_label.insert("end", "。實際建倉數量請貓友互相通知。")
pos_limit_explain_label.tag_configure("link", foreground="blue", underline=1)
pos_limit_explain_label.tag_bind("link", "<Button-1>", lambda e: webbrowser.open("https://www.bitget.com/zh-TW/futures/introduction/position-limit"))
pos_limit_explain_label.config(state="disabled")
pos_limit_explain_label.pack()

# 添加作者資訊
author_label = Text(root, height=1, width=50)
author_label.pack()
author_label.insert("end", "作者：0xCatduck", "github")
author_label.tag_config("github", foreground="blue", underline=1)
author_label.tag_bind("github", "<Button-1>", lambda e: webbrowser.open("https://github.com/0xCatduck"))
author_label.config(state="disabled")

root.mainloop()