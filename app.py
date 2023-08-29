import os
from apikey import apikey
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY']= apikey

# App framework
st.title('Laminar-X Tax 🛃 Advisor')
prompt= st.text_input('Write your industry and current earning in this manner: Construction industry with a net income of $300000')

#Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'Give a detailed tax advice for a small and medium company in the {topic}'
)

# Llms
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

#Show stuff on prompt
if prompt:
    response= title_chain.run(topic=prompt)
    st.write(response)