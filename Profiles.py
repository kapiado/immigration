# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:04:25 2023

@author: katri
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components

st.markdown("# Profiles")

@st.cache_data
def majorswait():
#     df["DECISION_DATE"] = pd.to_datetime(df["DECISION_DATE"])
#     df["CASE_RECEIVED_DATE"] = pd.to_datetime(df["CASE_RECEIVED_DATE"])
#     # Create new column for waiting time
#     df["WAITING_TIME"] = df["DECISION_DATE"]-df["CASE_RECEIVED_DATE"]
#     fig = px.bar(df, x="FOREIGN_WORKER_INFO_MAJOR", y="WAITING_TIME", height=1200,color_discrete_sequence=['red'], log_y=True,
#               labels = {"FOREIGN_WORKER_INFO_MAJOR":"Major ","WAITING_TIME":"Waiting time"})
#     fig.update_xaxes(title="Major of Applicants",categoryorder='total descending')
#     fig.update_yaxes(title="Waiting Time in Days (logarithmic scale)")

#     fig.update_layout(
#     xaxis=dict(title_font=dict(size=14)),
#     yaxis=dict(title_font=dict(size=14)),
#     title="Majors and Waiting Time",
#     )
#     st.plotly_chart(fig)
    HtmlFile = open("major_graph.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height=1300)
# def unitofpay(dataframe):
#     fig = go.Figure(data=go.Histogram(x=df['PW_UNIT_OF_PAY_9089']))

#     fig.update_layout(
#         title='Distribution Plot for Unit of Pay',
#         xaxis=dict(title='Unit of Pay'),
#         yaxis=dict(title='Frequency', type='log')
#         )
#     st.plotly_chart(fig)

def numemployeeswaitingtime():
    HtmlFile = open("number_of_employee_and_waiting_time_bar_graph.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height=600)

def unitofpay():
    HtmlFile = open("unit_of_pay_bar_graph.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height=600)

tab1, tab2 = st.tabs(["Employee Profile","Employer Profile"])

with tab1:
   st.header("Employee Profile")
   c = st.empty()
   c.write("The Employee Profile includes key information about the demographic of employees in our dataset, who undergo the immigration backlog process in the United States. This includes their education, salary, nationality, profession, major and layoff history. In the profile, we present visual representations of the data related to Immigration Backlog. We will explore the trend of immigration backlog overtime, in terms of applications received and waiting time for approval, for example. By examining these factors, we aim to gain insights into the patterns and changes within the immigration backlog, enabling a better understanding.")
   majorswait()
   numemployeeswaitingtime()
   unitofpay()
   #st.image("https://static.streamlit.io/examples/cat.jpg")

with tab2:
   st.header("Employer Profile")
   st.text("Insert Employer Profile details here")
   #st.image("https://static.streamlit.io/examples/dog.jpg")