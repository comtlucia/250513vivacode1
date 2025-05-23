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
#mbti_types = ["INTJ", "INFP", "ENTP", "ISFJ", "ENFP", "ISTP", "ESFJ", "INFJ"]
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

selected_mbti = st.selectbox("", mbti_types)

# MBTI 유형별 진로 데이터
mbti_data = {
    #
    "ISTJ": {
        "style": "📘 책임감 있고 신중한 ISTJ! 규칙과 질서를 중시하며 묵묵히 자신의 역할을 완수해요.",
        "jobs": [
            {"name": "회계사 📑", "reason": "정확하고 체계적인 숫자 분석에 강해요."},
            {"name": "공무원 🏛️", "reason": "규칙과 절차를 잘 따르며 안정적인 환경에서 능력을 발휘해요."},
            {"name": "법무 행정 전문가 ⚖️", "reason": "절차적 사고로 법률을 다루는 데 적합해요."},
            {"name": "데이터 품질 관리자 📊", "reason": "세밀한 확인과 꼼꼼함으로 데이터를 관리해요."},
            {"name": "인사관리 전문가 🧾", "reason": "규칙과 구조를 갖춘 조직 속에서 인재를 관리하는 데 능해요."}
        ]
    },
    "ISFP": {
        "style": "🎨 온화하고 감성적인 ISFP! 자유롭게 감정을 표현하며 조용한 실천가예요.",
        "jobs": [
            {"name": "플로리스트 🌷", "reason": "자연을 사랑하고 미적 감각이 뛰어나요."},
            {"name": "메이크업 아티스트 💄", "reason": "감각적인 표현으로 사람들을 아름답게 만드는 데 재능 있어요."},
            {"name": "사진 작가 📸", "reason": "순간을 예술로 포착하는 데 몰입할 수 있어요."},
            {"name": "애완동물 행동 전문가 🐶", "reason": "동물과의 교감을 중요시하며 조용한 배려심이 있어요."},
            {"name": "산림 치유 지도사 🌲", "reason": "자연을 통해 사람들의 마음을 치유하는 데 적합해요."}
        ]
    },
    "ESTP": {
        "style": "⚡ 에너지 넘치고 즉흥적인 ESTP! 도전을 즐기며 순간의 선택에도 강해요.",
        "jobs": [
            {"name": "스포츠 트레이너 🏋️", "reason": "활동적이며 몸을 쓰는 일에 열정을 느껴요."},
            {"name": "소방관 🚒", "reason": "위기 상황에서 빠르고 침착한 판단을 내려요."},
            {"name": "응급 구조사 🚑", "reason": "현장 대응과 실질적인 조치를 신속하게 할 수 있어요."},
            {"name": "판매 컨설턴트 🛍️", "reason": "사람과의 소통과 현장 감각이 탁월해요."},
            {"name": "중계 아나운서 🎙️", "reason": "순간 판단력과 말솜씨가 중요한 분야에 강해요."}
        ]
    },
    "ESTJ": {
        "style": "📋 조직을 이끄는 관리자형 ESTJ! 계획대로 일하는 걸 선호하고 리더십이 뛰어나요.",
        "jobs": [
            {"name": "경영 관리자 🧑‍💼", "reason": "팀과 자원을 효율적으로 관리하는 데 탁월해요."},
            {"name": "군 간부 🎖️", "reason": "규율과 명확한 체계를 중시하며 책임감이 강해요."},
            {"name": "건설 현장 관리자 🚧", "reason": "구조적 문제를 해결하며 프로젝트를 이끄는 데 강점이 있어요."},
            {"name": "생산 품질 관리자 🏭", "reason": "정확성과 품질을 위한 시스템 개선을 즐겨요."},
            {"name": "학교 행정 관리자 🏫", "reason": "교육기관의 체계를 유지하고 발전시키는 역할을 잘해요."}
        ]
    },
    "ESFP": {
        "style": "🎉 즐거움과 감각의 사람, ESFP! 사람들과 어울리는 것을 즐기며 순간의 행복을 나누고 싶어해요.",
        "jobs": [
            {"name": "공연 예술가 🎭", "reason": "무대 위에서 감정을 자유롭게 표현하는 데 강해요."},
            {"name": "관광 가이드 🗺️", "reason": "새로운 장소와 사람을 연결해주는 일에 흥미를 느껴요."},
            {"name": "호텔리어 🏨", "reason": "고객 응대와 서비스에서 따뜻함을 전해요."},
            {"name": "아동체육 교사 ⚽", "reason": "아이들과 함께 몸을 움직이며 즐겁게 소통할 수 있어요."},
            {"name": "MC / 사회자 🎤", "reason": "유쾌한 분위기와 진행 능력이 돋보여요."}
        ]
    },
    "ENTJ": {
        "style": "🏆 목표지향적이고 리더십 강한 ENTJ! 조직을 만들고 이끄는 데 자신감이 넘쳐요.",
        "jobs": [
            {"name": "경영 컨설턴트 📈", "reason": "효율과 전략을 바탕으로 조직을 성장시키는 데 능해요."},
            {"name": "벤처 투자 심사역 💼", "reason": "미래 가능성을 분석하고 큰 방향을 제시해요."},
            {"name": "프로젝트 매니저 📋", "reason": "팀을 통솔하며 계획적으로 성과를 이끌어내요."},
            {"name": "해외영업 전문가 🌍", "reason": "글로벌 환경 속에서 목표를 향해 과감히 나아가요."},
            {"name": "변호사 ⚖️", "reason": "복잡한 문제를 전략적으로 풀고 논리적으로 설득해요."}
        ]
    },
    "ENFJ": {
    "style": "🌟 따뜻하고 설득력 있는 리더, ENFJ! 다른 사람을 도우며 함께 성장하는 걸 중요하게 생각해요.",
    "jobs": [
        {"name": "고등학교 교사 🧑‍🏫", "reason": "학생들을 진심으로 이끌고 가르치는 데 열정적이에요."},
        {"name": "홍보 마케터 📢", "reason": "사람들의 감정을 움직이는 메시지를 만드는 데 능해요."},
        {"name": "비영리단체 활동가 ❤️", "reason": "사회적 가치 실현을 위해 헌신하는 데 보람을 느껴요."},
        {"name": "기업 교육 강사 🗣️", "reason": "조직 내 구성원을 성장시키는 역할에 강점을 보여요."},
        {"name": "심리 상담사 💬", "reason": "사람의 감정을 섬세하게 파악하고 치유하려는 마음이 깊어요."}
      ]
   },

    "INTP": {
        "style": "🔍 깊이 사고하고 분석하는 INTP! 창의적인 아이디어와 논리로 세상을 해석해요.",
        "jobs": [
            {"name": "빅데이터 분석가 📊", "reason": "복잡한 데이터에서 인사이트를 도출하는 데 능해요."},
            {"name": "컴퓨터 과학자 💻", "reason": "알고리즘과 구조에 대한 이해가 뛰어나요."},
            {"name": "AI 윤리 연구자 🧠", "reason": "기술과 철학 사이의 교차점을 탐색하는 걸 즐겨요."},
            {"name": "기술 필자 ✍️", "reason": "전문적인 지식을 논리적으로 글로 풀어내는 데 탁월해요."},
            {"name": "리서치 엔지니어 🔬", "reason": "새로운 개념을 실험하고 구조화하는 데 몰입해요."}
        ]
    }, 
    #
    "INTJ": {
        "style": "🧠 전략적이고 냉철한 INTJ! 복잡한 문제도 침착하게 풀어나가는 타입이에요.",
        "jobs": [
            {"name": "AI 알고리즘 개발자 🤖", "reason": "체계적인 논리로 복잡한 문제를 해결하는 데 강해요."},
            {"name": "데이터 과학자 📊", "reason": "숫자 속 의미를 분석해 전략적 결정을 내리는 데 능숙해요."},
            {"name": "전략기획 컨설턴트 🧠", "reason": "큰 그림을 그리고 기업의 방향성을 제시하는 데 적합해요."},
            {"name": "정보보안 전문가 🔐", "reason": "리스크를 예측하고 철저한 대비책을 세우는 데 능해요."},
            {"name": "물리학자 🔬", "reason": "깊이 있는 탐구와 체계적 연구에 몰입할 수 있어요."}
        ]
    },
    "INFP": {
        "style": "🌸 감성 충만한 INFP! 말은 적지만 따뜻한 가치와 상상이 가득하죠.",
        "jobs": [
            {"name": "시인 ✍️", "reason": "세상의 감정을 섬세하게 담아내는 데 탁월해요."},
            {"name": "아동문학 작가 📚", "reason": "상상력과 따뜻함으로 어린이의 세계를 표현할 수 있어요."},
            {"name": "예술치료사 🎭", "reason": "예술을 통해 사람들의 마음을 치유할 수 있어요."},
            {"name": "청소년 상담사 💬", "reason": "청소년들의 고민을 진심으로 들어줄 수 있어요."},
            {"name": "인권 NGO 활동가 🌍", "reason": "사회 정의와 약자를 향한 진심이 행동으로 이어져요."}
        ]
    },
    "ENTP": {
        "style": "💡 아이디어 뿜뿜! 활기를 주는 ENTP는 대화도 잘하고 생각도 톡톡 튀죠!",
        "jobs": [
            {"name": "광고 캠페인 기획자 📣", "reason": "창의적 전략과 커뮤니케이션 감각이 뛰어나요."},
            {"name": "스타트업 CEO 🚀", "reason": "새로운 아이디어로 세상에 도전하는 데 주저함이 없어요."},
            {"name": "방송 프로그램 PD 🎥", "reason": "기획력과 통찰력으로 다채로운 콘텐츠를 만드는 데 강해요."},
            {"name": "비즈니스 개발 매니저 🤝", "reason": "사람들과의 네트워킹과 협업에서 에너지를 얻어요."},
            {"name": "테크 유튜버 🎬", "reason": "정보 전달력과 재미를 겸비해 사람들을 끌어들이는 데 탁월해요."}
        ]
    },
    "ISFJ": {
        "style": "💖 따뜻하고 묵묵한 헌신가, 바로 ISFJ! 책임감이 누구보다 강해요.",
        "jobs": [
            {"name": "초등학교 교사 🧑‍🏫", "reason": "어린이에게 안정감을 주고 성장을 돕는 데 헌신적이에요."},
            {"name": "특수교육 교사 🧩", "reason": "배려심과 인내심으로 다양한 학생을 이끌 수 있어요."},
            {"name": "간호사 👩‍⚕️", "reason": "환자의 상태를 세심하게 돌보는 데 능숙해요."},
            {"name": "사회복지기관 행정직 🏢", "reason": "조용히, 성실하게 체계를 유지하는 데 강점을 보여요."},
            {"name": "의료 행정 코디네이터 🗂️", "reason": "질서와 체계를 중시하며 헌신적으로 일할 수 있어요."}
        ]
    },
    "ENFP": {
        "style": "🌈 자유로운 영혼, ENFP! 열정과 호기심으로 항상 새로운 걸 탐색하죠.",
        "jobs": [
            {"name": "콘텐츠 크리에이터 🎥", "reason": "에너지 넘치는 소통과 창의력으로 사람들과 연결돼요."},
            {"name": "무대 공연 연출가 🎭", "reason": "사람들의 감정을 자극하는 연출에 재능이 있어요."},
            {"name": "청소년 진로 코치 🧭", "reason": "학생의 가능성을 발견하고 이끌어주는 데 기쁨을 느껴요."},
            {"name": "국제교류 프로그램 운영자 🌐", "reason": "다양한 문화를 연결하고 이벤트를 기획하는 데 탁월해요."},
            {"name": "모바일 앱 UX 디자이너 📱", "reason": "사용자의 감성과 창의성을 연결하는 데 흥미를 느껴요."}
        ]
    },
    "ISTP": {
        "style": "🔧 실용적이고 조용한 해결사, ISTP! 말보다는 행동으로 보여주는 타입이에요.",
        "jobs": [
            {"name": "기계 설계 기술자 🛠️", "reason": "정밀한 설계와 기능 중심 사고가 뛰어나요."},
            {"name": "자동차 정비 기술자 🚗", "reason": "복잡한 구조를 빠르게 파악하고 해결할 수 있어요."},
            {"name": "로봇 프로그래머 🤖", "reason": "기계와 소프트웨어를 결합하는 논리력이 있어요."},
            {"name": "드론 운영 전문가 🚁", "reason": "신기술을 빠르게 익히고 조작하는 데 능숙해요."},
            {"name": "3D 프린팅 기술자 🧱", "reason": "도면을 직접 현실로 구현하는 데 흥미가 있어요."}
        ]
    },
    "ESFJ": {
        "style": "🤝 친절하고 조화로운 ESFJ! 함께할 때 더 빛나는 팀워크의 달인이죠.",
        "jobs": [
            {"name": "이벤트 플래너 🎈", "reason": "사람들을 위한 특별한 순간을 기획하는 데 재능 있어요."},
            {"name": "호텔 프론트 매니저 🏨", "reason": "세심한 서비스와 대인 친화력이 뛰어나요."},
            {"name": "학교 상담교사 🎓", "reason": "학생을 이해하고 돕는 진심 어린 태도가 강점이에요."},
            {"name": "지역사회 복지공무원 🏛️", "reason": "이웃과 공동체를 위해 일하는 데 보람을 느껴요."},
            {"name": "초등학교 교사 🧑‍🏫", "reason": "아이들에게 따뜻한 관심과 질서를 제공할 수 있어요."}
        ]
    },
    "INFJ": {
        "style": "🔮 통찰력 있고 조용한 INFJ! 깊은 사고와 따뜻한 마음으로 세상을 바꾸고 싶어하죠.",
        "jobs": [
            {"name": "작가 ✍️", "reason": "깊이 있는 메시지를 글로 풀어내는 능력이 있어요."},
            {"name": "청소년 상담교사 🧒", "reason": "학생 개개인의 마음을 읽고 보듬는 데 탁월해요."},
            {"name": "사회운동 기획가 🕊️", "reason": "신념 있는 활동으로 세상을 변화시키는 데 열정적이에요."},
            {"name": "심리학 연구자 🧠", "reason": "인간의 내면을 탐구하고 설명하는 데 몰입할 수 있어요."},
            {"name": "문화콘텐츠 기획자 📽️", "reason": "의미 있는 스토리로 사회에 영향력 있는 콘텐츠를 만들 수 있어요."}
        ]
    }
}
# 결과 출력
if selected_mbti:
    profile = mbti_data[selected_mbti]
    st.markdown("---")
    st.subheader("💬 성향 분석")
    st.markdown(f"**{profile['style']}**")
    st.markdown("---")
    st.markdown("### 🎯 추천 진로")
    for job in profile["jobs"]:
        st.markdown(f"#### {job['name']}")
        st.markdown(f"- {job['reason']}")
    st.markdown("---")
    st.success("🌟 진로는 정답이 아니라 방향이에요. 당신다운 길을 스스로 열어가 보세요!")
