# from langchain_openai import ChatOpenAI
# LANGCHAIN_API_KEY="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"
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os 
from dotenv import load_dotenv


load_dotenv()


os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_TRACING_V2"]="true"

# Prompt Template

prompt = ChatPromptTemplate.from_messages(
    {
        ("system","You are a helpfull assistant, please provide response to user queries"),
        ("user","Question:{question}")
    }
)

# Streamlit

st.title("Ollama Chatbot")
input_text = st.text_input("Search The Topic You Want")

llm=Ollama(model="llama2")
output_parser = StrOutputParser()

# Chain

chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))



