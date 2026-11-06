from html import escape
from urllib.parse import quote_plus

import streamlit as st


st.set_page_config(
    page_title="이름 | Personal page",
    page_icon="🌿",
    layout="wide",
)

PROFILE = {
    "name": "이름을 입력하세요",
    "role": "좋아하는 일을 꾸준히 탐구하는 사람",
    "intro": "새로운 곳을 걷고, 좋은 이야기를 모으며, 작은 아이디어를 직접 만들어 봅니다. 이 문장을 나를 잘 설명하는 소개로 바꿔보세요.",
    "affiliation": "학교 · 회사 · 팀 이름",
    "field": "전공 · 직무 · 관심 분야",
    "location": "서울, 대한민국",
    "email": "hello@example.com",
    "image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1400&q=85",
}

TRIPS = [
    {
        "place": "여행지 01",
        "region": "도시 · 나라",
        "year": "20XX",
        "note": "오래 기억하고 싶은 풍경이나 순간을 적어보세요.",
        "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=900&q=80",
    },
    {
        "place": "여행지 02",
        "region": "도시 · 나라",
        "year": "20XX",
        "note": "그곳에서 발견한 나만의 이야기를 적어보세요.",
        "image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=900&q=80",
    },
    {
        "place": "여행지 03",
        "region": "도시 · 나라",
        "year": "20XX",
        "note": "다시 가고 싶은 이유를 한 줄로 남겨보세요.",
        "image": "https://images.unsplash.com/photo-1518837695005-2083093ee35b?auto=format&fit=crop&w=900&q=80",
    },
]

HOBBIES = [
    ("사진 기록", "빛과 장면을 모아두기"),
    ("느린 산책", "익숙한 동네 새롭게 보기"),
    ("읽고 메모하기", "마음에 남은 문장 수집"),
    ("커피 내리기", "잠깐의 여유 즐기기"),
]

SONGS = [
    ("좋아하는 곡을 입력하세요", "아티스트 이름", "01"),
    ("오래 듣고 싶은 곡", "아티스트 이름", "02"),
    ("요즘 자주 듣는 곡", "아티스트 이름", "03"),
]

PROJECTS = [
    {
        "number": "01",
        "name": "프로젝트 이름",
        "kind": "개인 프로젝트 · 20XX",
        "description": "어떤 문제를 발견했고, 어떤 방식으로 풀었는지 간단히 소개해보세요.",
        "tags": ["기획", "디자인", "개발"],
        "url": "",
    },
    {
        "number": "02",
        "name": "함께 만든 프로젝트",
        "kind": "팀 프로젝트 · 20XX",
        "description": "내가 맡은 역할과 프로젝트를 통해 배운 점을 적어보세요.",
        "tags": ["협업", "리서치", "프로토타입"],
        "url": "",
    },
    {
        "number": "03",
        "name": "작은 실험",
        "kind": "사이드 프로젝트 · 20XX",
        "description": "관심사에서 출발한 작은 실험이나 진행 중인 작업을 소개해보세요.",
        "tags": ["아이디어", "기록", "실험"],
        "url": "",
    },
]

STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap');

:root {
    --paper: #f4f6ef;
    --paper-soft: #edf1e6;
    --white: #fbfcf8;
    --ink: #293a30;
    --muted: #6d7e70;
    --line: #d8e1d4;
    --forest: #385943;
    --fern: #54745b;
    --sage: #759276;
    --celadon: #91aa8d;
    --mint: #b2c9b0;
    --seafoam: #c8dcca;
    --pistachio: #dbe5c2;
    --limewash: #e7edcf;
    --moss: #aab987;
    --olive: #87976d;
    --dew: #e2ebe2;
    --stone: #a7b3a5;
}

html { scroll-behavior: smooth; }
.stApp {
    color: var(--ink);
    background-color: var(--paper);
    background-image: radial-gradient(rgba(84, 116, 91, 0.075) 0.7px, transparent 0.7px);
    background-size: 15px 15px;
    font-family: 'Noto Sans KR', sans-serif;
}
.stApp, .stApp p, .stApp span, .stApp div, .stApp a { letter-spacing: 0; }
.block-container { max-width: 1160px; padding: 1.4rem 2.2rem 3rem; }
header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }

.site-nav {
    min-height: 55px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid var(--line);
    margin-bottom: 1.8rem;
}
.nav-mark { color: var(--forest); font-size: 15px; font-weight: 700; }
.nav-links { display: flex; gap: 27px; }
.nav-links a, .nav-links a:visited {
    color: var(--muted);
    font-size: 12px;
    text-decoration: none;
}
.nav-links a:hover { color: var(--forest); }

.hero {
    display: grid;
    grid-template-columns: 1.04fr 0.96fr;
    align-items: center;
    gap: 54px;
    min-height: 480px;
    padding: 28px 0 58px;
}
.eyebrow {
    color: var(--fern);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px !important;
    text-transform: uppercase;
}
.hero h1 {
    margin: 20px 0 17px;
    color: var(--ink);
    font-family: 'DM Serif Display', 'Noto Sans KR', serif;
    font-size: 61px;
    font-weight: 400;
    line-height: 1.18;
}
.hero h1 span { color: var(--fern); }
.hero-role { color: var(--muted); font-size: 15px; font-weight: 500; }
.hero-copy {
    max-width: 470px;
    margin: 16px 0 25px;
    color: #647568;
    font-size: 13px;
    line-height: 1.95;
    word-break: keep-all;
}
.hero-actions { display: flex; flex-wrap: wrap; gap: 10px; }
.hero-actions a {
    display: inline-flex;
    min-height: 41px;
    align-items: center;
    padding: 0 17px;
    border: 1px solid var(--forest);
    border-radius: 4px;
    background: var(--forest);
    color: var(--white) !important;
    font-size: 12px;
    text-decoration: none;
}
.hero-actions a.secondary { background: transparent; color: var(--forest) !important; }
.hero-photo-wrap { position: relative; padding: 0 18px 18px 0; }
.hero-photo-wrap:after {
    position: absolute;
    z-index: 0;
    right: 0;
    bottom: 0;
    width: 78%;
    height: 74%;
    border-radius: 6px;
    background: var(--pistachio);
    content: '';
}
.hero-photo {
    position: relative;
    z-index: 1;
    display: block;
    width: 100%;
    height: 360px;
    border-radius: 5px;
    object-fit: cover;
}
.photo-label {
    position: absolute;
    z-index: 2;
    right: 30px;
    bottom: 31px;
    padding: 9px 12px;
    background: rgba(251, 252, 248, 0.94);
    color: var(--forest);
    font-size: 10px;
}

.section { padding: 66px 0; border-top: 1px solid var(--line); scroll-margin-top: 24px; }
.section-heading {
    display: flex;
    align-items: end;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 27px;
}
.section-index { color: var(--sage); font-size: 11px; font-weight: 700; }
.section-heading h2 {
    margin: 6px 0 0;
    color: var(--ink);
    font-family: 'DM Serif Display', 'Noto Sans KR', serif;
    font-size: 34px;
    font-weight: 400;
}
.section-note { color: var(--muted); font-size: 11px; }
.about-grid { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 55px; align-items: start; }
.about-copy {
    max-width: 650px;
    margin: 0;
    color: #4f6254;
    font-size: 16px;
    line-height: 2;
    word-break: keep-all;
}
.affiliation {
    padding: 22px 24px;
    border-left: 3px solid var(--celadon);
    background: rgba(251, 252, 248, 0.76);
}
.affiliation-label { margin-bottom: 9px; color: var(--sage); font-size: 10px; font-weight: 700; letter-spacing: 1px !important; }
.affiliation strong { display: block; color: var(--ink); font-size: 16px; }
.affiliation p { margin: 5px 0 0; color: var(--muted); font-size: 12px; }
.affiliation .location { margin-top: 17px; color: var(--fern); }

.travel-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 17px; }
.trip-card { overflow: hidden; border: 1px solid var(--line); border-radius: 5px; background: var(--white); }
.trip-card img { display: block; width: 100%; aspect-ratio: 1.48; object-fit: cover; }
.trip-body { padding: 17px 18px 19px; }
.trip-meta { display: flex; justify-content: space-between; color: var(--olive); font-size: 10px; }
.trip-body h3 { margin: 8px 0 5px; color: var(--ink); font-size: 17px; font-weight: 600; }
.trip-body p { min-height: 40px; margin: 0; color: var(--muted); font-size: 11px; line-height: 1.8; word-break: keep-all; }

.interest-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
.interest-item { min-height: 127px; padding: 18px 17px; border-top: 2px solid var(--sage); background: rgba(251, 252, 248, 0.78); }
.interest-item:nth-child(4n + 2) { border-color: var(--celadon); }
.interest-item:nth-child(4n + 3) { border-color: var(--moss); }
.interest-item:nth-child(4n) { border-color: var(--mint); }
.interest-number { color: var(--stone); font-size: 10px; }
.interest-item h3 { margin: 14px 0 5px; color: var(--forest); font-size: 14px; font-weight: 600; }
.interest-item p { margin: 0; color: var(--muted); font-size: 10px; }

.playlist { border-top: 1px solid var(--line); }
.song-row {
    display: grid;
    grid-template-columns: 54px 1fr auto;
    align-items: center;
    gap: 15px;
    min-height: 72px;
    border-bottom: 1px solid var(--line);
}
.song-number { color: var(--sage); font-family: 'DM Serif Display', serif; font-size: 21px; }
.song-title { color: var(--ink); font-size: 13px; font-weight: 600; }
.song-artist { margin-top: 3px; color: var(--muted); font-size: 10px; }
.song-link, .song-link:visited { color: var(--fern); font-size: 10px; text-decoration: none; }
.song-link:hover { color: var(--forest); text-decoration: underline; }

.project-list { border-top: 1px solid var(--line); }
.project-row {
    display: grid;
    grid-template-columns: 62px 1fr 170px;
    gap: 18px;
    align-items: start;
    padding: 22px 4px;
    border-bottom: 1px solid var(--line);
}
.project-number { color: var(--sage); font-family: 'DM Serif Display', serif; font-size: 25px; }
.project-kind { margin-bottom: 6px; color: var(--olive); font-size: 10px; }
.project-name { margin: 0; color: var(--ink); font-size: 16px; font-weight: 600; }
.project-description { max-width: 600px; margin: 7px 0 0; color: var(--muted); font-size: 11px; line-height: 1.8; word-break: keep-all; }
.project-tags { display: flex; flex-wrap: wrap; justify-content: end; gap: 5px; padding-top: 3px; }
.project-tags span { padding: 5px 8px; border-radius: 3px; background: var(--dew); color: var(--fern); font-size: 9px; }
.project-link { display: inline-block; margin-top: 8px; color: var(--fern); font-size: 10px; text-decoration: none; }

.contact-band {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    padding: 27px 30px;
    border-radius: 5px;
    background: var(--forest);
    color: var(--white);
}
.contact-band p { margin: 0 0 5px; color: var(--seafoam); font-size: 10px; }
.contact-band h2 { margin: 0; font-family: 'DM Serif Display', 'Noto Sans KR', serif; font-size: 25px; font-weight: 400; }
.contact-band a, .contact-band a:visited { color: var(--limewash); font-size: 12px; text-decoration: none; }
.site-footer { display: flex; justify-content: space-between; gap: 15px; padding-top: 24px; color: var(--muted); font-size: 10px; }

@media (max-width: 800px) {
    .block-container { padding: 1rem 1.3rem 2.5rem; }
    .hero { grid-template-columns: 1fr 0.82fr; gap: 28px; min-height: 410px; }
    .hero h1 { font-size: 48px; }
    .hero-photo { height: 300px; }
    .about-grid { gap: 28px; }
    .interest-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 580px) {
    .block-container { padding: 0.7rem 1rem 2rem; }
    .site-nav { align-items: flex-start; padding: 7px 0 13px; }
    .nav-links { max-width: 245px; flex-wrap: wrap; justify-content: end; gap: 8px 15px; }
    .hero { grid-template-columns: 1fr; gap: 24px; padding: 24px 0 38px; }
    .hero h1 { margin-top: 14px; font-size: 43px; }
    .hero-copy { margin-bottom: 18px; }
    .hero-photo { height: 245px; }
    .hero-photo-wrap { max-width: 460px; }
    .section { padding: 46px 0; }
    .section-heading { align-items: start; flex-direction: column; gap: 7px; margin-bottom: 20px; }
    .section-heading h2 { font-size: 29px; }
    .about-grid { grid-template-columns: 1fr; gap: 22px; }
    .about-copy { font-size: 14px; }
    .travel-grid { grid-template-columns: 1fr; }
    .trip-card { display: grid; grid-template-columns: 0.9fr 1.1fr; }
    .trip-card img { height: 100%; min-height: 160px; aspect-ratio: auto; }
    .trip-body { padding: 14px; }
    .trip-body p { min-height: 0; }
    .interest-grid { gap: 8px; }
    .interest-item { min-height: 116px; padding: 14px 12px; }
    .song-row { grid-template-columns: 38px 1fr auto; gap: 8px; }
    .project-row { grid-template-columns: 42px 1fr; gap: 10px; }
    .project-tags { grid-column: 2; justify-content: start; padding-top: 0; }
    .contact-band { align-items: flex-start; flex-direction: column; padding: 23px; }
    .site-footer { flex-direction: column; }
}
</style>
"""

st.markdown(STYLES, unsafe_allow_html=True)

travel_cards = "".join(
    f"""
    <article class="trip-card">
        <img src="{escape(trip['image'], quote=True)}" alt="{escape(trip['place'], quote=True)} 풍경" loading="lazy">
        <div class="trip-body">
            <div class="trip-meta"><span>{escape(trip['region'])}</span><span>{escape(trip['year'])}</span></div>
            <h3>{escape(trip['place'])}</h3>
            <p>{escape(trip['note'])}</p>
        </div>
    </article>
    """
    for trip in TRIPS
)

hobby_items = "".join(
    f"""
    <article class="interest-item">
        <span class="interest-number">0{index}</span>
        <h3>{escape(name)}</h3>
        <p>{escape(description)}</p>
    </article>
    """
    for index, (name, description) in enumerate(HOBBIES, start=1)
)

song_rows = "".join(
    f"""
    <div class="song-row">
        <span class="song-number">{escape(number)}</span>
        <div>
            <div class="song-title">{escape(title)}</div>
            <div class="song-artist">{escape(artist)}</div>
        </div>
        <a class="song-link" href="https://open.spotify.com/search/{quote_plus(f'{title} {artist}')}" target="_blank" rel="noreferrer">Spotify에서 찾기 ↗</a>
    </div>
    """
    for title, artist, number in SONGS
)

project_rows = "".join(
    f"""
    <article class="project-row">
        <div class="project-number">{escape(project['number'])}</div>
        <div>
            <div class="project-kind">{escape(project['kind'])}</div>
            <h3 class="project-name">{escape(project['name'])}</h3>
            <p class="project-description">{escape(project['description'])}</p>
            {f'<a class="project-link" href="{escape(project["url"], quote=True)}" target="_blank" rel="noreferrer">프로젝트 보기 ↗</a>' if project['url'] else ''}
        </div>
        <div class="project-tags">{''.join(f'<span>{escape(tag)}</span>' for tag in project['tags'])}</div>
    </article>
    """
    for project in PROJECTS
)

st.markdown(
    f"""
    <nav class="site-nav" aria-label="페이지 메뉴">
        <a class="nav-mark" href="#top">{escape(PROFILE['name'])} / NOTEBOOK</a>
        <div class="nav-links">
            <a href="#about">소개</a>
            <a href="#travel">여행</a>
            <a href="#interests">취미</a>
            <a href="#projects">프로젝트</a>
        </div>
    </nav>

    <main id="top">
        <section class="hero">
            <div>
                <div class="eyebrow">A LITTLE PAGE ABOUT ME</div>
                <h1>안녕하세요,<br><span>{escape(PROFILE['name'])}</span>입니다.</h1>
                <div class="hero-role">{escape(PROFILE['role'])}</div>
                <p class="hero-copy">{escape(PROFILE['intro'])}</p>
                <div class="hero-actions">
                    <a href="#projects">프로젝트 둘러보기</a>
                    <a class="secondary" href="mailto:{escape(PROFILE['email'], quote=True)}">연락하기</a>
                </div>
            </div>
            <div class="hero-photo-wrap">
                <img class="hero-photo" src="{escape(PROFILE['image'], quote=True)}" alt="나를 표현하는 풍경 사진">
                <span class="photo-label">A VIEW I LOVE</span>
            </div>
        </section>

        <section class="section" id="about">
            <div class="section-heading">
                <div><div class="section-index">01 / ABOUT</div><h2>나에 대하여</h2></div>
                <div class="section-note">지금의 나를 가장 잘 보여주는 이야기</div>
            </div>
            <div class="about-grid">
                <p class="about-copy">{escape(PROFILE['intro'])}</p>
                <aside class="affiliation">
                    <div class="affiliation-label">CURRENTLY</div>
                    <strong>{escape(PROFILE['affiliation'])}</strong>
                    <p>{escape(PROFILE['field'])}</p>
                    <p class="location">{escape(PROFILE['location'])}</p>
                </aside>
            </div>
        </section>

        <section class="section" id="travel">
            <div class="section-heading">
                <div><div class="section-index">02 / PLACES</div><h2>기억에 남은 여행</h2></div>
                <div class="section-note">다녀온 곳과 그곳에 남겨둔 순간</div>
            </div>
            <div class="travel-grid">{travel_cards}</div>
        </section>

        <section class="section" id="interests">
            <div class="section-heading">
                <div><div class="section-index">03 / OFF DUTY</div><h2>좋아하는 것들</h2></div>
                <div class="section-note">일상에 작은 리듬을 더해주는 취미</div>
            </div>
            <div class="interest-grid">{hobby_items}</div>
        </section>

        <section class="section" id="playlist">
            <div class="section-heading">
                <div><div class="section-index">04 / ON REPEAT</div><h2>요즘의 플레이리스트</h2></div>
                <div class="section-note">자주 꺼내 듣는 노래</div>
            </div>
            <div class="playlist">{song_rows}</div>
        </section>

        <section class="section" id="projects">
            <div class="section-heading">
                <div><div class="section-index">05 / SELECTED WORK</div><h2>만들어 온 것들</h2></div>
                <div class="section-note">생각을 결과물로 옮긴 프로젝트</div>
            </div>
            <div class="project-list">{project_rows}</div>
        </section>

        <section class="contact-band" id="contact">
            <div><p>LET'S SAY HELLO</p><h2>좋은 이야기는 언제든 환영이에요.</h2></div>
            <a href="mailto:{escape(PROFILE['email'], quote=True)}">{escape(PROFILE['email'])} ↗</a>
        </section>
        <footer class="site-footer">
            <span>{escape(PROFILE['name'])} · Personal notebook</span>
            <span>천천히 모으고, 나답게 기록하기</span>
        </footer>
    </main>
    """,
    unsafe_allow_html=True,
)