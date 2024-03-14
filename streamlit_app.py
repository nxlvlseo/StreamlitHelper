import streamlit as st
import openai

openai.api_key = st.secrets["secrets"]["OPENAI_API_KEY"]

def get_gpt_response(prompt):
    response = openai.Completion.create(
      engine="Streamlit",
      prompt=prompt,
      temperature=0.7,
      max_tokens=150,
    )
    return response.choices[0].text.strip()

st.title('Custom GPT with Streamlit')
user_input = st.text_input("Ask something:", "")
if st.button('Submit'):
    response = get_gpt_response(user_input)
    st.text_area("GPT's response:", value=response, height=200)
