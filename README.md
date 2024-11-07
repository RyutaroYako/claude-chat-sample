# Claude Chat Application

Anthropic 社の Claude 3.5 Sonnet を使用した Streamlit ベースのチャットアプリケーションです。

## セットアップ手順

1. リポジトリをクローン

```bash
git clone <repository-url>
cd <repository-name>
```

2. アプリケーションの起動

```bash
docker compose up --build
```

## API Key の設定方法（2 つの方法）

### 方法 1: 環境変数ファイルを使用

1. .env.example を.env にコピー

```bash
cp .env.example .env
```

2. .env ファイルを編集して API キーを設定

```
ANTHROPIC_API_KEY=your_api_key_here
```

### 方法 2: Web UI 上で直接入力

1. アプリケーションにアクセス
2. サイドバーの API Key 入力欄にキーを入力

## 使用方法

1. ブラウザで http://localhost:8501 にアクセス
2. Anthropic の API キーを設定（環境変数または画面上で入力）
3. チャット入力欄にメッセージを入力して送信
4. 必要に応じて「チャット履歴をクリア」ボタンで会話をリセット

## 機能

- Claude 3.5 Sonnet とのリアルタイムチャット
- チャット履歴の保持と表示
- API キーの柔軟な設定（環境変数ファイルまたは UI 上で設定可能）
- チャット履歴のクリア機能

## 技術スタック

- Python
- Streamlit
- Anthropic Claude API
- Docker
- Docker Compose

## 開発環境での実行

Docker Compose を使用せずに直接実行する場合：

1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

2. アプリケーションの起動

```bash
streamlit run app.py
```

## 注意事項

- API キーは安全に管理してください
- 環境変数ファイル(.env)の使用は任意です。UI から API キーを入力することも可能です。
- チャットの履歴はブラウザセッション内でのみ保持されます
