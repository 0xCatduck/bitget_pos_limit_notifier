# BitgetPosLimitNotifier

BitgetPosLimitNotifier 是一款用於實時監控並通知使用者 Bitget 交易平台上特定交易對的倉位限制比例是否發生變化的工具。
設計主要用以查詢Bitget 已經施加開倉限制的交易對，在何時解封或著進一步限制開倉數量。
![BitgetPosLimitNotifier Screenshot](https://i.imgur.com/9Hrel48.png)

## 功能

- **實時監控**: 定時檢查並更新所選交易對的倉位限制。
- **用戶自定義**: 允許使用者輸入並更新他們想要監控的交易對。
- **警告通知**: 當所選交易對的倉位限制發生變化時，程式會通過彈窗提醒使用者。

## 安裝

本工具需要 Python 3.6 或更高版本。可以從以下地址下載並安裝 Python：https://www.python.org/downloads/

除此之外，本工具不需要安裝任何額外的第三方庫。

您也可以下載位於右側Release的BitgetPostLimitNotifier.exe (v1.0)，不須python環境即可直接開啟程式。

## 使用方法

1. 啟動應用。
2. 在輸入框中輸入您想要監控的交易對（例如，對於 UMA/USDT 交易對，只需輸入 'UMA'）。
3. 點擊“更新”按鈕開始監控。
4. 應用會每10秒自動檢查倉位限制，並在發現任何變化時通過彈窗提醒。

## 注意事項

視窗縮小後若發生倉位限制變化，彈窗不會跳出而是在背景顯示並且程式的icon會閃爍。
![Minimize window Screenshot](https://i.imgur.com/GzUfyKE.png)

## 貢獻

如果您想要對此項目做出貢獻，請訪問以下 GitHub 頁面：[0xCatduck's BitgetPosLimitNotifier](https://github.com/0xCatduck)

## 聯繫方式

如有任何問題或建議，請通過以下方式聯繫我：

- GitHub：[0xCatduck](https://github.com/0xCatduck)
- Gmail：[0xCatduck](mailto:0xCatduck@gmail.com)
- X: [0xCatduck](https://twitter.com/0xCatduck)