#importing libraries
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

#loading data i
data = pd.read_csv("music.csv")
features = data[["age" , "gender"]]
target = data[["genre"]]

#here i have used a random forest model
model = RandomForestClassifier(n_estimators =4)
model1 = model.fit(features , target )

#designing webapp using streamlit 
st.title('Music Genre prediction assignment for APTCODER')
st.subheader('Input Data')
st.dataframe(data)
st.subheader('Check Predictions Here')
age = st.number_input('Enter Your Age ' )
gender = st.radio( "Enter Gender ", ('Male', 'Female'))
if gender == 'Male' :
	gen= 1 
else :
	gen = 0 

if st.button('CHECK'):
	inp = [[age , gen]]
	res = model1.predict(inp)
	prediction = res[0]   
	st.header('Suitable Music Genre is ')
	st.header(prediction)
else:
     st.write('check here')

