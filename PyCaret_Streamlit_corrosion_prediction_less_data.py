#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pycaret.regression import load_model, predict_model


# In[2]:


import streamlit as st


# In[3]:


import pandas as pd
import numpy as np


# In[4]:


model = load_model('corrosion_regressor_less_data')


# In[7]:


def predict_corrosion(model, df):
    predictions_data = predict_model(estimator = model, data = df)
    predictions=predictions_data['Label'][0]
    return predictions


# In[10]:


st.title('Corrosion Prediction Web App')
st.write('This is a web app to predict corrosion rates of oil wells based on         several features that you can see in the sidebar. Please adjust the         value of each feature. After that, click on the Predict button at the bottom to         see the prediction of the model.')


# In[11]:


BPPD = st.sidebar.slider(label = 'BPPD', min_value = 0,
                          max_value = 2000 ,
                          value = 500,step=1)


# In[12]:


BAPD = st.sidebar.slider(label = 'BAPD', min_value = 0,
                          max_value = 5000 ,
                          value = 1000,step=1)
                          
Caudal_gas = st.sidebar.slider(label = 'Caudal_gas_MSCFD', min_value = 0,
                          max_value = 1000 ,
                          value = 100,step=1)
   
Presion_cabeza = st.sidebar.slider(label = 'Presion_cabeza_psi', min_value = 0,
                          max_value = 500,
                          value = 150,step=1)

Temperatura_cabeza = st.sidebar.slider(label = 'Temperatura_cabeza_F', min_value = 0,
                          max_value = 300 ,
                          value = 150,step=1)

Salinidad = st.sidebar.slider(label = 'Salinidad_ppm', min_value = 0,
                          max_value = 100000 ,
                          value = 50000,step=100)

CO2_gas = st.sidebar.slider(label = 'CO2_gas %', min_value = 0,
                          max_value = 100 ,
                          value = 20,step=1)
                          
Bicarbonatos = st.sidebar.slider(label = 'bicarbonatos_ppm', min_value = 0,
                          max_value = 3000,
                          value = 500,step=1)

Dosis_IC = st.sidebar.slider(label = 'dosis_IC_ppm', min_value = 0,
                          max_value = 300,
                          value = 100,step=1)

Fe = st.sidebar.slider(label = 'Fe_ppm', min_value = 0,
                          max_value = 200,
                          value = 50,step=1)


# In[13]:


features = {'BPPD': BPPD, 'BAPD': BAPD,
            'Caudal_gas_MSCFD': Caudal_gas, 'Presion_cabeza_psi': Presion_cabeza,
            'Temperatura_cabeza_F': Temperatura_cabeza, 'Salinidad_ppm': Salinidad,
            'CO2_gas': CO2_gas, 'bicarbonatos_ppm': Bicarbonatos,
            'dosis_IC_ppm': Dosis_IC, 'Fe_ppm': Fe
           }
 

features_df  = pd.DataFrame([features])

st.table(features_df)  

if st.button('Predict'):
    prediction = predict_corrosion(model, features_df)
    if prediction < 1:
        st.write("Corrosion risk: Low")
    if prediction>=1 and prediction<5:
        st.write("Corrosion risk: Moderate")
    if prediction>=5 and prediction<10:
       st.write("Corrosion risk: High")
    if prediction >= 10:
        st.write("Corrosion risk: Severe")
    
    prediction='Based on your input variables, the corrosion rate is '+str('%f' % prediction) + ' mpy'
    st.write(prediction)

