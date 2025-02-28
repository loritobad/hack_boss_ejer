import os
import numpy as np
from sklearn.compose import make_column_transformer
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import streamlit as st
import joblib

def color_green(val):
    return 'background-color: lightgreen'

@st.cache_resource
def load_scikit_model(output_file):
    
    return joblib.load(output_file)

def train_pipeline(task, output_file, df):
    estado = ""
    #modelo ya entrenado
    if os.path.exists(output_file):
        model_ = load_scikit_model(output_file)
        
        estado = "Esta usando un modelo ya entrenado para hacer predicciones."
            
        return {"model": model_, "txt": estado}
    
    
    if task == "regresion":
        X = df.drop('price', axis=1)
        y = df['price']
        model_ = transform_pipeline(X, y, output_file, task)
        return {"model": model_, "txt": estado}
    
    if task == "clasificacion":
        X_c = df.drop('cut', axis=1)
        y_c = df['cut']
        model_ = transform_pipeline(X_c, y_c, output_file, task)
        return {"model": model_, "txt": estado}
    
    
   

def transform_pipeline(X, y, output_file, task):
    
    numerical_cols = X.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = X.select_dtypes(exclude=[np.number]).columns.tolist()
        
        
    numerical_pipeline = make_pipeline(
        SimpleImputer(strategy='median'),
        MinMaxScaler()
        )
            
    categorical_pipeline = make_pipeline(
        SimpleImputer(strategy='most_frequent'),
        OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        )
        
            
    column_transformer = make_column_transformer(
        (numerical_pipeline, numerical_cols),
        (categorical_pipeline, categorical_cols)
        )
    
    if task == "regresion":
             
        pipeline = make_pipeline(column_transformer, RandomForestRegressor(random_state=42))
        pipeline.fit(X, y)
    
    if task == "clasificacion":
        pipeline = make_pipeline(column_transformer, RandomForestClassifier(random_state=42))
        pipeline.fit(X, y)
    
    joblib.dump(pipeline, output_file)
    model_ = load_scikit_model(output_file)
    estado = "El modelo ha sido entrenado y guardado."
    return {"model": model_, "txt": estado}