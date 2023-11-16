# App to predict penguin species
# Using a pre-trained ML model in Streamlit

# Import libraries
import streamlit as st
import pickle

# Function to load the model and make predictions
def load_and_predict(input_data):
    # Load the pickled model
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Make predictions using the loaded model (replace this with your model's prediction logic)
    prediction = model.predict(input_data)
    return prediction

def user_form():
    st.title('User Form')

    # Text Input for Name
    name = st.text_input('Enter your name')

    # Slider for Age
    age = st.slider('Enter your age', 1, 100)

    # Dropdown for Gender
    gender = st.selectbox('Select your gender', ['Male', 'Female', 'Other'])

    # Button to submit the form
    if st.button('Submit'):
        # Create a dictionary of user input
        input_data = {
            'Name': name,
            'Age': age,
            'Gender': gender
        }

        # Call the function to load model and make predictions
        prediction = load_and_predict(input_data)

        # Display the prediction or perform any other action
        st.success(f"Prediction: {prediction}")

if __name__ == "__main__":
    user_form()
