import base64
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Portal de Proyectos", page_icon="🌐", layout="centered")

# Imagen de fondo almacenada en el mismo repositorio.
fondo = Path(__file__).resolve().parent / "Backdrop_TPZ.webp"
if fondo.is_file():
    imagen_base64 = base64.b64encode(fondo.read_bytes()).decode("ascii")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(10, 20, 35, 0.48), rgba(10, 20, 35, 0.62)),
                              url("data:image/webp;base64,{imagen_base64}");
            background-size: cover;
            background-position: center center;
            background-attachment: fixed;
        }}
        .stApp h1, .stApp h2, .stApp h3, .stApp p,
        .stApp [data-testid="stCaptionContainer"] {{
            color: #ffffff;
        }}
        div[data-testid="stVerticalBlockBorderWrapper"]:has(> div[data-testid="stVerticalBlock"]) {{
            backdrop-filter: blur(5px);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


st.title("Portal de Proyectos")
st.write("Selecciona el proyecto al que deseas ingresar.")
st.caption("Las credenciales se solicitan en el sistema correspondiente.")

proyectos = [
    ("🇵🇪", "Proyecto Perú", "Sistema de gestión y reportes de Perú", "https://tpzperu-6pbksbwa4qetjw2mkphmku.streamlit.app/"),
    ("🇮🇹", "Proyecto Italia", "Sistema de gestión y reportes de Italia", "https://proyecto-italia.streamlit.app/"),
]
for bandera, nombre, descripcion, url in proyectos:
    with st.container(border=True):
        st.subheader(f"{bandera} {nombre}")
        st.write(descripcion)
        st.link_button(f"Ingresar a {nombre}", url, use_container_width=True)
