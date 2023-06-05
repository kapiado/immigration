# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:17:05 2023

@author: katri
"""
import streamlit as st
import importlib

# Create a sidebar
st.sidebar.header('Navigation')

# Add links to different pages
page = st.sidebar.selectbox('Go to', ['Overview', 'Average Waiting Time', 'Employee Profile'])

# Render different pages based on the selected option
if page == 'Overview':
    overview = importlib.import_module('Overview')
    overview.render()
elif page == 'Average Waiting Time':
    avgwaittime = importlib.import_module('Average Waiting Time')
    avgwaittime.render()
elif page == 'Employee Profile':
    emp = importlib.import_module('Employee Profile')
    emp.render()
