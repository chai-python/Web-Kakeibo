# Web Kakeibo

## 概要

PythonとFlaskを使って作成したWeb版の家計簿アプリケーションです。
支出の登録・表示・編集・削除ができます。

## 使用技術

- Python
- Flask
- HTML
- JSON
- Git / GitHub

## 主な機能

- 支出管理： 支出の登録・表示・編集・削除
- 検索機能： 商品名による支出の検索
- 月別表示： 指定した年月の支出を表示
- 支出集計： 月ごとの支出総額を計算
- 予算管理： 月間予算の登録・保存、予算残額の計算
- データ保存： JSONファイルを使用した支出データと予算データの保存

## 使用方法
1. PythonとFlaskをインストールします。
2. プロジェクトのディレクトリで app.py を実行します。
3. Flaskサーバーの起動後、ブラウザで `http://127.0.0.1:5000` にアクセスします。
> ※ 本アプリケーションはローカル環境で動作します。アクセスするには、事前にFlaskサーバーを起動する必要があります。

## ファイル構成

```text
Web-Kakeibo/
├── app.py
├── README.md
├── .gitignore
├── kakeibo.json
├── budget.json
└── templates/
    ├── index.html
    └── edit.html
```
> ※ `kakeibo.json` と `budget.json` はローカルで使用するデータファイルであり、GitHubには公開しません。

### 主なファイル

- `app.py`： Flaskによる画面表示、支出管理、集計、予算管理などの処理
- `templates/index.html`： 家計簿のメイン画面
- `templates/edit.html`： 支出を編集する画面
- `kakeibo.json`： 支出データの保存先
- `budget.json`： 月間予算データの保存先

## 学習目的

Pythonで作成した家計簿をWebアプリケーション化することを通じて、Flaskによるルーティング、HTMLフォームを使ったデータ送信、JSONファイルによるデータの保存・読み込みなど、Webアプリケーションの基本的な仕組みを学ぶことを目的としています。

## 今後の予定

- UIの改善
- コードの整理と動作確認
