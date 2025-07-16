import streamlit as st
import pandas as pd
import altair as alt

# ------------------ 페이지 설정 ------------------
st.set_page_config(page_title="MBTI 국가별 Top3", page_icon="🌍", layout="centered")
st.title("🌎 국가별 MBTI 유형 Top 3 시각화")

# ------------------ CSV 불러오기 ------------------
uploaded_file = st.file_uploader("📂 MBTI CSV 파일을 업로드하세요 (선택)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ 업로드한 파일을 불러왔습니다.")
else:
    try:
        df = pd.read_csv("countriesMBTI_16types.csv")
        st.info("ℹ️ 업로드된 파일이 없어 기본 파일(countriesMBTI_16types.csv)을 사용합니다.")
    except FileNotFoundError:
        st.error("❌ 기본 파일이 폴더에 없습니다. CSV 파일을 업로드해주세요.")
        st.stop()

# ------------------ 국가 선택 ------------------
country_list = df['Country'].unique().tolist()
selected_country = st.selectbox("🌐 국가를 선택하세요", country_list)

# ------------------ 상위 3개 MBTI 유형 추출 ------------------
row = df[df['Country'] == selected_country].iloc[0]
mbti_scores = row.drop('Country')

top3 = mbti_scores.sort_values(ascending=False).head(3).reset_index()
top3.columns = ['MBTI', '비율']
top3['비율(%)'] = top3['비율'] * 100

# ------------------ Altair 시각화 ------------------
chart = alt.Chart(top3).mark_bar().encode(
    x=alt.X('MBTI:N', title='MBTI 유형'),
    y=alt.Y('비율(%):Q', title='비율 (%)'),
    color=alt.Color('MBTI:N', legend=None)
).properties(
    title=f"{selected_country}의 MBTI 유형 Top 3",
    width=500,
    height=400
)

st.altair_chart(chart, use_container_width=True)

# ------------------ 수치 테이블 ------------------
st.markdown("### 📊 세부 수치")
st.dataframe(top3[['MBTI', '비율(%)']].round(2), use_container_width=True)
