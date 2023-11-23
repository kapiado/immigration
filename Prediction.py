# App to predict penguin species
# Using a pre-trained ML model in Streamlit

# Import libraries
import streamlit as st
import pickle
def displayPrediction(cluster, query, probs):
    st.title("Prediction Results")
    cluster = str(int(float(cluster)))
    st.write("")
    st.write("")
    st.subheader("Decision Tree Classification: Cluster " + cluster)

    probs_dict = {f"{i}": p for i, p in enumerate(probs.tolist())}

    keys = {
        "0": 'ADHD, Anxiety, Conduct Disorder, Delirium, Substance Abuse, Dementia, Oppositional Defiant Disorder, Other, Personality Disorder, Pervasive Developmental Disorder, Trauma-Related',
        "1": 'Bipolar, Depression',
        "2": 'Schizophrenia/psychotic'
    }

    sorted_keys = sorted(map(int, keys.keys()))
    ordered_dict = {str(key): keys[str(key)] for key in sorted_keys}

    df = pd.DataFrame.from_dict(keys, orient='index', columns=['Disorders'])
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
    Info = query
    df = pd.read_csv('CSV_files/dummieCodex.csv')

    # replace each row with its mode
    df = modes('AGE', df)
    df = modes('EDUC', df)
    df = modes('ETHNIC', df)
    df = modes('RACE', df)
    df = modes('GENDER', df)
    df = modes('MARSTAT', df)
    df = modes('SAP', df)
    df = modes('EMPLOY', df)
    df = modes('LIVARAG', df)
    df = modes('NUMMHS', df)
    df = modes('STATEFIP', df)

    headers = ['NAICS_CODE','PW_LEVEL','PW_AMOUNT','WORK_STATE','COUNTRY_OF_CITIZENSHIP','EMPLOYER_NUM_EMPLOYEES','CLASS_OF_ADMISSION',
            'JOB_EDUCATION','EXPERIENCE','EXPERIENCE_MONTHS','LAYOFF_IN_PAST_SIX_MONTHS','WORKER_EDUCATION']

    df_query = pd.DataFrame(columns=headers)
    df_query.loc[0] = query

    def more(column, df_query):
        new_col = column + '_replaced'
        df_query[new_col] = False

        df_query[new_col] = df_query.apply(lambda row: True if pd.isna(row[column]) else False, axis = 1)
        return df_query

    df_query = more('AGE', df_query)
    df_query = more('EDUC', df_query)
    df_query = more('ETHNIC', df_query)
    df_query = more('RACE', df_query)
    df_query = more('GENDER', df_query)
    df_query = more('MARSTAT', df_query)
    df_query = more('SAP', df_query)
    df_query = more('EMPLOY', df_query)
    df_query = more('LIVARAG', df_query)
    df_query = more('NUMMHS', df_query)
    df_query = more('STATEFIP', df_query)

    first_row = df_query.iloc[0].copy()
    df.loc[0] = first_row
    df_codex = df.reset_index(drop=True)

    x = pd.get_dummies(df_codex.drop(columns = ['MH1']), drop_first = True)
    row = np.array(x.iloc[0]).reshape(1, -1)
    zeros = np.zeros((1, 10), dtype=int)
    row = np.concatenate((row, zeros), axis=1)

    loaded_model = joblib.load("pkl_files/dt_clustered_modes.sav")

    y_predicted = loaded_model.predict(row)
    cluster = y_predicted[0]
    probs = loaded_model.predict_proba(row)

    displayPrediction(cluster, query, probs)


def displayInput(Info):
        headers = ['NAICS Code','Prevailing Wage Level','Prevailing Wage Amount','Work State','Country of Citizenship','Employer Number of Employees','Class of Admission','Job Education','Experience','Months of Experience','Layoff in Past Six Months','Education']
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
    st.text("This predictive dashboard predicts the waiting time from the date the application was received by OFLC to the date a decision was made by OFLC for green card applicants. \n*OFLC = Office of Foreign Labor Certification")
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
        codeInfo = st.selectbox('NAICS Code', codeOptions, help = "Select most appropriate Industry Code as found here https://www.census.gov/naics/?58967?yearbck=2022")

        wage_levels = ["1", "2", "3", "4"]
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
                                                      ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
                                                       "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                                                       "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                                                       "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                                                       "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"], 
                                 help = "Select the U.S. state of primary worksite")

        employeenumInfo = st.number_input('Employer Number of Employees', min_value = 0)



        education_options = [
    "High School", "Associate's", "Bachelor's", "Doctorate", 
    "Master's", "None", "Other"
]
        # was job education -- how to address this since this is the education required by the job
        educationInfo = st.selectbox('Highest Completed Education  Level', options=education_options) 
        
        expInfo = st.radio('Do you have job/industry experience?', options=["Yes","No"])
        
        expmonthsInfo = st.number_input('Months of Experience', min_value = 0, help = "Input how many months of job experience you have")
        if expInfo == "No":
            expmonthsInfo = 0

        #if sapInfo == "No":
            #sapInfo = "Yes"
        
        layoffInfo =  st.radio('Have you been affected from layoff(s) in the past six months?', options =["Yes","No"])

        if layoffInfo == "Yes":
            layoffInfo = "Y"
        else:
            layoffInfo = "N"


        submit = st.form_submit_button('Submit', on_click=set_stage, args=(1,
                    [codeInfo, wagelevelInfo, wageamountInfo, admiclassInfo, countryInfo, stateInfo, employeenumInfo,  educationInfo, expInfo, expmonthsInfo, layoffInfo]))

    #if st.session_state.stage > 0 and st.session_state.input != ['15-17', '0 to 8', 'Full time', 'Male', 'AL', 'Homeless', 'Mexican', 'Native', 'Never married', 'Yes', 1]:

    if st.session_state.stage > 0:
        Info = st.session_state.input
        smt = [Info[0], Info[1], Info[6], Info[7], Info[3], Info[8], Info[9], Info[2], Info[5], Info[10], Info[4]]
        headers =  ['NAICS Code','Prevailing Wage Level','Prevailing Wage Amount','Class of Admission','Country of Citizenship','Work State','Employer Number of Employees','Job Education','Experience','Months of Experience','Layoff in Past Six Months','Education']
        data = {}
        for i in range(len(headers)):
            data['Question'] = headers
            data['Answer'] = smt
            df = pd.DataFrame(data)
        with st.container():
            st.table(df.set_index('Question').T)

    # def executeQuery(Info)
    def executeQuery():
        #query = [Info[0], Info[1], Info[6], Info[7], Info[3], Info[8], Info[9], Info[2], Info[5], Info[10], Info[4]]
        st.text('Thank you!')
        #process(query)

    if st.session_state.stage > 0:
        st.button('View Prediction', on_click=executeQuery, args=(st.session_state.input, ))
