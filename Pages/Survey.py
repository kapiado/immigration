# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 00:37:41 2023

@author: katri
"""

import streamlit as st
import pandas as pd

st.title("Survey Form")
st.subheader("Enter details below:")

with st.form("form1", clear_on_submit=True):
    name = st.text_input("Full Name OR Anonymous")
    email = st.text_input("Email")
    message = st.text_area("Message")
    rating = st.slider("Rate the usability of this tool:",min_value=1, max_value=10)
    
    submit = st.form_submit_button("Submit this form")