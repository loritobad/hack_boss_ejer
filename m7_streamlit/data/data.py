import streamlit as st
import os
import pandas as pd


def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv"
    local_folder = "data"
    local_path = os.path.join(local_folder, "diamonds.csv")
    
    if os.path.exists(local_path):
        df = pd.read_csv(local_path)
        #st.info(f"El archivo ya existe y se cargó desde: {local_path}")
    else:
       
        df = pd.read_csv(url)
        df.to_csv(local_path, index=False)
        #st.success(f"Archivo descargado y guardado en: {local_path}")
    
    return df