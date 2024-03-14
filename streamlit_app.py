import streamlit as st
import openai

openai.api_key = 'your_openai_api_key_here'

def get_gpt_response(prompt):
    response = openai.Completion.create(
      engine="your_custom_gpt_model_name",
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
