import streamlit as st

# 페이지 설정
st.set_page_config(page_title="🌟 나를 닮은 직업 찾기", page_icon="🧭", layout="centered")

# 타이틀
st.markdown("""
# 🌟 "내 성향으로 미래를 그려봐!" 🌟  
### MBTI로 보는 ✨맞춤형 진로 로드맵✨  
> 내가 어떤 사람인지 알면, 어울리는 일이 보이기 시작해요.  
""")

st.markdown("---")

# 사용자 선택 안내 (크게)
st.markdown("#### 📍 당신의 MBTI를 골라보세요:")
mbti_types = ["INTJ", "INFP", "ENTP", "ISFJ", "ENFP", "ISTP", "ESFJ", "INFJ"]
selected_mbti = st.selectbox("", mbti_types)

# MBTI 유형별 진로 데이터
mbti_data = {
    "INTJ": {
        "style": "🧠 전략적이고 냉철한 INTJ! 복잡한 문제도 침착하게 풀어나가는 타입이에요.",
        "jobs": [
            {"name": "AI 개발자 🤖", "reason": "체계적인 사고로 알고리즘을 설계하는 데 강해요."},
            {"name": "데이터 과학자 📊", "reason": "방대한 데이터 속 패턴을 읽는 통찰력이 뛰어나요."},
            {"name": "시스템 엔지니어 🛠️", "reason": "시스템의 구조와 안정성을 설계하는 데 적합해요."}
        ]
    },
    "INFP": {
        "style": "🌸 감성 충만한 INFP! 말은 적지만 따뜻한 가치와 상상이 가득하죠.",
        "jobs": [
            {"name": "시인 ✍️", "reason": "세상의 감정을 섬세하게 담아낼 수 있어요."},
            {"name": "일러스트레이터 🎨", "reason": "머릿속 세계를 그림으로 펼치는 데 탁월해요."},
            {"name": "심리상담가 💬", "reason": "타인의 마음을 깊이 이해하고 공감할 줄 알아요."}
        ]
    },
    "ENTP": {
        "style": "💡 아이디어 뿜뿜! 활기를 주는 ENTP는 대화도 잘하고 생각도 톡톡 튀죠!",
        "jobs": [
            {"name": "광고 기획자 📣", "reason": "창의적이고 도발적인 메시지를 만드는 데 딱이에요."},
            {"name": "스타트업 창업가 🚀", "reason": "모험과 변화를 즐기며 판을 뒤엎는 걸 좋아하잖아요!"},
            {"name": "방송인 🎙️", "reason": "사람들과 소통하고 주목받는 걸 좋아하니까요."}
        ]
    },
    "ISFJ": {
        "style": "💖 따뜻하고 묵묵한 헌신가, 바로 ISFJ! 책임감이 누구보다 강해요.",
        "jobs": [
            {"name": "간호사 👩‍⚕️", "reason": "섬세하고 헌신적인 돌봄이 필요한 직업이죠."},
            {"name": "사회복지사 🧓", "reason": "약자들을 돌보는 데에서 큰 보람을 느껴요."},
            {"name": "교직원 🏫", "reason": "규칙적인 환경 속에서 누군가를 돕는 일에 잘 어울려요."}
        ]
    },
    "ENFP": {
        "style": "🌈 자유로운 영혼, ENFP! 열정과 호기심으로 항상 새로운 걸 탐색하죠.",
        "jobs": [
            {"name": "유튜버 🎥", "reason": "끊임없이 새로운 콘텐츠를 만들고 표현하는 걸 즐기니까요."},
            {"name": "콘서트 기획자 🎤", "reason": "흥과 기획력이 넘치는 당신에게 찰떡이에요."},
            {"name": "무용가 💃", "reason": "표현력과 에너지로 무대를 사로잡을 수 있어요."}
        ]
    },
    "ISTP": {
        "style": "🔧 실용적이고 조용한 해결사, ISTP! 말보다는 행동으로 보여주는 타입이에요.",
        "jobs": [
            {"name": "기계공 🧰", "reason": "복잡한 기계나 장비를 다루는 데 능숙해요."},
            {"name": "자동차 정비사 🚗", "reason": "문제를 분석하고 손으로 해결하는 걸 좋아해요."},
            {"name": "드론 전문가 🚁", "reason": "기술과 모험을 동시에 즐기는 당신에게 어울려요."}
        ]
    },
    "ESFJ": {
        "style": "🤝 친절하고 조화로운 ESFJ! 함께할 때 더 빛나는 팀워크의 달인이죠.",
        "jobs": [
            {"name": "이벤트 플래너 🎈", "reason": "사람들을 위한 특별한 순간을 기획해요."},
            {"name": "호텔 매니저 🏨", "reason": "세심한 서비스로 모두를 만족시키는 걸 좋아해요."},
            {"name": "초등교사 🧑‍🏫", "reason": "아이들과 따뜻한 유대를 맺는 데 강점이 있어요."}
        ]
    },
    "INFJ": {
        "style": "🔮 통찰력 있고 조용한 INFJ! 깊은 사고와 따뜻한 마음으로 세상을 바꾸고 싶어하죠.",
        "jobs": [
            {"name": "작가 ✍️", "reason": "깊이 있는 메시지를 글로 전할 수 있어요."},
            {"name": "청소년 상담사 🧒", "reason": "복잡한 감정을 진심으로 들어줄 수 있어요."},
            {"name": "사회운동가 🕊️", "reason": "정의롭고 지속가능한 세상을 만들고자 해요."}
        ]
    }
}

# 결과 출력
if selected_mbti:
    profile = mbti_data[selected_mbti]
    st.markdown("---")
    st.subheader("💬 성향 분석")
    st.markdown(f"**{profile['style']}**")
    st.markdown("## 🎯 추천 진로")
    for job in profile["jobs"]:
        st.markdown(f"### {job['name']}")
        st.markdown(f"- {job['reason']}")
    st.markdown("---")
    st.success("🌟 진로는 정답이 아니라 방향이에요. 당신다운 길을 스스로 열어가 보세요!")
