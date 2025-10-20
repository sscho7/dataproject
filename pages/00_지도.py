# app.py
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster
import pandas as pd

st.set_page_config(page_title="Seoul - Top 10 for Foreign Visitors", layout="wide")

st.title("🌏 외국인이 좋아하는 서울 관광지 TOP 10")
st.write("지도에서 마커를 클릭하면 간단한 설명이 나옵니다. 사이드바에서 표시 옵션을 조절하세요.")

# 관광지 데이터 (이름, 위도, 경도, 간단 설명)
spots = [
    {"name":"Gyeongbokgung Palace (경복궁)", "lat":37.579617, "lon":126.977041,
     "desc":"조선의 대표 궁궐. 한복 대여 후 방문하면 입장료 면제되는 곳이 많음."},
    {"name":"Changdeokgung Palace & Secret Garden (창덕궁)", "lat":37.582601, "lon":126.991041,
     "desc":"유네스코 세계유산, 후원이 유명함."},
    {"name":"Bukchon Hanok Village (북촌한옥마을)", "lat":37.582600, "lon":126.983000,
     "desc":"전통 한옥이 밀집한 사진 명소."},
    {"name":"Insadong (인사동)", "lat":37.574011, "lon":126.984688,
     "desc":"전통 공예와 찻집, 기념품 쇼핑에 적합."},
    {"name":"Myeongdong (명동)", "lat":37.560976, "lon":126.985023,
     "desc":"쇼핑과 스트리트푸드가 유명한 대표 상권."},
    {"name":"N Seoul Tower / Namsan (남산서울타워)", "lat":37.551169, "lon":126.988227,
     "desc":"서울 야경을 한눈에 볼 수 있는 전망 포인트."},
    {"name":"Hongdae (홍대/홍익대학교 거리)", "lat":37.556268, "lon":126.923623,
     "desc":"젊음의 거리, 스트리트 퍼포먼스와 카페·음악문화."},
    {"name":"Dongdaemun Design Plaza (동대문 DDP)", "lat":37.566295, "lon":127.009389,
     "desc":"현대 건축과 야간 조명이 유명한 디자인 허브."},
    {"name":"Gwangjang Market (광장시장)", "lat":37.570128, "lon":127.004532,
     "desc":"전통 먹거리(비빔밥, 마약김밥, 빈대떡 등)로 인기."},
    {"name":"Itaewon (이태원)", "lat":37.534602, "lon":126.994973,
     "desc":"다문화 음식과 밤문화가 발달한 외국인 친화 지역."},
]

df = pd.DataFrame(spots)

# Sidebar controls
st.sidebar.header("지도 옵션")
start_lat = st.sidebar.number_input("지도 중심 위도", value=37.56, format="%.6f")
start_lon = st.sidebar.number_input("지도 중심 경도", value=126.98, format="%.6f")
zoom = st.sidebar.slider("초기 줌 레벨", min_value=10, max_value=15, value=12)
use_cluster = st.sidebar.checkbox("마커 클러스터 사용", value=True)
show_list = st.sidebar.checkbox("관광지 리스트 보기", value=True)
popup_more = st.sidebar.checkbox("팝업에 설명 보이기", value=True)

# Build folium map
m = folium.Map(location=[start_lat, start_lon], zoom_start=zoom)

if use_cluster:
    marker_group = MarkerCluster()
else:
    marker_group = folium.FeatureGroup(name="Attractions")

for _, row in df.iterrows():
    popup_html = f"<b>{row['name']}</b>"
    if popup_more:
        popup_html += f"<br><small>{row['desc']}</small>"
    folium_marker = folium.Marker(location=[row['lat'], row['lon']],
                                  popup=folium.Popup(popup_html, max_width=300),
                                  tooltip=row['name'])
    marker_group.add_child(folium_marker)

m.add_child(marker_group)
m.add_child(folium.LayerControl())

# Display map
st.header("지도")
map_area = st_folium(m, width=1000, height=650)

# Optional: show list / table
if show_list:
    st.header("관광지 목록")
    st.dataframe(df[["name", "lat", "lon", "desc"]].rename(columns={
        "name":"이름", "lat":"위도", "lon":"경도", "desc":"설명"
    }))

st.markdown("---")
st.caption("데이터 출처 예시: TripAdvisor, VisitKorea 등 여행 관련 자료를 종합하여 선정. (예: 경복궁, 명동, 남산타워 등).")
