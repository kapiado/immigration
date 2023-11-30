# App to predict penguin species
# Using a pre-trained ML model in Streamlit

# Import libraries
import streamlit as st
import pandas as pd
import pickle
def displayPrediction(cluster, query, probs):
    st.title("Prediction Results")
    cluster = str(int(float(cluster)))
    st.write("")
    st.write("")
    st.subheader("Decision Tree Classification: Cluster " + cluster)

    probs_dict = {f"{i}": p for i, p in enumerate(probs.tolist())}

    keys = {
        "1": '0-9m', #0
        "2": '9m+'
    }

    sorted_keys = sorted(map(int, keys.keys()))
    ordered_dict = {str(key): keys[str(key)] for key in sorted_keys}

    # waiting time here
    df = pd.DataFrame.from_dict(keys, orient='index', columns=['WAITING_TIMERANGE'])
    df.index.name = 'Cluster'

    sorted_probs = sorted(map(int, probs_dict.keys()))
    ordered_probs = {str(key): probs_dict[str(key)] for key in sorted_probs}

    cluster_values = [ordered_probs[str(i)] for i in range(len(ordered_probs))]
    cluster_values = cluster_values[0]
    df['Probability'] = cluster_values

    df['Probability'] = df['Probability'].apply(lambda x: float(x) * 100)
    df['Probability'] = df['Probability'].apply(lambda x: format(x, '.2f') + '%')


    #st.dataframe(df)
    highlight_row(df, cluster)

    with st.expander("View Input"):
        smt = query
        headers = ['NAICS_CODE','PW_LEVEL','PW_AMOUNT','WORK_STATE','COUNTRY_OF_CITIZENSHIP','EMPLOYER_NUM_EMPLOYEES','CLASS_OF_ADMISSION',
            'JOB_EDUCATION','EXPERIENCE','EXPERIENCE_MONTHS','LAYOFF_IN_PAST_SIX_MONTHS','WORKER_EDUCATION']
        data = {}
        for i in range(len(headers)):
            data['Question'] = headers
            data['Answer'] = smt
            df = pd.DataFrame(data)
        with st.container():
            st.table(df.set_index('Question').T)

def process(query):
    df2 = pd.read_csv("11_30_23_Pred_Data_Final1.csv")
    df2 = df2.drop(columns = ['WAITING_TIMERANGE'])


    # Loading model and mapping pickle files
    dt_pickle = open('11_30_23_rf_model_final.sav', 'rb') 
    dt_model = pickle.load(dt_pickle) 
    dt_pickle.close() 

    df3 = df2.copy()
    df3.loc[len(df3)] = [codeInfo, wagelevelInfo, wageamountInfo, stateInfo, countryInfo, employeenumInfo,  admiclassInfo,  jobeducationInfo, expInfo, expmonthsInfo, layoffInfo, educationInfo]
    # Create dummies for encode_df
    cat_var = ['NAICS_CODE', 'PW_LEVEL','WORK_STATE','COUNTRY_OF_CITIZENSHIP','CLASS_OF_ADMISSION','JOB_EDUCATION','EXPERIENCE','LAYOFF_IN_PAST_SIX_MONTHS','WORKER_EDUCATION']
    df3 = pd.get_dummies(df3, columns = cat_var)
    # Extract encoded user data
    user_encoded_df = df3.tail(1)

    st.subheader("Predicting Waiting Time")

    new_prediction_dt = dt_model.predict(user_encoded_df)
    new_prediction_prob_dt = dt_model.predict_proba(user_encoded_df).max()
    # Show the predicted cost range on the app
    st.write("Random Forest Prediction: {}".format(*new_prediction_dt))
    st.write("Prediction Probability: {:.0%}".format(new_prediction_prob_dt))

    # Info = query
    # # df = pd.read_csv('CSV_files/dummieCodes.csv')
    # df = pd.read_csv('dummieCodex.csv')

    # # replace each row with its mode
    # df = modes('NAICS_CODE', df)
    # df = modes('WORKER_EDUCATION', df)
    # df = modes('PW_LEVEL', df)
    # df = modes('PW_AMOUNT', df)
    # df = modes('WORK_STATE', df)
    # df = modes('COUNTRY_OF_CITIZENSHIP', df)
    # df = modes('EMPLOYER_NUM_EMPLOYEES', df)
    # df = modes('CLASS_OF_ADMISSION', df)
    # df = modes('JOB_EDUCATION', df)
    # df = modes('EXPERIENCE', df)
    # df = modes('EXPERIENCE_MONTHS', df)
    # df = modes('LAYOFF_IN_PAST_SIX_MONTHS', df)


    # headers = ['NAICS_CODE','WORKER_EDUCATION','PW_LEVEL','PW_AMOUNT','WORK_STATE','COUNTRY_OF_CITIZENSHIP','EMPLOYER_NUM_EMPLOYEES','CLASS_OF_ADMISSION',
    #         'JOB_EDUCATION','EXPERIENCE','EXPERIENCE_MONTHS','LAYOFF_IN_PAST_SIX_MONTHS']

    # df_query = pd.DataFrame(columns=headers)
    # df_query.loc[0] = query

    # def more(column, df_query):
    #     new_col = column + '_replaced'
    #     df_query[new_col] = False

    #     df_query[new_col] = df_query.apply(lambda row: True if pd.isna(row[column]) else False, axis = 1)
    #     return df_query

    # df_query = more('NAICS_CODE', df_query)
    # df_query = more('WORKER_EDUCATION', df_query)
    # df_query = more('PW_LEVEL', df_query)
    # df_query = more('PW_AMOUNT', df_query)
    # df_query = more('WORK_STATE', df_query)
    # df_query = more('COUNTRY_OF_CITIZENSHIP', df_query)
    # df_query = more('EMPLOYER_NUM_EMPLOYEES', df_query)
    # df_query = more('CLASS_OF_ADMISSION', df_query)
    # df_query = more('JOB_EDUCATION', df_query)
    # df_query = more('EXPERIENCE', df_query)
    # df_query = more('EXPERIENCE_MONTHS', df_query)
    # df_query = more('LAYOFF_IN_PAST_SIX_MONTHS', df_query)

    # first_row = df_query.iloc[0].copy()
    # df.loc[0] = first_row
    # df_codex = df.reset_index(drop=True)

    # x = pd.get_dummies(df_codex.drop(columns = ['WAITING_TIMERANGE']), drop_first = True)
    # row = np.array(x.iloc[0]).reshape(1, -1)
    # zeros = np.zeros((1, 10), dtype=int)
    # row = np.concatenate((row, zeros), axis=1)

    # # loaded_model = joblib.load("pkl_files/dt_clustered_modes.sav")
    # loaded_model = joblib.load("NEWrf_model3_11_21_23.sav")

    # y_predicted = loaded_model.predict(row)
    # cluster = y_predicted[0]
    # probs = loaded_model.predict_proba(row)

    displayPrediction(cluster, query, probs)


def displayInput(Info):
        headers = ['NAICS_CODE','WORKER_EDUCATION','PW_LEVEL','PW_AMOUNT','WORK_STATE','COUNTRY_OF_CITIZENSHIP','EMPLOYER_NUM_EMPLOYEES','CLASS_OF_ADMISSION',
            'JOB_EDUCATION','EXPERIENCE','EXPERIENCE_MONTHS','LAYOFF_IN_PAST_SIX_MONTHS']
    #['NAICS Code','Prevailing Wage Level','Prevailing Wage Amount','Work State','Country of Citizenship','Employer Number of Employees','Class of Admission','Job Education','Experience','Months of Experience','Layoff in Past Six Months','Education']
        #query = [Info[0], Info[1], Info[6], Info[7], Info[3], Info[8], Info[9], Info[2], Info[5], Info[10], Info[4]]

        df_query = pd.DataFrame(columns=headers)
        df_query.loc[0] = Info
        df_transposed = df_query.transpose().reset_index()
        df_transposed.columns = df_transposed.iloc[0]
        df_transposed = df_transposed.iloc[1:]
        df_transposed = df_transposed.T

        # create a Streamlit table from the transposed dataframe
        st.table(df_transposed)
        #st.dataframe(df_transposed)

def interface():
    st.title("Estimate Your Green Card Application Wait Time")
    st.caption("This predictive dashboard predicts the waiting time from the date the application was received by the U.S. Department of Labor's Office of Foreign Labor Certification (OFLC) to the date a decision was made by OFLC for green card applicants.")
    # st.text("")
    # st.caption("*OFLC = Office of Foreign Labor Certification")
    if 'stage' not in st.session_state:
        st.session_state.stage = 0
        st.session_state.input = [] 
        st.session_state.ret = []

    def set_stage(stage, input):
        st.session_state.stage = stage
        st.session_state.input = input

        interface()
        #displayInput(input)

    # Some code
    with st.form(key='my_form'):
        codeOptions = ['11 - Agriculture, Forestry, Fishing and Hunting', 
                       '21 - Mining, Quarrying, and Oil and Gas Extraction', 
                       '22 - Utilities', 
                       '23 - Construction', 
                       '31 - Manufacturing (Food, Beverage, Tobacco, Apparel, Leather, Textiles)', 
                       '32 - Manufacturing (Paper, Printing, Petroleum, Coal, Chemicals, Plastics, Rubber, Nonmetallic)', 
                       '33 - Manufacturing (Primary Metals, Fabricated Metal, Machinery, Computer and Electronic Products, Electrical Equipment and Appliances, Transportations Equipment, Furniture, Miscellaneous Manufacturing)', 
                       '42 - Wholesale Trade',
                       '44 - Retail Trade (Automotive Sales and Services, Home Furnishing and Improvement, Food and Beverage, Health and Personal Care, Clothing and Accessories, Gasoline Stations)',
                       '45 - Retail Trade (Sporting Goods, Hobbies, Books, Department Stores, General Merchandise Stores, Florists, Office Supplies, Pet Supplies, Art Dealers, Various Specialty Stores)', 
                       '48 - Transportation and Warehousing (Air, Rail, Water, Truck, Transit, Pipeline, Scenic and Sightseeing Services, Transportation Support Activities)', 
                       '49 - Transportation and Warehousing (Federal Government-Operated Postal Services, Couriers, Messengers, Warehousing Storage-Related Services)',
                       '51 - Information',
                       '52 - Finance and Insurance',
                       '53 - Real Estate and Rental and Leasing',
                       '54 - Professional, Scientific, and Technical Services',
                       '55 - Management of Companies and Enterprises',
                       '56 - Administrative and Support and Waste Management and Remediation Services',
                       '61 - Educational Services',
                       '62 - Health Care and Social Assistance',
                       '71 - Arts, Entertainment, and Recreation',
                       '72 - Accommodation and Food Services',
                       '81 - Other Services (except Public Administration)',
                       '92 - Public Administration']
        
    
    # To get the selected value from the select box
        codeInfo = st.selectbox('NAICS Code', codeOptions, help="Select most appropriate Industry Code as found here https://www.census.gov/naics/?58967?yearbck=2022")
    
        # Initialize variables for NAICS Codes
    # Assign numerical values based on specific strings in the NAICS Code
        education_options = [
    "High School", "Associate's", "Bachelor's", "Doctorate", 
    "Master's", "None", "Other"
    ]
        # was job education -- how to address this since this is the education required by the job
        educationInfo = st.selectbox('Highest Completed Education Level', options=education_options) 
        
        wage_levels = ["Level I", "Level II", "Level III", "Level IV"]
        wagelevelInfo = st.selectbox('Prevailing Wage Level', wage_levels, help = "Select most appropriate prevailing wage level")
    
        wageamountInfo = st.number_input('Prevailing Wage Amount', min_value = 0)
        admiclasses = [
    "A-3", "A1/A2", "B-1", "B-2", "C-1", "C-3", "CW-1", "D-1", "D-2", 
    "E-1", "E-2", "E-3", "EWI", "F-1", "F-2", "G-1", "G-4", "G-5", 
    "H-1A", "H-1B", "H-1B1", "H-2A", "H-2B", "H-3", "H-4", "I", 
    "J-1", "J-2", "K-4", "L-1", "L-2", "M-1", "M-2", "N", "Not in USA", 
    "O-1", "O-2", "O-3", "P-1", "P-3", "P-4", "Parolee", "Q", 
    "R-1", "R-2", "T-1", "T-2", "TD", "TN", "TPS", "U-1", "V-2", 
    "VWB", "VWT"
    ]
    
        admiclassInfo = st.selectbox('Class of Admission', admiclasses)
        
        countryInfo = st.selectbox('Country of Citizenship', options=[
    "ARGENTINA", "AUSTRALIA", "BANGLADESH", "BELARUS", "BRAZIL", 
    "BULGARIA", "CANADA", "CHILE", "CHINA", "COLOMBIA", "ECUADOR", 
    "EGYPT", "FRANCE", "GERMANY", "GREECE", "HONG KONG", "INDIA", 
    "INDONESIA", "IRAN", "IRELAND", "ISRAEL", "ITALY", "JAPAN", 
    "JORDAN", "LEBANON", "MALAYSIA", "MEXICO", "NEPAL", "NETHERLANDS", 
    "NIGERIA", "PAKISTAN", "PERU", "PHILIPPINES", "POLAND", "ROMANIA", 
    "RUSSIA", "SINGAPORE", "SOUTH AFRICA", "SOUTH KOREA", "SPAIN", 
    "SRI LANKA", "SWEDEN", "SYRIA", "TAIWAN", "THAILAND", "TURKEY", 
    "UKRAINE", "UNITED KINGDOM", "VENEZUELA", "VIETNAM"
    ])
    
        stateInfo = st.selectbox('U.S. Work State',
                                                      [
        'ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'CONNECTICUT', 'DELAWARE',
        'DISTRICT OF COLUMBIA', 'FLORIDA', 'GEORGIA', 'GUAM', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA',
        'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARSHALL ISLANDS', 'MARYLAND', 'MASSACHUSETTS',
        'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA', 'NEW HAMPSHIRE',
        'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'NORTHERN MARIANA ISLANDS',
        'OHIO', 'OKLAHOMA', 'OREGON', 'PENNSYLVANIA', 'PUERTO RICO', 'RHODE ISLAND', 'SOUTH CAROLINA',
        'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGIN ISLANDS', 'VIRGINIA', 'WASHINGTON',
        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'
    ], 
                                 help = "Select the U.S. state of primary worksite")
    
        employeenumInfo = st.number_input('Number of Employees at Company', min_value = 0)
    
    
        jobeducation_options = [
    "High School", "Associate's", "Bachelor's", "Doctorate", 
    "Master's", "None", "Other"] 
        # was job education -- how to address this since this is the education required by the job
        jobeducationInfo = st.selectbox('Education Level Required by Job', options=jobeducation_options) 
    
        expInfo = st.radio('Do you have job/industry experience?', options=["Yes","No"])
        
        expmonthsInfo = st.number_input('Months of Experience', min_value = 0, help = "Input how many months of job experience you have")
        
        layoffInfo =  st.radio('Have you been affected from layoff(s) in the past six months?', options =["Yes","No"])
    
    
    
        submit = st.form_submit_button('Submit', args=(1,
                        [codeInfo, wagelevelInfo, wageamountInfo, stateInfo, countryInfo, employeenumInfo,  admiclassInfo,  jobeducationInfo, expInfo, expmonthsInfo, layoffInfo, educationInfo]))

    #if st.session_state.stage > 0 and st.session_state.input != ['15-17', '0 to 8', 'Full time', 'Male', 'AL', 'Homeless', 'Mexican', 'Native', 'Never married', 'Yes', 1]:

    if st.session_state.stage > 0:
        Info = st.session_state.input
        smt = [Info[0], Info[1], Info[2], Info[3], Info[4], Info[5], Info[6], Info[7], Info[8], Info[9], Info[10], Info[11]]
        headers =  ['NAICS Code','Education Level','Prevailing Wage Level','Prevailing Wage Amount','Class of Admission','Country of Citizenship','Work State','Education Required by Job','Employer Number of Employees','Experience','Months of Experience','Layoff in Past Six Months']
        data = {}
        for i in range(len(headers)):
            data['Question'] = headers
            data['Answer'] = smt
            df = pd.DataFrame(data)
            
        with st.container():
            st.table(df.set_index('Question').T)

    # def executeQuery(Info)
    def executeQuery():
        query = [Info[0], Info[1], Info[2], Info[3], Info[4], Info[5], Info[6], Info[7], Info[8], Info[9], Info[10], Info[11]]
        #st.text('Thank you!')
        process(query)

    if st.session_state.stage > 0:
        st.button('View Prediction', on_click=executeQuery, args=(st.session_state.input, ))
