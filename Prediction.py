# App to predict penguin species
# Using a pre-trained ML model in Streamlit

# Import libraries
import streamlit as st
import pandas as pd
import pickle

# def predictionmodel():
#     st.title('Penguin Classifier: A Machine Learning App') 
    
#     # Display the image
#     #st.image('penguins.png', width = 400)
    
#     st.write("This app uses 6 inputs to predict the species of penguin using " 
#              "a model built on the Palmer's Penguin's dataset. Use the form below" 
#              " to get started!") 
    
#     # Reading the pickle files that we created before 
#     dt_pickle = open('decision_tree_penguin.pickle', 'rb') 
#     map_pickle = open('output_penguin.pickle', 'rb') 
#     clf = pickle.load(dt_pickle) 
#     unique_penguin_mapping = pickle.load(map_pickle) 
#     dt_pickle.close() 
#     map_pickle.close() 
    
#     # Checking if these are the same Python objects that we used before
#     # st.write(clf)
#     # st.write(unique_penguin_mapping)
    
#     # Adding Streamlit functions to get user input
#     # For categorical variables, using selectbox
#     island = st.selectbox('Penguin Island', options = ['Biscoe', 'Dream', 'Torgerson']) 
#     sex = st.selectbox('Sex', options = ['Female', 'Male']) 
    
#     # For numerical variables, using number_input
#     # NOTE: Make sure that variable names are same as that of training dataset
#     bill_length_mm = st.number_input('Bill Length (mm)', min_value = 0) 
#     bill_depth_mm = st.number_input('Bill Depth (mm)', min_value = 0) 
#     flipper_length_mm = st.number_input('Flipper Length (mm)', min_value = 0) 
#     body_mass_g = st.number_input('Body Mass (g)', min_value = 0) 
    
#     # st.write('The user inputs are {}'.format([island, sex, bill_length, bill_depth, flipper_length, body_mass]))
    
#     # Putting sex and island variables into the correct format
#     # so that they can be used by the model for prediction
#     island_Biscoe, island_Dream, island_Torgerson = 0, 0, 0 
#     if island == 'Biscoe': 
#       island_Biscoe = 1 
#     elif island == 'Dream': 
#       island_Dream = 1 
#     elif island == 'Torgerson': 
#       island_Torgerson = 1 
    
#     sex_female, sex_male = 0, 0 
#     if sex == 'Female': 
#       sex_female = 1 
#     elif sex == 'Male': 
#       sex_male = 1 

def interface():
    st.title("Backend Interface")
    if 'stage' not in st.session_state:
        st.session_state.stage = 0
        st.session_state.input = []
        st.session_state.ret = []

    def set_stage(stage, input):
        st.session_state.stage = stage
        st.session_state.input= input

        interface()
        #displayInput(input)

    # Some code
    with st.form(key='my_form'):
        ageOptions = ['15-17', '18-20', '21-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65 up']
        ageInfo = st.selectbox('Age Group', ageOptions, help = "Select most appropriate age group")

        education_levels = ["0 to 8", "9 to 11", "12 or GED", "12+"]
        educInfo = st.selectbox("Highest Completed Education Level", education_levels, help = "Select the highest level of education you have completed")

        employment_statuses = ["Full time", "Part time", "Employed non differentiated", "Unemployed", "Not in labor force"]
        employInfo = st.selectbox("Employment Status", employment_statuses)

        genderInfo = st.radio("Sex", options=["Male", "Female"], help = "Sex assigned at birth")

        stateInfo = st.selectbox("State of Residence",
                                                      ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
                                                       "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                                                       "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                                                       "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                                                       "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"])


        housing_situations = ["Homeless", "Private residence", "Other"]
        livArangInfo = st.selectbox("Living Arrangement", housing_situations)

        ethnicities = ["Mexican", "Puerto Rican", "Other Hispanic or Latino origin", "Not of Hispanic or Latino origin"]
        ethnicityInfo = st.selectbox("Ethnicity", ethnicities)

        race_options = ['Native', 'Asian', 'Black or African American', 'Pacific Islander', 'White', 'Other/Multiple']
        raceInfo = st.selectbox('Race:', options=race_options)

        marital_status_options = ['Never married', 'Now married', 'Separated', 'Divorced', 'Widowed']
        marStatInfo = st.selectbox('Marital Status:', options=marital_status_options)

        sapInfo = st.radio("Substance Abuse History", options=["Yes", "No"], help = "Please select 'yes' if you have experienced issues with substance abuse")

        if sapInfo == "No":
            sapInfo = "Yes"

        #veteranInfo = st.radio("Veteran", options=["Yes", "No"])
        numhs =  st.selectbox("Number of Previously Diagnosed Mental Health Disorders", options = [0, 1, 2, 3], help = "Please enter the number of mental health disorders you have been clinically diagnosed with")

        if numhs == 0:
            numhs = 1

        veteranInfo = "No"

        submit = st.form_submit_button('Submit', on_click=set_stage, args=(1,
                    [ageInfo, educInfo, employInfo, genderInfo, stateInfo, livArangInfo, ethnicityInfo, raceInfo, marStatInfo, sapInfo, numhs]))

    #if st.session_state.stage > 0 and st.session_state.input != ['15-17', '0 to 8', 'Full time', 'Male', 'AL', 'Homeless', 'Mexican', 'Native', 'Never married', 'Yes', 1]:

    if st.session_state.stage > 0:
        Info = st.session_state.input
        smt = [Info[0], Info[1], Info[6], Info[7], Info[3], Info[8], Info[9], Info[2], Info[5], Info[10], Info[4]]
        headers = ['Age', 'Education', 'Ethnicity', 'Race', 'Sex', 'Marital Status', 'Substance Abuse Problem', 'Employment', 'Living Arrangement', 'Mental Health History', 'State']
        data = {}
        for i in range(len(headers)):
            data['Question'] = headers
            data['Answer'] = smt
            df = pd.DataFrame(data)
        with st.container():
            st.table(df.set_index('Question').T)

    def executeQuery(Info):
        query = [Info[0], Info[1], Info[6], Info[7], Info[3], Info[8], Info[9], Info[2], Info[5], Info[10], Info[4]]

        process(query)

    if st.session_state.stage > 0:
        st.button('View Prediction', on_click=executeQuery, args=(st.session_state.input, ))
    
    # Using predict() with new data provided by the user
    # new_prediction = clf.predict([[bill_length_mm, bill_depth_mm, flipper_length_mm, 
    #   body_mass_g, island_Biscoe, island_Dream, island_Torgerson, sex_female, sex_male]]) 
    
    # # Map prediction with penguin species
    # prediction_species = unique_penguin_mapping[new_prediction][0]
    
    # # Show the predicted species on the app
    # st.subheader("Predicting Your Penguin's Species")
    # st.write('We predict your penguin is of the {} species'.format(prediction_species)) 
    
    # # Showing additional items
    # # st.subheader("Prediction Performance")
    # # tab1, tab2, tab3, tab4 = st.tabs(["Decision Tree", "Feature Importance", "Confusion Matrix", "Classification Report"])
    
    # # with tab1:
    # #   st.image('dt_visual.svg')
    # # with tab2:
    # #   st.image('feature_imp.svg')
    # # with tab3:
    # #   st.image('confusion_mat.svg')
    # # with tab4:
    # #     df = pd.read_csv('class_report.csv', index_col=0)
    # #     st.dataframe(df)
