import streamlit as st
import random
import datetime

# 제목 🎉
st.title("🎮 랜덤 챌린지 생성기!")
st.write("오늘 뭐 할지 고민될 땐? 내가 랜덤으로 정~해줄게! 😎")

# 이름 입력 💬
name = st.text_input("너 이름이 뭐야? ✍️", "")

# 버튼 클릭 🎲
if st.button("오늘의 챌린지 뽑기! 🎯"):
    if name.strip() == "":
        st.warning("이름 먼저 알려줘야지~ 😅")
    else:
        # 랜덤 챌린지 리스트 🎯
        challenges = [
            "오늘 10분만이라도 스트레칭 하기 🧘",
            "휴대폰 없이 1시간 살아보기 📵",
            "가족에게 먼저 인사하기 😊",
            "물 8컵 마시기 💧",
            "좋아하는 노래 들으며 산책하기 🎧",
            "책 10쪽만 읽기 📖",
            "친구에게 안부 톡 보내기 💌",
            "오늘 하루 감사한 일 3가지 적기 🌈",
            "하늘 사진 찍기 ☁️",
            "웃긴 밈 찾아서 친구랑 공유하기 😂"
        ]

        # 랜덤 선택
        challenge = random.choice(challenges)

        # 현재 날짜
        today = datetime.date.today().strftime("%Y-%m-%d")

        # 결과 출력 💥
        st.success(f"✨ {name}의 {today} 랜덤 챌린지! ✨")
        st.write(f"👉 **{challenge}** 👈")
        st.balloons()
