# App to predict penguin species
# Using a pre-trained ML model in Streamlit

# Import libraries
import streamlit as st
import pickle

def user_form():
    st.title('User Form')

    if 'stage' not in st.session_state:
        st.session_state.stage = 'form'

    if st.session_state.stage == 'form':
        name = st.text_input('Enter your name')

        age = st.slider('Enter your age', 1, 100)

        gender = st.selectbox('Select your gender', ['Male', 'Female', 'Other'])

        if st.button('Submit'):
            st.session_state.user_data = {'Name': name, 'Age': age, 'Gender': gender}
            st.session_state.stage = 'result'

    elif st.session_state.stage == 'result':
        user_data = st.session_state.user_data
        st.write(f"Name: {user_data['Name']}, Age: {user_data['Age']}, Gender: {user_data['Gender']}")

    if __name__ == "__main__":
        user_form()
