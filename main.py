# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:17:05 2023

@author: katri
"""
import streamlit as st
import importlib
import requests

# Create a sidebar
st.sidebar.header('Navigation')

# Add links to different pages
page = st.sidebar.selectbox('Go to', ['Overview', 'Average Waiting Time', 'Employee Profile'])

# Use session state to store the current page
current_page = st.session_state.get('current_page', 'Home')

# Update the current page if a new page is selected
if current_page != page:
    st.session_state.current_page = page
    
# Raw file URL on GitHub
file_url = 'https://github.com/kapiado/immigration/'


    
# Render different pages based on the selected option
if page == 'Overview':
    overview = "1_Overview.py"
    # Retrieve the file content
    response = requests.get(file_url+overview)
    file_content = response.text

    # Display the file content
    st.code(file_content, language='python')
elif page == 'Average Waiting Time':
    avgwaittime = importlib.import_module('Average Waiting Time')
    avgwaittime.render()
elif page == 'Employee Profile':
    emp = importlib.import_module('Employee Profile')
    emp.render()
