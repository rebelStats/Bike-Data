#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 14:53:09 2022

@author: user
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
#text on website
st.write("""
# Bike Distance Prediction App

This app predicts the distance taken by a trip for a rented bike in NYC!

Data obtained from [Kaggle](https://www.kaggle.com/datasets/daesunryu/public-dataset-from-bikesharecompany). 
""")

st.sidebar.header('User Input Features')
#Collect User input features
def user_input_features():
    member = st.sidebar.selectbox('Member/Casual', ('member','casual'))
    weekend = st.sidebar.selectbox('Weekend/Weekday', ('Weekend','Weekday'))
    ride_length_seconds = st.sidebar.slider('Ride Length in Seconds', 60, 3000, 800)
    with_friend = st.sidebar.selectbox("With Friend", ("Yes","No"))
    time_of_day = st.sidebar.selectbox("Time of day", ("morning","afternoon","night"))
    
    data = {'member_casual':member,
            "weekend_weekday":weekend,
            'ride_length_seconds':ride_length_seconds,
            'with_friend': with_friend,
            'time_of_day':time_of_day,
            
        
        }
    features = pd.DataFrame(data,index =[0])
    return features
input_df = user_input_features()
#combine user input with data to create dummy variables from user input
bike = pd.read_csv('bike_streamlit.csv')
variables= ["member_casual","weekend_weekday","ride_length_seconds","with_friend","time_of_day"]
bike = bike[variables]
df = pd.concat([input_df,bike],axis = 0)

df = pd.get_dummies(df) 
df = df[:1] # select first row (user input row)

st.subheader('User Input features')
st.write(df)
#read regression model
load_rf = pickle.load(open('bike_rf.pkl','rb'))

#make predictions with model
prediciton = load_rf.predict(df)

st.subheader('Distance Prediction in KM')
st.write(prediciton)