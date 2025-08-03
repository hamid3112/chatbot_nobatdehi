#!/usr/bin/env python
# coding: utf-8

# In[15]:


import json
import random
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import streamlit as st
try:
    path = r"C:\Users\SEYED\Desktop\AI\project\بات نوبت دهی\output.json"
    with open (path , "r" , encoding="utf-8") as f:
        data_set = json.load(f)
    vectorizer = joblib.load(r"C:\Users\SEYED\tfidf_vectorizer_pkl")
    model = joblib.load(r"C:\Users\SEYED\chatbot_model.pkl")
except FileNotFoundError:
    st.error("فایل داده یا مدل ها پیدا نشدند.")
    st.stop()
#نیت
def predict_intent(text):
    text_vectorized = vectorizer.transform([text])
    intent = model.predict(text_vectorized)[0]
    probabilities = model.predict_proba(text_vectorized)
    confidence = max(probabilities[0])
    return intent , confidence
#جواب
def get_respons(intent):
    for intent_obj in data_set["intents"]:
        if intent_obj["tag"]==intent:
            responses = intent_obj["respons"]
            return random.choice(responses)
    return "متاسفانه در حال حاضر نمیتونم پاسخ بدم"
        
#گفتگو
st.title("چت نوبت دهی🤖")
st.markdown(""" سلام من یه دستیارهوشمند برای نوبت دهی هستم 😊. چه جوری مینونم کمکت کنم؟ میتونی ازم درباره
نوبت گیری، تغییر نوبت، کنسلی وقت، آدرس ، زمان های حضور دکتر بپرسی""")    
#حافظه گفتگو
if "messages" not in st.session_state:
    st.session_state.messages =[]
#نمایش پیام های قبلی
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
#گرفتن پیام از کاربر و چاپ
if prompt:=st.chat_input("اینجا بنویسید :"):
    st.session_state.messages.append({"role":"user" , "content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # پیشینی پرامپت
    intent , confidence = predict_intent(prompt)
    if confidence<0.5:
        intent="Defult"
    response = get_respons(intent)
    #چاپ جواب
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role":"assistant" , "content":response})

