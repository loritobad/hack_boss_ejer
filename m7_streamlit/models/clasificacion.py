from asyncio import tasks
import streamlit as st


from pipeline.pipeline import pipeline

from utils.utils import color_green

import pandas as pd
import os

def clasificacion():
    st.title("Clasificacion")
    if "eda_data" in st.session_state:
        
        df = st.session_state["eda_data"]
        st.subheader(f"Muestra: {df.shape[0]} filas.", divider=True)
        model_ = pipeline(df, "clasificacion")
        
    
        model = model_["model"]
        txt = model_["txt"]
        
        if model:
            st.success(txt)
            
            output_dir = "csv"
            csv_file = os.path.join(output_dir, "historico_predicciones_cla.csv")
            
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
                    
                    max_price = float(df['price'].max())

                    price = st.number_input(
                        'Price', 
                        min_value=0.0,            # Aseguramos que sea float
                        max_value=max_price,           # Convertido a float
                        value=float(df['price'].min()),  # Convertido a float
                        step=1.0                  # Ya es float
                    )
                    
                    
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
                    
                    boton_clasificar = st.form_submit_button("Clasificar")
                    if boton_clasificar:
                        X_new_predict = pd.DataFrame({
                            'carat': [carat],
                            'depth': [depth],
                            'table': [table],
                            'price': [price],
                            'color': [selected_color],
                            'clarity': [selected_clarity],
                            'x': [x],
                            'y': [y],
                            'z': [z]                    
                        })
                        
                        

                       
                        prediccion = model.predict(X_new_predict)[0]
                        st.metric('CUT estimado', value=prediccion)
                        
                        X_new_predict['cut_estimado'] = prediccion
                        
                        
                        if os.path.exists(csv_file):
                            X_new_predict.to_csv(csv_file, mode='a', index=False, header=False)
                        else:
                            
                            X_new_predict.to_csv(csv_file, mode='w', index=False, header=True)
                
            with data_predict:
                
                if os.path.exists(csv_file):
                    st.subheader("Histórico de predicciones")
                    df_predictions = pd.read_csv(csv_file)
                    df_styled = df_predictions.style.applymap(color_green, subset=['cut_estimado'])
                    st.dataframe(df_styled)
            
        else:
            st.error("Error al entrenar el modelo.")