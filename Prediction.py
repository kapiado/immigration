# App to predict penguin species
# Using a pre-trained ML model in Streamlit

# Import libraries
import streamlit as st
import pickle

def user_form():
    st.title('User Form')

    if 'name' not in st.session_state:
        st.session_state.name = st.text_input('Enter your name')

    if 'age' not in st.session_state:
        st.session_state.age = st.slider('Enter your age', 1, 100)

    if 'gender' not in st.session_state:
        st.session_state.gender = st.selectbox('Select your gender', ['Male', 'Female', 'Other'])

    submit_button = st.button('Submit')

    if submit_button:
        name = st.session_state.name
        age = st.session_state.age
        gender = st.session_state.gender

        st.success(f"Name: {name}, Age: {age}, Gender: {gender}")

    if __name__ == "__main__":
        user_form()
