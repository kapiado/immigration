# App to predict penguin species
# Using a pre-trained ML model in Streamlit

# Import libraries
import streamlit as st
import pickle
import streamlit.ReportThread as ReportThread
from streamlit.server.Server import Server
from session_state import get_state

class SessionState(object):
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

def get_state(hash_funcs=None):
    """Gets the SessionState for the current session or creates new."""
    ctx = ReportThread.get_report_ctx()

    this_session = None
    current_server = Server.get_current()
    if hasattr(current_server, '_session_infos'):
        session_infos = Server.get_current()._session_infos.values()
        for session_info in session_infos:
            s = session_info.session
            if s.id == ctx.session_id:
                this_session = s
    if this_session is None:
        raise RuntimeError("Couldn't get your Streamlit Session object.")
    if not hasattr(this_session, '_custom_session_state'):
        this_session._custom_session_state = SessionState(**(hash_funcs or {}))
    return this_session._custom_session_state

# Function to load the model and make predictions
def load_and_predict(input_data):
    # Load the pickled model
    with open('rf_model.sav', 'rb') as file:
        model = pickle.load(file)

    # Make predictions using the loaded model (replace this with your model's prediction logic)
    prediction = model.predict(input_data)
    return prediction
    prediction = 42
    return prediction

def user_form():
    st.title('User Form')

    # Get session state
    state = get_state()

    # Text Input for Name
    name = st.text_input('Enter your name', key="name")
    state.name = name

    # Slider for Age
    age = st.slider('Enter your age', 1, 100, key="age")
    state.age = age

    # Dropdown for Gender
    gender = st.selectbox('Select your gender', ['Male', 'Female', 'Other'], key="gender")
    state.gender = gender

    # Button to submit the form
    if st.button('Submit'):
        # Create a dictionary of user input
        input_data = {
            'Name': state.name,
            'Age': state.age,
            'Gender': state.gender
        }

        # Call the function to load model and make predictions
        prediction = load_and_predict(input_data)

        # Display the prediction or perform any other action
        st.success(f"Prediction: {prediction}")

if __name__ == "__main__":
    user_form()
