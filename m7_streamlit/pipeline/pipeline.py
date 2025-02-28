
import joblib
import numpy as np

from sklearn.compose import make_column_transformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.pipeline import  make_pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import streamlit as st

from utils.utils import  train_pipeline

import os

def pipeline(df, task):
    
     
    
    if task == "regresion":
        output_dir = "pipeline"
        output_file = os.path.join(output_dir, "pipe_regresion.joblib")
        
        model_ = train_pipeline("regresion", output_file, df)
        
        return model_
        
    elif task == "clasificacion":
        output_dir = "pipeline"
        output_file = os.path.join(output_dir, "pipe_clasificacion.joblib")
        
        model_ = train_pipeline("clasificacion", output_file, df)
    
        return model_
    
   
        
        


