import streamlit as st

# ------------------------ 설정 ------------------------
st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="🧠", layout="centered")
st.title("🐾 MBTI로 알아보는 나랑 어울리는 포켓몬!")

st.markdown("당신의 MBTI를 선택하면, 성격에 꼭 맞는 포켓몬 친구를 소개해드릴게요! ✨")

# ------------------------ 데이터 ------------------------
pokemon_dict = {
    "INTJ": {
        "name": "뮤츠",
        "desc": "INTJ는 전략가형으로, 혼자 깊이 사고하며 큰 그림을 그리는 타입입니다. 강력한 능력을 가진 '뮤츠'는 당신처럼 신중하고 똑똑한 포켓몬이에요.",
        "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/150.png"
    },
    "INFP": {
        "name": "이브이",
        "desc": "INFP는 순수하고 가능성이 무한한 성격이에요. 다양한 진화 가능성을 가진 '이브이'는 당신의 따뜻하고 창의적인 면을 닮았답니다.",
        "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png"
    },
    "ENTP": {
        "name": "피카츄",
        "desc": "ENTP는 활발하고 재치 있는 타입! '피카츄'처럼 에너지 넘치고 모두와 잘 어울리는 매력으로 주변을 밝게 만듭니다 ⚡️",
        "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png"
    },
    "ISFJ": {
        "name": "라프라스",
        "desc": "ISFJ는 보호자형으로, 조용하고 따뜻한 마음을 가졌어요. 사람을 태워주는 친절한 '라프라스'는 헌신적인 당신을 닮았어요.",
        "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/131.png"
    },
    "ESTP": {
        "name": "리자몽",
        "desc": "ESTP는 도전적이고 에너지 넘치는 타입! '리자몽'처럼 모험심이 강하고 언제든 행동에 나서는 성격이에요.🔥",
        "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/006.png"
    },
    "INFJ": {
        "name": "루기아",
        "desc": "INFJ는 통찰력 있고 조용한 이상주의자예요. 전설 속 깊은 바다에 사는 루기아는 고요하지만 강한 당신의 내면을 닮았답니다.",
        "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/249.png"
    },
    "ENFP": {
        "name": "토게피",
        "desc": "ENFP는 자유로운 영혼이에요. 항상 즐겁고 귀여운 토게피처럼, 당신은 사람들에게 행복을 전하는 존재입니다 🎉",
        "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/175.png"
    },
    "ISTP": {
        "name": "갸라도스",
        "desc": "ISTP는 조용한 장인형이에요. 평소에는 조용해 보여도, 결정적인 순간엔 누구보다 강력한 갸라도스 같은 매력을 가졌습니다.",
        "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/130.png"
    }
    # 원하는 경우 나머지 MBTI도 추가 가능
}

# ------------------------ UI ------------------------
mbti_list = list(pokemon_dict.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요!", mbti_list)

if selected_mbti:
    pokemon = pokemon_dict[selected_mbti]
    st.subheader(f"🌟 추천 포켓몬: {pokemon['name']}")
    st.image(pokemon["img"], caption=pokemon["name"], use_column_width=True)
    st.markdown(f"🧬 **설명:** {pokemon['desc']}")
