import streamlit as st

# 🎨 제목
st.title("🌟 MBTI로 보는 나의 진로 추천기 🎯")
st.write("너의 성격 유형(MBTI)에 딱 맞는 진로를 추천해줄게! 😎")

# 🧩 MBTI 목록
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI 선택
selected_mbti = st.selectbox("너의 MBTI를 골라봐! 🔍", mbti_list)

# 진로 데이터 🎓
career_data = {
    "INTJ": {
        "career": ["데이터 분석가", "전략 기획자"],
        "major": "컴퓨터공학, 산업공학, 경영학",
        "personality": "논리적이고 계획적인 너에게 어울리는 직업이야! 목표를 향해 꾸준히 나아가는 타입 💡"
    },
    "INTP": {
        "career": ["연구원", "AI 개발자"],
        "major": "물리학, 컴퓨터공학, 인공지능학",
        "personality": "탐구심이 강하고 새로운 걸 깊게 파는 스타일! 🧠 실험하고 분석하는 일에 찰떡이야."
    },
    "ENTJ": {
        "career": ["경영 컨설턴트", "기업가"],
        "major": "경영학, 경제학, 리더십학",
        "personality": "리더십이 넘치고 추진력이 강한 타입! 💪 사람들과 함께 목표를 이루는 게 어울려."
    },
    "ENTP": {
        "career": ["창업가", "마케팅 기획자"],
        "major": "경영학, 광고홍보학, 미디어학",
        "personality": "아이디어 뱅크💡 도전정신 가득한 너에게 창의적인 일이 잘 맞아!"
    },
    "INFJ": {
        "career": ["심리상담사", "사회복지사"],
        "major": "심리학, 사회복지학, 교육학",
        "personality": "공감능력이 높고 사람을 돕는 걸 좋아하는 따뜻한 성격 💕"
    },
    "INFP": {
        "career": ["작가", "디자이너"],
        "major": "문예창작학, 시각디자인학, 예술학",
        "personality": "감성 풍부한 이상주의자 🌷 창의적이고 자유로운 일을 좋아해!"
    },
    "ENFJ": {
        "career": ["교사", "홍보 전문가"],
        "major": "교육학, 커뮤니케이션학, 심리학",
        "personality": "사람을 이끄는 힘이 있고, 따뜻하게 격려할 줄 아는 리더형 💫"
    },
    "ENFP": {
        "career": ["예술가", "콘텐츠 기획자"],
        "major": "영상학, 미디어커뮤니케이션학, 예술학",
        "personality": "에너지 넘치고 상상력이 풍부한 너! 🌈 자유롭게 표현하는 일이 딱 맞아."
    },
    "ISTJ": {
        "career": ["회계사", "공무원"],
        "major": "회계학, 행정학, 법학",
        "personality": "책임감 강하고 꼼꼼한 현실주의자 📘 정확한 일처리가 강점이야."
    },
    "ISFJ": {
        "career": ["간호사", "교사"],
        "major": "간호학, 교육학, 사회복지학",
        "personality": "따뜻하고 헌신적인 성격 ❤️ 누군가를 돌보는 일이 잘 어울려."
    },
    "ESTJ": {
        "career": ["경영자", "프로젝트 매니저"],
        "major": "경영학, 산업공학, 행정학",
        "personality": "현실적이고 리더십이 뛰어난 타입 💼 계획 세우는 걸 좋아하지?"
    },
    "ESFJ": {
        "career": ["상담교사", "홍보전문가"],
        "major": "심리학, 커뮤니케이션학, 교육학",
        "personality": "사람들과 함께하는 걸 좋아하는 사회형 😊 협력과 소통이 강점이야!"
    },
    "ISTP": {
        "career": ["엔지니어", "정비사"],
        "major": "기계공학, 전자공학, 로봇공학",
        "personality": "문제 해결에 강하고 손재주 좋은 현실주의자 🔧"
    },
    "ISFP": {
        "career": ["패션디자이너", "사진작가"],
        "major": "패션학, 디자인학, 예술학",
        "personality": "감각적이고 조용한 예술가 타입 🎨 미적 감각이 뛰어나!"
    },
    "ESTP": {
        "career": ["영업 전문가", "스포츠 코치"],
        "major": "체육학, 경영학, 커뮤니케이션학",
        "personality": "활동적이고 즉흥적인 스타일 ⚡ 도전적인 일이 잘 어울려!"
    },
    "ESFP": {
        "career": ["배우", "이벤트 플래너"],
        "major": "공연예술학, 관광학, 커뮤니케이션학",
        "personality": "사람들에게 에너지를 주는 무대형 인싸 🌟 즐겁게 일하는 게 최고야!"
    }
}

# 버튼 클릭 시 결과 출력 🎯
if st.button("내 진로 보기 🚀"):
    data = career_data.get(selected_mbti)
    st.subheader(f"🌈 {selected_mbti} 유형의 진로 추천 🌈")
    st.write(f"✨ 추천 진로: **{data['career'][0]}**, **{data['career'][1]}**")
    st.write(f"🎓 관련 학과: {data['major']}")
    st.write(f"💬 성격 특징: {data['personality']}")
    st.balloons()
