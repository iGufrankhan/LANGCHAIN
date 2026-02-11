import os
import streamlit as st
import dotenv
dotenv.load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question: {input}")
    ]
)

st.title("Simple Question Answering App")

user_input = st.text_input("What is your question?")

llm = OllamaLLM(model="llama3.2:1b")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if user_input:
    response = chain.invoke({"input": user_input})
    st.write("Answer:", response)
