# App to predict penguin species
# Using a pre-trained ML model in Streamlit

# Import libraries
import streamlit as st
import pickle

def user_form():
    st.title('Streamlit User Form')

    def user():
        if 'stage' not in st.session_state:
            st.session_state.stage = 0

        if st.session_state.stage == 0:
            name = st.text_input('Enter your name')
            age = st.slider('Enter your age', 1, 100)
            gender = st.selectbox('Select your gender', ['Male', 'Female', 'Other'])

            if st.button('Submit'):
                input_data = {'Name': name, 'Age': age, 'Gender': gender}
                st.session_state.ret = "Thank you!"
                st.session_state.stage += 1

        elif st.session_state.stage > 0:
            st.write(st.session_state.ret)

    user()

if __name__ == "__main__":
    main()
