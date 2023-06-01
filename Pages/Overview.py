# -*- coding: utf-8 -*-
"""
Created on Wed May 31 18:26:27 2023

@author: katri
"""
markdown = """
Web App URL: <https://kapiado-immigration-home-p9sni2.streamlit.app/>
GitHub Repository: <https://github.com/kapiado/immigration>
"""
st.sidebar.title("About")
st.sidebar.info(markdown)
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Background",
    page_icon="👋",
)
st.markdown("# Overview")
st.write("# Overview")
@st.cache_data
def cases():
    HtmlFile = open("CasesReceived.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height=600)
    
def avgwait():
    # Convert to datetime format for subtraction
# df["DECISION_DATE"] = pd.to_datetime(df["DECISION_DATE"])
# df["CASE_RECEIVED_DATE"] = pd.to_datetime(df["CASE_RECEIVED_DATE"])
# # Create new column for waiting time
# df["WAITING_TIME"] = df["DECISION_DATE"]-df["CASE_RECEIVED_DATE"]
# # Convert column to string and remove days and timestamp
# waitstr = df["WAITING_TIME"].astype(str).str.replace('days.+','')
# # Create a new column to get only days
# df["WAITING_TIME_DAYS"] = waitstr
# # Make column int
# df["WAITING_TIME_DAYS"] = df["WAITING_TIME_DAYS"].astype(int)
# average_waiting_time = df.groupby('CASE_RECEIVED_YEAR')['WAITING_TIME_DAYS'].mean()
# numcases= df["CASE_RECEIVED_YEAR"].value_counts().sort_index() # Number of cases per year
# fig = px.bar(x = numcases.index, y = average_waiting_time, title='Average Waiting Time from 2006-2021',height=500,color=average_waiting_time)
# fig.update_xaxes(title='Year',type='category')
# fig.update_yaxes(title='Average Waiting Time (days)',type='linear')
# st.plotly_chart(fig)
    HtmlFile = open("AvgWaitingTime.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height=600)
    
cases()
avgwait()
    
# st.sidebar.success("Select a page above.")

# st.markdown(
#     """
#     Streamlit is an open-source app framework built specifically for
#     Machine Learning and Data Science projects.
#     **👈 Select a demo from the sidebar** to see some examples
#     of what Streamlit can do!
#     ### Want to learn more?
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
# """
# )
