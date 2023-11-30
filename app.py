import streamlit as st
import requests

# Streamlit app
st.image("https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?q=80&w=1920&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", caption="Wine", use_column_width=True)
st.title('AI Instagram Influencer')

user_input = st.text_area("What should we have her do?")
if st.button('Create'):
    url=f'some_url_for_our_model{user_input}'
    response = requests.get(url)
    verdict = response.json()
