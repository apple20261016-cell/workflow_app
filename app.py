import streamlit as st

# ページの設定
st.set_page_config(page_title="社内ワークフローシステム", page_icon="🔐", layout="centered")

# セッション状態（ログイン状態）の初期化
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def check_password():
    """パスワード認証の判定"""
    # ここに任意のパスワードを設定します
    CORRECT_PASSWORD = "secret123"
    
    password_input = st.text_input("パスワードを入力してください", type="password")
    if st.button("ログイン"):
        if password_input == CORRECT_PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("パスワードが違います。")

# 1. 未認証の場合はログイン画面を表示
if not st.session_state.authenticated:
    st.title("🔐 社内ワークフローシステム")
    st.info("このアプリを利用するにはパスワードが必要です。（初期パスワード: secret123）")
    check_password()

# 2. 認証済みの場合はメインのワークフロー画面を表示
else:
    st.title("📋 簡易ワークフロー申請フォーム")
    st.write("必要事項を入力して申請してください。")

    with st.form("workflow_form"):
        applicant = st.text_input("申請者氏名")
        department = st.selectbox("所属部署", ["営業部", "開発部", "総務部", "マーケティング部"])
        title = st.text_input("申請件名")
        category = st.selectbox("申請種別", ["経費精算", "備品購入", "出張申請", "その他"])
        amount = st.number_input("金額（円）", min_value=0, step=1000)
        reason = st.text_area("申請理由・詳細")
        
        submitted = st.form_submit_button("申請を送信する")
        if submitted:
            if applicant and title:
                st.success(f"【送信完了】{applicant} さんからの申請（{title}）を受け付けました！")
                # 送信された内容の確認表示
                st.info(f"【内容確認】所属: {department} / 種別: {category} / 金額: {amount:,}円\n\n理由: {reason}")
            else:
                st.warning("「申請者氏名」と「申請件名」は必須です。")

    # サイドバーにログアウトボタンを配置
    with st.sidebar:
        st.write("⚙️ メニュー")
        if st.button("ログアウト"):
            st.session_state.authenticated = False
            st.rerun()
