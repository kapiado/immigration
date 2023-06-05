# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:17:05 2023

@author: katri
"""
import streamlit as st
import importlib
import subprocess

# Create a sidebar
st.sidebar.header('Navigation')

# Add links to different pages
page = st.sidebar.selectbox('Go to', ['Overview', 'Average Waiting Time', 'Employee Profile'])

# Use session state to store the current page
current_page = st.session_state.get('current_page', 'Home')

# Update the current page if a new page is selected
if current_page != page:
    st.session_state.current_page = page
  
# Render different pages based on the selected option
if page == 'Overview':
    subprocess.call(["python", "1_Overview.py"])

    # Display the file content
    #st.code(file_content, language='python')
#elif page == 'Average Waiting Time':
    #avgwaittime = importlib.import_module('Average Waiting Time')
    #avgwaittime.render()
#elif page == 'Employee Profile':
    #emp = importlib.import_module('Employee Profile')
    #emp.render()
