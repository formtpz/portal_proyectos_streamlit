import streamlit as st

st.set_page_config(page_title="Portal de Proyectos", page_icon="🌐", layout="centered")

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
