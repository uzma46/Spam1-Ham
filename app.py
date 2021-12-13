import streamlit as st
import joblib
st.title('SPAM HAM CLASSIFICATION')         #title for webapp
text_model = joblib.load('spam-ham')        #load the model using joblib
ip = st.text_input('Enter your massage : ') #user input in streamlit
op = text_model.predict([ip])               #predict if the written message is spam or ham
if st.buttom('predict')                     #create a button called predict
  st.title(op[0])                           #if the button is pressed, then print the msg spam or ham