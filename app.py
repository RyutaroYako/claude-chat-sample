import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

# 環境変数の読み込み（.envファイルが存在する場合のみ）
if os.path.exists(".env"):
    load_dotenv()


# Anthropicクライアントの初期化（APIキーがある場合のみ）
def get_client():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if api_key:
        return anthropic.Anthropic(api_key=api_key)
    return None


# Streamlitの設定
st.set_page_config(page_title="Claude Chat App", page_icon="🤖", layout="wide")

# セッション状態の初期化
if "messages" not in st.session_state:
    st.session_state.messages = []
if "client" not in st.session_state:
    st.session_state.client = None

# タイトルの表示
st.title("💬 Claude Chat App")

# サイドバーにAPIキー入力欄を追加
with st.sidebar:
    api_key = st.text_input("Anthropic API Key", type="password")
    if api_key:
        os.environ["ANTHROPIC_API_KEY"] = api_key
        st.session_state.client = get_client()
    elif os.getenv("ANTHROPIC_API_KEY"):
        st.session_state.client = get_client()

    st.markdown(
        """
    ### 使い方
    1. Anthropic API Keyを入力
    2. メッセージを入力
    3. Enterキーを押すか送信ボタンをクリック

    ### 注意事項
    - API Keyは安全に管理してください
    - 長い会話は料金がかかる可能性があります
    """
    )

# チャット履歴の表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザー入力
if prompt := st.chat_input("メッセージを入力してください"):
    # API Keyのチェック
    if not st.session_state.client:
        st.error("Anthropic API Keyを入力してください。")
        st.stop()

    # ユーザーメッセージの表示と保存
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            # Claudeとの対話
            with st.spinner("Claude が考え中..."):
                response = st.session_state.client.messages.create(
                    model="claude-3-sonnet-20240229",
                    max_tokens=4096,
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                )
                full_response = response.content[0].text

            # 応答の表示
            message_placeholder.markdown(full_response)

        # 応答の保存
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )

    except Exception as e:
        st.error(f"エラーが発生しました: {str(e)}")

# 履歴クリアボタン
if st.button("チャット履歴をクリア"):
    st.session_state.messages = []
    st.rerun()
