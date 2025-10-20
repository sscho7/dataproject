import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="국가별 MBTI 비율 분석", page_icon="🌏", layout="wide")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

st.title("🌍 국가별 MBTI 유형 분포 대시보드")
st.markdown("국가를 선택하면 MBTI 16유형의 비율을 인터랙티브 그래프로 볼 수 있습니다!")

# 국가 선택
country = st.selectbox("국가를 선택하세요:", sorted(df["Country"].unique()))

# 선택한 국가 데이터 필터링
country_data = df[df["Country"] == country].iloc[0, 1:]  # MBTI 데이터만
country_df = pd.DataFrame({
    "MBTI": country_data.index,
    "비율": country_data.values
}).sort_values("비율", ascending=False)

# 색상 설정 (1등은 빨간색, 나머지는 점진적인 그라데이션)
colors = ["#ff4b4b"] + [f"rgba(255,150,{int(200+i*2)},0.8)" for i in range(1, len(country_df))]

# Plotly 막대 그래프
fig = px.bar(
    country_df,
    x="MBTI",
    y="비율",
    text=country_df["비율"].apply(lambda x: f"{x*100:.1f}%"),
)

# 그래프 색상 반영
fig.update_traces(marker_color=colors, textposition="outside")

# 그래프 디자인 조정
fig.update_layout(
    title=f"🇨🇳 {country}의 MBTI 유형 분포",
    xaxis_title="MBTI 유형",
    yaxis_title="비율 (단위: 비율)",
    template="plotly_white",
    title_font=dict(size=22, color="#333", family="Arial Black"),
    font=dict(size=14),
)

st.plotly_chart(fig, use_container_width=True)

# 하단 설명
st.markdown("---")
st.caption("📊 데이터 출처: countriesMBTI_16types.csv | 개발: Streamlit + Plotly")
