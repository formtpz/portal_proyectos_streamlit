"""Portal de acceso a los proyectos TPZ."""
import base64
import html
import mimetypes
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Portal de Proyectos | TPZ",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).resolve().parent
logo = next(
    (archivo for archivo in ROOT.iterdir()
     if archivo.is_file() and archivo.stem.lower() == "logo1"
     and archivo.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".svg"}),
    None,
)
if logo:
    mime = mimetypes.guess_type(logo.name)[0] or "image/png"
    logo_src = f"data:{mime};base64,{base64.b64encode(logo.read_bytes()).decode('ascii')}"
    logo_html = f'<img src="{html.escape(logo_src, quote=True)}" alt="Logotipo TPZ" />'
else:
    logo_html = '<span class="brand-fallback">TPZ</span>'

st.markdown(
    """
<style>
:root { color-scheme: light; }
html, body, [data-testid="stAppViewContainer"], .stApp {
    background: #ffffff !important;
    color: #263142 !important;
}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"], #MainMenu, footer {
    display: none !important;
}
header[data-testid="stHeader"] { height: 0 !important; min-height: 0 !important; }
[data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none !important; }
.block-container { padding: 0 !important; max-width: none !important; }
#MainMenu, footer { visibility: hidden; }
.portal { min-height: 100vh; position: relative; overflow: hidden; isolation: isolate; }
.portal::before {
    content: ""; position: fixed; inset: 0; z-index: -2;
    background: #ffffff;
}
.portal-header {
    position: sticky; top: 0; z-index: 10; height: 125px;
    display: flex; align-items: center; justify-content: center;
    background: rgba(255,255,255,.88); backdrop-filter: blur(16px);
    border-bottom: 1px solid #f1e9e9;
}
.portal-header img { max-width: min(560px, 85vw); max-height: 110px; width: auto; height: auto; object-fit: contain; }
.brand-fallback { font-size: 32px; font-weight: 800; letter-spacing: .14em; color: #b84d55; }
.portal-main { max-width: 980px; margin: 0 auto; padding: 28px 24px 60px; text-align: center; position: relative; z-index: 1; }
.eyebrow { display: inline-block; padding: 8px 15px; background: #fff2f3; border: 1px solid #ffe1e3; border-radius: 99px; color: #b85560; font-size: 12px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; }
.portal-main h1 { font-size: clamp(34px, 5vw, 56px); color: #263142 !important; margin: 8px 0 12px; letter-spacing: -.045em; font-weight: 750; }
.portal-main > .intro { display: block; box-sizing: border-box; width: min(590px, calc(100vw - 40px)); max-width: 100%; margin: 0 auto 28px !important; padding: 0; text-align: center !important; font-size: 17px; color: #78818e !important; line-height: 1.7; }
.project-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px; text-align: left; }
.project-card {
    background: rgba(255,255,255,.94); border: 1px solid #eee7e9;
    border-radius: 22px; padding: 32px; box-shadow: 0 16px 50px rgba(65,47,52,.055);
    transition: transform .3s ease, box-shadow .3s ease, border-color .3s ease;
}
.project-card:hover { transform: translateY(-5px); border-color: #f1c5ca; box-shadow: 0 24px 65px rgba(65,47,52,.10); }
.project-heading { display: flex; align-items: center; gap: 14px; margin-bottom: 12px; }
.project-icon { display: inline-flex; flex: 0 0 auto; align-items: center; justify-content: center; width: 48px; height: 48px; background: #fff3f3; border-radius: 14px; font-size: 17px; font-weight: 750; color: #b84e59; }
.project-heading h2 { margin: 0 !important; }
.project-card h2 { font-size: 25px; margin: 0 0 10px; color: #293444 !important; letter-spacing: -.025em; }
.project-card p { font-size: 15px; color: #7b8490 !important; line-height: 1.6; margin: 0 0 27px; min-height: 50px; }
.project-link { display: inline-flex; align-items: center; justify-content: center; width: 100%; box-sizing: border-box; padding: 13px 18px; border-radius: 12px; background: #b84e59; color: white !important; text-decoration: none !important; font-weight: 650; transition: background .2s, transform .2s; }
.project-link:hover { background: #a53e49; transform: translateY(-1px); }
.portal-note { margin-top: 36px; color: #9ba2ac; font-size: 13px; }
.particle { position: fixed; z-index: -1; border-radius: 50%; background: rgba(221,104,115,.20); pointer-events: none; animation: drift var(--duration) ease-in-out infinite alternate; }
@keyframes drift { from { transform: translate3d(0,0,0); opacity: .25; } to { transform: translate3d(var(--dx),var(--dy),0); opacity: .65; } }
@media(max-width: 680px) {
    .portal-header { height: 100px; }
    .portal-header img { max-height: 88px; max-width: 85vw; }
    .portal-main { padding: 22px 20px 45px; }
    .project-grid { grid-template-columns: 1fr; gap: 18px; }
    .project-card { padding: 26px; }
}
@media(prefers-reduced-motion: reduce) {
    .particle { animation: none; }
    .project-card, .project-link { transition: none; }
}
</style>
""",
    unsafe_allow_html=True,
)

particulas = []
for i in range(24):
    left = (i * 43 + 11) % 100
    top = (i * 37 + 17) % 100
    size = 4 + (i * 7) % 9
    duration = 8 + (i * 3) % 13
    dx = -25 + (i * 13) % 51
    dy = -32 + (i * 17) % 65
    particulas.append(
        f'<span class="particle" style="left:{left}%;top:{top}%;'
        f'width:{size}px;height:{size}px;--duration:{duration}s;'
        f'--dx:{dx}px;--dy:{dy}px"></span>'
    )

st.markdown(
    f"""
<div class="portal">
    {''.join(particulas)}
    <header class="portal-header">{logo_html}</header>
    <main class="portal-main">
        <h1>Bienvenido al portal de proyectos</h1>
        <p class="intro">Selecciona el proyecto al que deseas ingresar para continuar con tus reportes y herramientas de trabajo.</p>
        <section class="project-grid">
            <article class="project-card">
                <div class="project-heading"><span class="project-icon">PE</span><h2>Proyecto Perú</h2></div>
                <p>Accede al sistema de gestión, reportes y seguimiento del proyecto Perú.</p>
                <a class="project-link" href="https://tpzperu-6pbksbwa4qetjw2mkphmku.streamlit.app/" target="_self">Ingresar a Perú ↗</a>
            </article>
            <article class="project-card">
                <div class="project-heading"><span class="project-icon">IT</span><h2>Proyecto Italia</h2></div>
                <p>Accede al sistema de gestión, reportes y seguimiento del proyecto Italia.</p>
                <a class="project-link" href="https://proyecto-italia.streamlit.app/" target="_self">Ingresar a Italia ↗</a>
            </article>
        </section>
    </main>
</div>
""",
    unsafe_allow_html=True,
)
