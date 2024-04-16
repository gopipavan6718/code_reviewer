import os
import streamlit as st
from openai import OpenAI

f = open('apikey.txt')
key = f.read()
client = OpenAI(api_key=key)

def pythonCode_fix(prompt):
    gen = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'Given a Python code snippet, the system should analyze it for errors, provide a description of the error in ordered list with heading bug report, and generate corrected code with heading correct code.'},
            {'role': 'user', 'content': prompt}
        ]
    )
    return gen.choices[0].message.content

# Streamlit UI
st.title('🤖 AI Python Code Fixer')
prompt = st.text_area('Enter a Python Code Snippet:')
if st.button('Generate'):
    if prompt:
        with st.spinner('Generating...'):
            corrected_code = pythonCode_fix(prompt)
            st.code(corrected_code, language='python')
    else:
        st.warning('Please enter a Python code snippet.')