import streamlit as st
from models.clasificacion import clasificacion
from models.regresion import regresion

from menu.inicio import eda

def layout():
    
    with st.sidebar:
        sidebar_logo = "images/img.jpg"
        st.sidebar.image(sidebar_logo, use_container_width=True)
    
        st.title("Seleccione una tarea")
        menu = st.sidebar.selectbox(
            "Seleccione una opción:", 
            options=["EDA","Regresion", "Clasificación"]
        )
        
    
    if menu == "Regresion":
        regresion()
    elif menu == "Clasificación":
        clasificacion()
    elif menu == "EDA":
        eda()
        
    