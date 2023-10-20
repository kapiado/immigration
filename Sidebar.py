import pandas as pd
import streamlit as st

#center text align indexes cluster
#comma separate bars
#features -> predictors + drop veteran column
#clustering image\#new flowchart
#Machine Learning: Explain what that is
#details on stuff. data partitioning, which hyperparameters

#explain more about AWS

#more about feature importance
#decision tree download


def sideBar():
    tabs = ["Home", "Overview"]

    st.sidebar.subheader("Navigation")
    home_button = st.sidebar.button("Home", key="Home", type="secondary")
    overview_button = st.sidebar.button("Overview", key="Overview", type="secondary")
    employeeprofile_button = st.sidebar.button("Employee Profile", key="Employee Profile", type="secondary")
    #dashboard_button = st.sidebar.button("Predictive Dashboard", key="Predictive Dashboard", type="secondary")
    st.write(" ")
    #st.sidebar.subheader("Methodology")
    #data_description_button = st.sidebar.button("Data Description", key="Data Description", type="secondary")
    #data_cleaning_button = st.sidebar.button("Data Cleaning", key="Data Cleaning", type="secondary")
    #clustering_button = st.sidebar.button("Clustering", key="Clustering", type="secondary")
    #ml_button = st.sidebar.button("Machine Learning", key="Machine Learning", type="secondary")
    #results_button = st.sidebar.button("Results", key="Results", type="secondary")

    # Store the buttons in a list
    selection = [home_button, overview_button]

    # Return the list of buttons
    return selection



