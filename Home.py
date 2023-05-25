# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:46:34 2023

@author: katri
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px          # Plotly
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.write("# Analysis of Factors Affecting U.S. Permanent Residency Using Data and Predictive Analytics")
image = Image.open('green card.jfif')

st.image(image,caption='Figure 1: Green Card Resident Image (Amazon)')




df = pd.read_csv("PERM_Data_5_22_23.csv")

# Cases received vs. Years
def cases(dataframe):
    #uniqueyears = df["CASE_RECEIVED_YEAR"].unique() # Obtain years for x-axis
    #years = list(uniqueyears) # Put into list
    numcases= df["CASE_RECEIVED_YEAR"].value_counts().sort_index() # Number of cases per year
    fig = px.bar(x = numcases.index, y = numcases, title='Cases Received from 2006-2021',height=500,color=numcases)
    fig.update_xaxes(title='Year',type='category')
    fig.update_yaxes(title='Total Received',type='linear')
    st.plotly_chart(fig)
    
def avgwait(dataframe):
    # Convert to datetime format for subtraction
    df["DECISION_DATE"] = pd.to_datetime(df["DECISION_DATE"])
    df["CASE_RECEIVED_DATE"] = pd.to_datetime(df["CASE_RECEIVED_DATE"])
    # Create new column for waiting time
    df["WAITING_TIME"] = df["DECISION_DATE"]-df["CASE_RECEIVED_DATE"]
    # Convert column to string and remove days and timestamp
    waitstr = df["WAITING_TIME"].astype(str).str.replace('days.+','')
    # Create a new column to get only days
    df["WAITING_TIME_DAYS"] = waitstr
    # Make column int
    df["WAITING_TIME_DAYS"] = df["WAITING_TIME_DAYS"].astype(int)
    average_waiting_time = df.groupby('CASE_RECEIVED_YEAR')['WAITING_TIME_DAYS'].mean()
    numcases= df["CASE_RECEIVED_YEAR"].value_counts().sort_index() # Number of cases per year
    fig = px.bar(x = numcases.index, y = average_waiting_time, title='Average Waiting Time from 2006-2021',height=500,color=average_waiting_time)
    fig.update_xaxes(title='Year',type='category')
    fig.update_yaxes(title='Average Waiting Time (days)',type='linear')
    st.plotly_chart(fig)
    
st.header('Background')
cases(df)
avgwait(df)
c = st.empty()
c.write('The immigration backlog is a result of the accumulation of immigration applications that have not been processed within a reasonable timeframe. \nIt is caused by increased demand, insufficient resources, complex procedures, and policy changes. Backlogs lead to delays in family reunification, economic impact, strain on resources, and uncertainty for individuals. In this dashboard, we aim to achieve transparency for individuals that are in the middle of the process and want to begin the process for residency. We will be  looking at historical data and factors that influence the wait times in this process, and provide an interface where users can predict their personal waiting time based on their demographics.')

#new line and research objectives content
st.write("")
st.header('Research Objectives')
st.subheader('Descriptive')
st.subheader('Prescriptive')

#new line and team intro
st.write("")
st.header('The Team')
st.write('**Team Members:** Katrina Apiado, Mahek Karachandani, Nika Mahdavi, & Boaz Nakhimovsky')
st.write('**Advisor:** Dr. German Serna & Dr. Liz Thompson')
st.write('**Sponsor:** Dr. Puneet Agarwal')


st.write("")
d = st.empty()
st.header('Reference List')
st.write("")
e = st.empty()
e.write('Galetti, Beth. “Amazon Urges Green Card Allocation to Help Immigrant Employees.” Amazon, Aug. 2022, www.aboutamazon.com/news/policy-news-views/amazon-urges-green-card-allocation-to-help-immigrant-employees.')
