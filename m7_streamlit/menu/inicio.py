

import streamlit as st

from data.data import load_data

import plotly.express as px


def eda():
    
    if "eda_data" not in st.session_state:
        st.session_state["eda_data"] = load_data()
    
    
    if st.button("Recargar Datos", type="primary"):
        st.session_state["eda_data"] = load_data()
        st.success("Datos originales cargados.")
    
    
    df = st.session_state["eda_data"]
    
    st.subheader("Aplique filtros a los datos")
    
   
    top, medio = st.columns([1,2], border=True)
    
    with top:
        # Filtro para 'cut'
        cut_options = df['cut'].unique()
        selected_cut = st.multiselect("Seleccione el Corte", options=cut_options, default=list(cut_options))
        
        # Filtro para 'color'
        color_options = df['color'].unique()
        selected_color = st.multiselect("Seleccione el Color", options=color_options, default=list(color_options))
       
        # Filtro para 'clarity'
        clarity_options = df['clarity'].unique()
        selected_clarity = st.multiselect("Seleccione la Claridad (Clarity)", 
                                          options=clarity_options, 
                                          default=list(clarity_options))
        
        # Slider para 'carat'
        min_carat = df['carat'].min()
        max_carat = df['carat'].max()
        selected_carat = st.slider("Rango de Carat", 
                                   min_value=float(min_carat), 
                                   max_value=float(max_carat), 
                                   value=(float(min_carat), float(max_carat)))
        
        # Slider para 'price'
        min_price = df['price'].min()
        max_price = df['price'].max()
        selected_price = st.slider("Rango de Price", 
                                   min_value=float(min_price), 
                                   max_value=float(max_price), 
                                   value=(float(min_price), float(max_price)))
        
        # Aplicar los filtros sobre el DataFrame original
        df_filtered = df[
            (df['cut'].isin(selected_cut)) &
            (df['color'].isin(selected_color)) &
            (df['clarity'].isin(selected_clarity)) &
            (df['carat'] >= selected_carat[0]) &
            (df['carat'] <= selected_carat[1]) &
            (df['price'] >= selected_price[0]) &
            (df['price'] <= selected_price[1])
        ]
        
        # Agrupar datos para algunos gráficos
        df_count = df_filtered['cut'].value_counts().reset_index()
        df_count.columns = ['cut', 'count']
        
        df_count_clarity = df_filtered['clarity'].value_counts().reset_index()
        df_count_clarity.columns = ['clarity', 'count']
        
    with medio:
        st.dataframe(df_filtered, use_container_width=True)
    
    # Mostrar algunas métricas
    met1, met2, met3, met4 = st.columns([1,1,1,4])
    
    with met1:
        st.metric("Número de registros", df_filtered.shape[0])
    with met2:
        st.metric("Precio medio", round(df_filtered['price'].mean(), 2))
    with met3:
        st.metric("Profundidad media", round(df_filtered['depth'].mean(), 2))
    with met4:
        df_count_color = df_filtered['color'].value_counts().reset_index()
        df_count_color.columns = ['color', 'count']
        
        df_count_cut = df_filtered['cut'].value_counts().reset_index()
        df_count_cut.columns = ['cut', 'count']
        
        texto = " ".join([f"{row['color']} : {row['count']} |" for index, row in df_count_color.iterrows()])
        texto_cut = " ".join([f"{row['cut']} : {row['count']} |" for index, row in df_count_cut.iterrows()])
        
        st.markdown(f"<p style='font-size:18px;'><b>COLORES:</b> {texto}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:18px;'><b>CORTE:</b> {texto_cut}</p>", unsafe_allow_html=True)
    
   
    barplot, piechart, his = st.columns([2,2,2])
    
    with barplot:
        fig = px.bar(df_count, x='cut', y='count', 
                     title="Distribución de 'cut' en los datos filtrados",
                     labels={"cut": "Corte", "count": "Cantidad"})
        st.plotly_chart(fig, use_container_width=True)
        
    with piechart:
        fig2 = px.pie(df_count_clarity, names='clarity', values='count', 
                      title="Distribución de 'clarity' en los datos filtrados")
        st.plotly_chart(fig2, use_container_width=True)
        
    with his:
        fig3 = px.histogram(df_filtered, x='price', title="Histograma de 'price' en los datos filtrados")
        st.plotly_chart(fig3, use_container_width=True)
    
    
    st.session_state["eda_data"] = df_filtered
    
