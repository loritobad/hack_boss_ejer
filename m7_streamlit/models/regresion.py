
import os
import streamlit as st
from pipeline.pipeline import pipeline

from utils.utils import color_green

import pandas as pd



def regresion():
    st.title("Regresión")
    if "eda_data" in st.session_state:
        
        df = st.session_state["eda_data"]
        st.subheader(f"Muestra: {df.shape[0]} filas.", divider=True)
        model_ = pipeline(df, "regresion")
        
    
        model = model_["model"]
        txt = model_["txt"]
        
        if model:
            st.success(txt)
            
            output_dir = "csv"
            csv_file = os.path.join(output_dir, "historico_predicciones.csv")
            
            form_predict, data_predict = st.columns([1, 2])
            with form_predict:
                st.subheader("Generar predicción")
                
                with st.form("input_predict_price"):
                    carat = st.number_input(
                    'Carat', 
                    min_value=0.0, max_value=100.0, 
                    value=df['carat'].mean(), 
                    step=0.1
                    )
                    depth = st.number_input(
                    'Depth', 
                    min_value=0.0, max_value=100.0, 
                    value=df['depth'].mean(), 
                    step=0.1
                    )
                    table = st.number_input(
                    'Table', 
                    min_value=0.0, max_value=100.0, 
                    value=df['table'].mean(), 
                    step=0.1
                    )
                    
                    cut_options = df['cut'].unique()
                    selected_cut = st.selectbox("Seleccione el Corte", options=list(cut_options))
                    
                    color_options = df['color'].unique()
                    selected_color = st.selectbox("Seleccione el Color", options=list(color_options))
                    
                    clarity_options = df['clarity'].unique()
                    selected_clarity = st.selectbox("Seleccione Clarity", options=list(clarity_options))
            
                    
                    
                    
                    x = st.number_input(
                    'X', 
                    min_value=0.0, max_value=100.0, 
                    value=df['x'].mean(), 
                    step=0.1
                    )
                    y = st.number_input(
                    'Y', 
                    min_value=0.0, max_value=100.0, 
                    value=df['y'].mean(), 
                    step=0.1
                    )
                    
                    z = st.number_input(
                    'Z', 
                    min_value=0.0, max_value=100.0, 
                    value=df['z'].mean(), 
                    step=0.1
                    )
                    boton_enviar = st.form_submit_button("Generar predicción")
                    if boton_enviar:
                        X_new_predict = pd.DataFrame({
                            'carat': [carat],
                            'depth': [depth],
                            'table': [table],
                            'cut': [selected_cut],
                            'color': [selected_color],
                            'clarity': [selected_clarity],
                            'x': [x],
                            'y': [y],
                            'z': [z]                    
                        })
                        
                        

                       
                        prediccion = model.predict(X_new_predict)[0]
                        st.metric('Precio estimado', value=f'{prediccion:.2f} €')
                        prediccion = round(prediccion, 2)
                        X_new_predict['price_estimado'] = prediccion
                        
                        
                        if os.path.exists(csv_file):
                            X_new_predict.to_csv(csv_file, mode='a', index=False, header=False)
                        else:
                            
                            X_new_predict.to_csv(csv_file, mode='w', index=False, header=True)
                
            with data_predict:
                
                if os.path.exists(csv_file):
                    st.subheader("Histórico de predicciones")
                    df_predictions = pd.read_csv(csv_file)
                    df_styled = df_predictions.style.applymap(color_green, subset=['price_estimado'])
                    st.dataframe(df_styled)
            
        else:
            st.error("Error al entrenar el modelo.")

   
    