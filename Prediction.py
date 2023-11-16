# App to predict penguin species
# Using a pre-trained ML model in Streamlit

# Import libraries
import streamlit as st
import pickle

def user_form():
    st.title('User Form')

    if 'stage' not in st.session_state:
        st.session_state.stage = 'input'

    if st.session_state.stage == 'input':
        st.session_state.input = {
            'name': st.text_input('Enter your name'),
            'age': st.slider('Enter your age', 1, 100),
            'gender': st.selectbox('Select your gender', ['Male', 'Female', 'Other'])
        }

        if st.button('Submit'):
            st.session_state.stage = 'result'

    elif st.session_state.stage == 'result':
        input_data = st.session_state.input
        st.session_state.ret = f"Name: {input_data['name']}, Age: {input_data['age']}, Gender: {input_data['gender']}"
        st.success(st.session_state.ret)

if __name__ == "__main__":
    user_form()
