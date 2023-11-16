# App to predict penguin species
# Using a pre-trained ML model in Streamlit

# Import libraries
import streamlit as st
import pickle

def user_form():
    st.title('User Form')

    name_placeholder = st.empty()
    age_placeholder = st.empty()
    gender_placeholder = st.empty()

    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    if not st.session_state.submitted:
        name = name_placeholder.text_input('Enter your name')
        age = age_placeholder.slider('Enter your age', 1, 100)
        gender = gender_placeholder.selectbox('Select your gender', ['Male', 'Female', 'Other'])

        if st.button('Submit'):
            st.session_state.name = name
            st.session_state.age = age
            st.session_state.gender = gender
            st.session_state.submitted = True

    if st.session_state.submitted:
        st.success(f"Name: {st.session_state.name}, Age: {st.session_state.age}, Gender: {st.session_state.gender}")

if __name__ == "__main__":
    user_form()
