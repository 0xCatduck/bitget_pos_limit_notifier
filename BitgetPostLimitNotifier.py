# -*- coding: utf-8 -*-
# @Project : BitgetPosLimitNotifier
# @Date    : 2024-01-21 20:00:00(UTC+8)
# @Author  : 0xCatduck
# @Link    : https://github.com/0xCatduck

import requests
import json
from tkinter import Tk, messagebox, Label, Entry, Button, Text
import webbrowser
import winsound

# 全局變量
current_symbol = ""
last_pos_limit = 0
timer = None

def fetch_pos_limit(symbol):
    try:
        response = requests.get(f"https://api.bitget.com/api/v2/mix/market/contracts?productType=USDT-FUTURES&symbol={symbol}USDT")
        data = json.loads(response.text)
        for item in data["data"]:
            return round(float(item["posLimit"]) * 100, 2)
    except Exception as e:
        messagebox.showerror("錯誤", f"無法從API獲取數據: {e}")
    return 0

def update_pos_limit_label(symbol, pos_limit):
    pos_limit_label.config(text=f"目前 {symbol} 倉位限制: {pos_limit}%")

def check():
    global last_pos_limit, current_symbol, timer
    if not current_symbol:
        return

    pos_limit = fetch_pos_limit(current_symbol)
    update_pos_limit_label(current_symbol, pos_limit)

    if pos_limit != last_pos_limit:
        winsound.Beep(1000, 1000)  # 頻率1000赫茲，持續時間1000毫秒
        messagebox.showwarning("警告", f"{current_symbol} posLimit 的值變化為 {pos_limit}%")
        last_pos_limit = pos_limit

    timer = root.after(10000, check)

def update_symbol():
    global current_symbol, timer
    if timer:
        root.after_cancel(timer)
    current_symbol = symbol_entry.get().upper()
    check()

def open_link(event):
    webbrowser.open("https://www.bitget.com/zh-TW/futures/introduction/position-limit")

# GUI部分
root = Tk()
root.title("Bitget倉位限制偵測器")
root.option_add("*Font", "標楷體")
root.geometry("310x240")

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