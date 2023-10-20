# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:46:34 2023

@author: katri
"""

import streamlit as st
import streamlit.components.v1 as components
# import numpy as np
import pandas as pd
# import plotly.express as px          # Plotly
# import plotly.graph_objects as go
from PIL import Image
#from streamlit_extras.switch_page_button import switch_page
#st.set_page_config(
#    page_title="Home",
#    page_icon="👋",
#)
#st.sidebar.success("Select a page above.")
#st.sidebar.title("Home")
#switch_page("Overview")

def home():

    st.write("# Analysis of Factors Affecting U.S. Permanent Residency Using Data and Predictive Analytics")
    image = Image.open('green card.jfif')
    
    st.image(image,caption='Figure 1: Green Card Resident Image (Amazon)')
    
    def cases():
        HtmlFile = open("CasesReceived.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,height=600)
        
    def avgwait():
        HtmlFile = open("AvgWaitingTime.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,height=600)
        
    st.header('Background')
    p = open("CasesReceived.html")
    components.html(p.read(),height=600)
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
