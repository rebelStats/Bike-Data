#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 12:13:08 2022

@author: user
"""
import pandas as pd
#from sklearn.model_selection import train_test_split
bike = pd.read_csv('bike_streamlit.csv')
#if the dataset is too big we can also split it using train test split
#bike1,bike2 = train_test_split(bike,test_size=0.5)
variables= ["member_casual","weekend_weekday","ride_length_seconds","with_friend","time_of_day"]
X = bike[variables]

X = pd.get_dummies(X)
print(X)
Y = bike.Dist

from sklearn.ensemble import RandomForestRegressor
# In our model building the size was 180 trees, but this creates too large file size

#Github max file size is 100MB, max estimators we can use is 19
rf=RandomForestRegressor(max_depth=30, max_features='auto', min_samples_leaf=4,
                      n_estimators=19, n_jobs=-1)
rf.fit(X,Y)

import pickle
pickle.dump(rf,open('bike_rf.pkl','wb'))
