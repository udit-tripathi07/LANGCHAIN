 #  STATIC PROMPT

from langchain_ollama import ChatOllama
import streamlit as st

model=ChatOllama(model="llama3.1:latest")
st.header('Research Tool')

user_input=st.text_input('Enter your prompt')

if st.button('Summarize'):
    result=model.invoke(user_input)
    st.write(result.content)
    