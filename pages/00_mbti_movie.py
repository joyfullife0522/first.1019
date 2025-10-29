import streamlit as st

# -------------------- 기본 설정 --------------------
st.set_page_config(page_title="MBTI Movie Matcher 🎬✨", layout="centered")

HEADER = "# 🎬 MBTI Movie Matcher"
SUBHEADER = "당신의 MBTI를 선택하면 감성에 딱 맞는 영화를 추천해줘요. 😎🍿"

st.markdown(HEADER)
st.markdown(SUBHEADER)
st.write("---")

# -------------------- MBTI 목록 --------------------
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP",
]

# -------------------- MBTI별 영화 추천 DB --------------------
MOVIE_DB = {
    "INTJ": [
        ("Inception", "2010", "🧠🔍✨", "복잡한 플롯과 전략적 사고가 즐거운 영화"),
        ("The Imitation Game", "2014", "🧩💻🇬🇧", "지적인 문제 해결과 침착한 주인공의 이야기"),
        ("Ex Machina", "2014", "🤖🧠🔬", "AI와 윤리에 대해 사려깊게 고민하게 만드는 작품"),
    ],
    "INTP": [
        ("The Matrix", "1999", "🌀🧠💡", "현실과 이론을 뒤엎는 SF 클래식"),
        ("Good Will Hunting", "1997", "📚🧠🤝", "지성과 감성의 균형을 보는 영화"),
        ("Primer", "2004", "🔧⏳🧪", "저예산이지만 머리를 굴리게 만드는 시간영화"),
    ],
    "ENTJ": [
        ("The Social Network", "2010", "🏢💼⚡", "리더십과 냉정한 전략이 돋보이는 이야기"),
        ("The Wolf of Wall Street", "2013", "💰🎢🔥", "대담한 목표와 추진력의 드라마"),
        ("Margin Call", "2011", "📉🏦🧾", "위기상황에서의 결정과 책임"),
    ],
    "ENTP": [
        ("Catch Me If You Can", "2002", "🕵️‍♂️✈️🎭", "재치있고 유머러스한 반전의 즐거움"),
        ("The Grand Budapest Hotel", "2014", "🎩🛎️🎨", "독창적 스타일과 재기발랄한 유머"),
        ("The Big Short", "2015", "💸📉🤯", "비정형적 시각으로 큰 이야기를 풀어냄"),
    ],
    "INFJ": [
        ("Her", "2013", "💬🤍🤖", "감성적이면서 사려깊은 로맨스+철학"),
        ("Amélie", "2001", "🌷😊🎨", "소박한 선의와 아름다운 시선으로 채운 영화"),
        ("Pan's Labyrinth", "2006", "🌑🧚‍♀️✨", "어둡고 시적이며 상징이 많은 작품"),
    ],
    "INFP": [
        ("Eternal Sunshine of the Spotless Mind", "2004", "💔🧠🌈", "감정의 깊이를 예쁘게 풀어낸 영화"),
        ("The Secret Life of Walter Mitty", "2013", "🌍✨🧭", "상상과 모험을 사랑하는 이들에게"),
        ("Into the Wild", "2007", "🏕️🚶‍♂️🌲", "자아 탐색과 자연을 향한 갈망의 이야기"),
    ],
    "ENFJ": [
        ("Dead Poets Society", "1989", "📚🎓🕊️", "사람들의 가능성을 끌어내는 따뜻한 리더"),
        ("Little Miss Sunshine", "2006", "🚐👨‍👩‍👧‍👦😂", "팀워크와 연대가 주는 힘"),
        ("The Pursuit of Happyness", "2006", "💪👨‍👦🌟", "희망과 헌신이 중심인 감동작"),
    ],
    "ENFP": [
        ("La La Land", "2016", "🎶💃🌆", "열정적이고 낭만적인 감성의 향연"),
        ("Big Fish", "2003", "🧚‍♂️🌊🎩", "상상력과 이야기로 삶을 축복하는 영화"),
        ("About Time", "2013", "⌛❤️👪", "따뜻하고 감성적인 로맨스"),
    ],
    "ISTJ": [
        ("Bridge of Spies", "2015", "🕊️⚖️🏛️", "원칙과 성실함으로 문제를 해결하는 이야기"),
        ("A Few Good Men", "1992", "⚖️👨‍✈️🔥", "명확한 논리와 책임이 돋보이는 법정극"),
        ("The Shawshank Redemption", "1994", "🏛️🔒🌄", "인내와 신념에 관한 보편적 메시지"),
    ],
    "ISFJ": [
        ("Pride & Prejudice", "2005", "💃🏡🌸", "섬세하고 따뜻한 감정선의 고전 로맨스"),
        ("The Help", "2011", "☕👩‍👩‍👧‍👧🤝", "연대와 배려가 중심인 이야기"),
        ("Finding Nemo", "2003", "🐠🌊👪", "보호와 책임의 따뜻한 가족영화"),
    ],
    "ESTJ": [
        ("Gladiator", "2000", "⚔️🏛️🔥", "리더십과 명확한 목표의 서사"),
        ("Air Force One", "1997", "✈️🛡️🇺🇸", "결단력과 위기관리의 스릴"),
        ("Apollo 13", "1995", "🚀🛠️🤝", "조직적 문제 해결의 클래식"),
    ],
    "ESFJ": [
        ("The Intouchables", "2011", "🤝😂💙", "사람 사이의 온정과 유머가 주는 힘"),
        ("Julie & Julia", "2009", "🍳📖💌", "사교성과 따뜻함을 즐기는 이들에게"),
        ("Mrs. Doubtfire", "1993", "👨‍👧‍👦😂🎭", "가족애와 유머가 섞인 영화"),
    ],
    "ISTP": [
        ("Drive", "2011", "🏎️🌃🔪", "침착하고 감각적인 액션무비"),
        ("Mad Max: Fury Road", "2015", "🏜️🚗💥", "속도와 실용성, 즉흥적 판타지"),
        ("No Country for Old Men", "2007", "🔫🌵🕶️", "냉정하고 묵직한 스릴러"),
    ],
    "ISFP": [
        ("Moonlight", "2016", "🌊🌙🎭", "감성적이고 시적인 영상미"),
        ("Call Me By Your Name", "2017", "🍑🌞🎻", "섬세한 감정과 미학을 즐기는 이들에게"),
        ("The Motorcycle Diaries", "2004", "🏍️🗺️🌄", "자유와 순간의 아름다움을 그린 여정"),
    ],
    "ESTP": [
        ("John Wick", "2014", "🔫⚡🖤", "직관적이고 액션 중심의 쾌감"),
        ("Baby Driver", "2017", "🚗🎧🏁", "아드레날린과 리듬감이 넘치는 영화"),
        ("Heat", "1995", "💣🏦🔥", "긴장감 넘치는 범죄 스릴러"),
    ],
    "ESFP": [
        ("Mamma Mia!", "2008", "🎤🌞💃", "파티같고 즉흥적인 뮤지컬 즐거움"),
        ("Pitch Perfect", "2012", "🎶😂👯", "현란하고 에너지 넘치는 음악코미디"),
        ("The Greatest Showman", "2017", "🎪✨🌟", "화려하고 감각적인 쇼무비"),
    ],
}

# -------------------- MBTI 선택 --------------------
st.subheader("당신의 MBTI를 골라주세요 🧭")
choice = st.selectbox("MBTI 선택", options=mbti_list, index=0)

st.write("---")
st.markdown(f"## 추천 영화 — {choice} 🎯")

# -------------------- 영화 표시 및 별점 --------------------
movies = MOVIE_DB.get(choice, [])

if movies:
    for title, year, tags, desc in movies:
        with st.expander(f"{title} ({year}) {tags}"):
            st.write(desc)
            rating = st.slider(f"⭐ {title} 별점 주기", 1, 5, 3)
            st.write(f"당신의 평가: {'⭐' * rating} ({rating}/5)")
else:
    st.info("아직 이 MBTI의 영화 데이터는 준비 중이에요! 🎥✨")

st.write("---")
st.caption("Made with ❤️ and lots of emojis — MBTI Movie Matcher")
