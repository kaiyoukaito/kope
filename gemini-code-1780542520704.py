import streamlit as st
import datetime

st.set_page_config(page_title="旭区親子(仮)", layout="centered")

st.title("👨‍👩‍👧‍👦 旭区親子(仮)")

# タブ切り替え（イチハブ方式）
tab1, tab2 = st.tabs(["📱 子世代画面 (注文・管理)", "👵 親世代画面 (訪問・見守り)"])

with tab1:
    st.subheader("本日の見守りステータス")
    st.success("✅ 正常：本日11:30に配送員が手渡し完了。お変わりありません。")
    
    st.markdown("---")
    st.subheader("🛒 今週の通信販売")
    # 通信販売画面（申し訳程度に要素を配置）
    item = st.selectbox("購入商品を選んでください", ["旭区野菜セット", "日用品詰合せ", "冷凍おかず"])
    st.button("カートに入れる")
    
    st.info("配送料：1,000円（※親の訪問販売契約で無料になります）")

with tab2:
    st.subheader("本日の訪問販売カタログ")
    st.write("・おすすめ：今週の特売野菜セット")
    st.button("注文を配送員に伝える")
    
    st.markdown("---")
    st.subheader("見守りメッセージ")
    st.write("「お元気です。また来週伺います。」")

# フッター
st.markdown("---")
st.caption(f"{datetime.date.today()} - 旭区親子(仮) 運営事務局")