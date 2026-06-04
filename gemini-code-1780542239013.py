import streamlit as st

# アプリの構成設定
st.set_page_config(page_title="旭区親子(仮) - 地域密着型インフラ", layout="wide")

st.title("👨‍👩‍👧‍👦 地域インフラプラットフォーム『 旭区親子(仮) 』")
st.caption("横浜市旭区の団地コミュニティを『定期配送』と『見守り』で繋ぐプラットフォーム")

# メイン画面：子世代と親世代の連動を直感的に表示
col1, col2 = st.columns(2)

with col1:
    st.subheader("📱 子世代用：通販・管理画面")
    purchase = st.slider("月間利用額(円)", 5000, 30000, 18000, 1000)
    mimamori = st.checkbox("実家の親の見守りサービス(月1,480円)を付帯", True)
    st.info("配送料: 1,000円 (親の訪問販売契約で無料になります)")

with col2:
    st.subheader("👵 親世代用：簡単注文・見守り")
    status = st.radio("訪問販売の利用状況", ["未利用", "定期訪問販売利用中"])
    st.success("本日の見守り: 配送員が手渡し完了。お元気そうです。")

st.markdown("---")

# 収支・インセンティブ連動ロジック（ここが肝）
if status == "定期訪問販売利用中":
    fee = 0
    msg = "✅ 【旭区親子(仮)特典】子世代の配送料が無料です"
else:
    fee = 1000
    msg = "⚠️ 親の訪問販売契約で配送料が無料になります"

st.subheader("📊 旭区親子(仮) 収支・割引計算")
st.metric("子世代の請求合計", f"{purchase + (1480 if mimamori else 0) + fee:,} 円")
st.write(msg)