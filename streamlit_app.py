import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_gpt_response(user_input):
    try:
        response = openai.ChatCompletion.create(
          model="Streamlit",  # Adjust according to the available models
          messages=[{"role": "system", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        st.error(f"An error occurred while generating the script: {e}")
        return ""

st.title('Custom GPT with Streamlit')
user_input = st.text_input("Ask something:", "")
if st.button('Submit'):
    response = get_gpt_response(user_input)
    st.text_area("GPT's response:", value=response, height=200)
