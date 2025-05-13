import streamlit as st

# MBTI 진로 추천 데이터 (INTJ, INFP 예시 / 나머지는 같은 형식으로 확장 가능)
mbti_profiles = {
    "INTJ": {
        "style": "🧠 논리적이고 체계적인 당신, INTJ! 조용한 열정으로 세상을 전략적으로 바라보는 타입이에요.",
        "fields": {
            "과학·기술 분야": [
                ("AI 연구원 🤖", "미래를 설계하고 알고리즘을 구상하는 데 강점 있어요."),
                ("데이터 분석가 📊", "숫자 속 의미를 꿰뚫는 통찰력이 있어요."),
                ("시스템 설계자 🛠️", "복잡한 구조를 정리하고 최적화하는 데 능해요.")
            ],
            "경영·전략 분야": [
                ("전략기획자 🧩", "큰 그림을 그리고 장기 계획을 세우는 데 적합해요."),
                ("프로젝트 매니저 📋", "체계적으로 일정을 조율하고 리더십을 발휘하죠.")
            ],
            "교육·연구 분야": [
                ("대학교수 🎓", "지식을 깊이 탐구하고 후학을 양성하는 데 의미를 느껴요."),
                ("과학 칼럼니스트 🧪", "복잡한 지식을 쉽게 풀어내는 데 뛰어나요.")
            ]
        }
    },
    "INFP": {
        "style": "🌸 감성적이고 창의적인 당신, INFP! 이상을 좇으며 세상을 더 아름답게 만들고 싶어하죠.",
        "fields": {
            "예술·창작 분야": [
                ("일러스트레이터 🎨", "자신만의 색으로 감정을 표현하는 데 탁월해요."),
                ("시인 ✍️", "섬세한 감정과 언어 감각으로 사람들의 마음을 움직여요."),
                ("웹툰 작가 ✏️", "자신만의 이야기로 사람들의 공감을 얻어요.")
            ],
            "상담·복지 분야": [
                ("심리상담사 💬", "타인의 감정을 공감하고 도와주는 데 진심이에요."),
                ("청소년 지도사 🧒", "아이들의 고민을 함께 나누고 성장시키는 역할을 해요.")
            ],
            "출판·문화 분야": [
                ("에디터 📰", "깊이 있는 콘텐츠를 기획하고 편집하는 데 흥미를 느껴요."),
                ("콘텐츠 작가 🪶", "세상을 바라보는 따뜻한 시선을 글로 풀어내요.")
            ]
        }
    }
}

# 앱 구성
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌟", layout="centered")
st.title("🌈 나를 닮은 진로 찾기")
st.subheader("MBTI로 알아보는 나만의 진로 제안서 ✨")
st.write("단순한 성격 분석을 넘어서, **당신다운 진로**를 함께 상상해봐요!")

# 사용자 MBTI 선택
st.markdown("#### 📍 당신의 MBTI를 골라보세요:")
selected_mbti = st.selectbox("", list(mbti_profiles.keys()))

# 결과 출력
if selected_mbti:
    profile = mbti_profiles[selected_mbti]
    st.markdown("---")
    st.subheader(f"💬 당신은... {selected_mbti}!")
    st.write(profile["style"])

    for field_name, jobs in profile["fields"].items():
        st.markdown(f"### 🎯 {field_name}")
        for job_title, job_reason in jobs:
            # 직업명: 크고 들여쓰기 (### 제목 수준)
            st.markdown(f"#### &nbsp;&nbsp;&nbsp;{job_title}", unsafe_allow_html=True)
            # 설명: 기본 크기, 직업명보다 한 칸 더 들여쓰기
            st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{job_reason}", unsafe_allow_html=True)

    st.markdown("---")
    st.success("🌟 진로는 정답이 아니라 탐험이에요. 당신의 성향을 나침반 삼아 자신만의 길을 만들어보세요!")
