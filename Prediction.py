# App to predict penguin species
# Using a pre-trained ML model in Streamlit

# Import libraries
import streamlit as st
import pickle

# Function to load the model and make predictions
def load_and_predict(input_data):
    # Load the pickled model
    with open('rf_model.sav', 'rb') as file:
        model = pickle.load(file)

    # Make predictions using the loaded model (replace this with your model's prediction logic)

    prediction = 42
    return prediction

def user_form():
    st.title('User Form')

    if 'name' not in st.session_state:
        st.session_state.name = st.text_input('Enter your name')

    if 'age' not in st.session_state:
        st.session_state.age = st.slider('Enter your age', 1, 100)

    if 'gender' not in st.session_state:
        st.session_state.gender = st.selectbox('Select your gender', ['Male', 'Female', 'Other'])

    if st.button('Submit'):
        input_data = {
            'Name': st.session_state.name,
            'Age': st.session_state.age,
            'Gender': st.session_state.gender
        }

        prediction = load_and_predict(input_data)

        st.success(f"Prediction: {prediction}")

if __name__ == "__main__":
    user_form()
