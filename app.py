#first pip install streamlit
import streamlit as st


st.title('AI Instagram Model')

st.subheader('What should we have her do?')

st.subheader('INPUT BOX: Enter an activity or description of a photo')

photo=st.text_input("Enter a description of a photo here:")

st.button("Take it for a spin")
st.write(photo) #for now



#if st.button("Make photo"):
#    label = model.predict(photo)
#    st.write(label)