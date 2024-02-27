from api import openai_api_key
import streamlit as st 
from langchain.llms import OpenAI
import os
os.environ["OPENAI_API_KEY"]=openai_api_key
def response(question):
    llm=OpenAI(temperature=0.7)
    resp=llm(question)
    return resp

st.set_page_config(page_title="QA DEMO")
st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
resp=response(input)

submit=st.button("Ask a Question")
if submit:
    st.subheader("The Response is ")
    st.write(resp)