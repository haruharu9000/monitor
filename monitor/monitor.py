import hashlib
import requests
import smtplib
from email.message import EmailMessage
from datetime import datetime
import os

# 設定
URL = "http://example.com"  # 監視対象ページ
EMAIL = "your@email.com"      # 通知先メールアドレス
APP_PASSWORD = "your-app-password"  # メールパスワード
HASH_FILE = "/Users/yourname/hash256.txt"  # ハッシュ値保存先（絶対パス）

# ページ取得とハッシュ算出
res = requests.get(URL, timeout=10)
page_hash = hashlib.sha256(res.text.encode("utf-8")).hexdigest()

# 前回のハッシュ読み込み
if os.path.exists(HASH_FILE):
    with open(HASH_FILE, "r") as f:
        previous_hash = f.read().strip()
else:
    previous_hash = None

# ハッシュ差分検知 → 通知
if page_hash != previous_hash:
    now = datetime.now().strftime("%Y年%m月%d日（%a）%H:%M:%S")
    body = f"ページが更新されたよ！\n{now}\n{URL}"

    msg = EmailMessage()
    msg["Subject"] = "【ページ更新通知】"
    msg["From"] = EMAIL
    msg["To"] = EMAIL
    msg.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)

    with open(HASH_FILE, "w") as f:
        f.write(page_hash)
