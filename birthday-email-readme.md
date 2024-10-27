# 生日郵件發送系統

自動化生日郵件發送系統，可在指定日期自動發送客製化的生日祝福郵件。

## 功能特點

- 自動檢查每日壽星
- 隨機選擇生日賀卡模板
- 個人化郵件內容
- 使用 Yahoo SMTP 服務發送郵件
- 完整的錯誤處理機制

## 系統需求

- Python 3.7 以上版本
- pandas 套件
- smtplib (Python 標準函式庫)
- email (Python 標準函式庫)

## 安裝說明

1. 將專案複製到本機：
```bash
git clone [您的儲存庫網址]
cd birthday-email-sender
```

2. 安裝必要套件：
```bash
pip install pandas
```

## 檔案結構

```
birthday-email-sender/
│
├── main.py              # 主程式
├── mail.py             # 郵件設定檔（含認證資訊）
├── birthdays.csv       # 生日資料檔
│
└── letter_templates/   # 信件模板目錄
    ├── letter_1.txt
    ├── letter_2.txt
    └── letter_3.txt
```

## 設定說明

### 1. 設定 mail.py

建立 `mail.py` 檔案並填入以下內容：

```python
yahoo_address = "您的信箱@yahoo.com"
yahoo_password = "您的應用程式專用密碼"
```

注意：為了安全性考量，請使用 Yahoo 的應用程式專用密碼，而非您的主要帳號密碼。

### 2. 準備 birthdays.csv

建立 `birthdays.csv` 檔案，格式如下：

```csv
name,email,month,day
張小明,xiaoming@example.com,10,27
李小華,xiaohua@example.com,10,28
```

### 3. 準備信件模板

在 `letter_templates` 目錄下建立三個模板檔案：
- letter_1.txt
- letter_2.txt
- letter_3.txt

模板中使用 `[NAME]` 作為姓名的替換標記，例如：

```
親愛的 [NAME]：

生日快樂！
願您有個美好的一天。

祝福您
生日郵件小組
```

## 使用方法

1. 確認所有設定檔都已正確配置
2. 執行主程式：
```bash
python main.py
```

程式會自動：
- 檢查今天是否有人生日
- 為壽星隨機選擇一個賀卡模板
- 替換模板中的姓名
- 發送個人化的生日郵件

## 錯誤處理

程式包含以下錯誤處理機制：
- 檢查設定檔是否存在
- 驗證 CSV 檔案格式
- 處理郵件發送失敗的情況
- SMTP 連線錯誤處理

## 常見問題

1. **郵件發送失敗**
   - 確認 Yahoo 帳號設定正確
   - 確認使用的是應用程式專用密碼
   - 檢查網路連線狀態

2. **找不到生日資料**
   - 確認 birthdays.csv 檔案存在
   - 確認 CSV 格式正確無誤

3. **模板載入失敗**
   - 確認 letter_templates 目錄存在
   - 確認三個模板檔案都存在且格式正確

## 安全注意事項

1. 切勿在程式碼中直接寫入密碼
2. 務必使用 Yahoo 的應用程式專用密碼
3. 請勿將含有敏感資訊的設定檔上傳至版本控制系統

## 參與開發

歡迎提交推送請求（Pull Request）或建立問題（Issue）來改善這個專案。在提交之前，請確保：
1. 程式碼遵循 PEP 8 規範
2. 新功能包含適當的錯誤處理
3. 更新相關文件

## 開發者

Dawei, Hao

## 版本更新紀錄

### 版本 1.0.0
- 初始版本發布
- 基本郵件發送功能
- 模板系統實作
- 錯誤處理機制