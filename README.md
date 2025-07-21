# 📡 Reservation Page Monitor

指定したWEBページ（例：ライブ予約ページ）を定期的にチェックし、
ページの内容に更新があった場合にメールで通知するPythonスクリプトです。

---

## ✨ 主な特徴

- 任意のURLのコンテンツをハッシュ化して差分を検出
- 更新が検出されると、指定メールアドレスに自動通知
- `crontab` による定期実行で自動化

---

## 📦 構成

```plaintext
reservation_monitor/
├── monitor/
│   ├── monitor.py         # メインスクリプト
│   ├── last_hash.txt      # ページのハッシュ値を記録
│   └── log.txt            # ログファイル（crontab用）
└── README.md              # このファイル
