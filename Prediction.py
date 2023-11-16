# App to predict penguin species
# Using a pre-trained ML model in Streamlit

# Import libraries
import streamlit as st
import pickle


def user_form():
    st.title('User Form')

    name = st.text_input('Enter your name')
    age = st.slider('Enter your age', 1, 100)
    gender = st.selectbox('Select your gender', ['Male', 'Female', 'Other'])

    if st.button('Submit'):
        st.success(f"Name: {name}, Age: {age}, Gender: {gender}")

if __name__ == "__main__":
    user_form()
