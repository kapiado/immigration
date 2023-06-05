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

def render():
        
    st.set_page_config(page_title="Employee Profile")
    st.markdown("# Employee Profile")
    
    path = "C:/Users/katri/multipage_app/HTML Files/"
    
    # def majorswait():
    #     HtmlFile = open("major_graph.html", 'r', encoding='utf-8')
    #     source_code = HtmlFile.read() 
    #     print(source_code)
    #     components.html(source_code,height=1300)
    
    # def numemployeeswaitingtime():
    #     HtmlFile = open("number_of_employee_and_waiting_time_bar_graph.html", 'r', encoding='utf-8')
    #     source_code = HtmlFile.read() 
    #     print(source_code)
    #     components.html(source_code,height=600)
    
    def unitofpay():
        HtmlFile = open(path+"unit_of_pay_bar_graph.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,height=600)
    
    c = st.empty()
    c.write("The Employee Profile includes key information about the demographic of employees in our dataset, who undergo the immigration backlog process in the United States. This includes their education, salary, nationality, profession, major and layoff history. In the profile, we present visual representations of the data related to Immigration Backlog. We will explore the trend of immigration backlog overtime, in terms of applications received and waiting time for approval, for example. By examining these factors, we aim to gain insights into the patterns and changes within the immigration backlog, enabling a better understanding.")
    
    tab1, tab2 = st.tabs(["NAICS Code","Employer Profile"])
    
    with tab1:
       st.header("Employee Profile")
       unitofpay()
       #st.image("https://static.streamlit.io/examples/cat.jpg")
    
    with tab2:
       st.header("Employer Profile")
       st.text("Insert Employer Profile details here")
       #st.image("https://static.streamlit.io/examples/dog.jpg")