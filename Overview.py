# -*- coding: utf-8 -*-
"""
Created on Wed May 31 18:26:27 2023

@author: katri
"""

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


def overview():
    #st.set_page_config(page_title="Overview")
    st.write("# Overview")

    path = "HTML Files/"

    def cases():
        HtmlFile = open("CasesReceived.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,height=480)
        
    def avgwait():    
        HtmlFile = open(path+"AverageWaitingTime.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,height=600)
    
    cases()
    avgwait()
    
    a = st.empty()
    a.write("The North American Industry Classification System (NAICS) is a standardized system used to classify business establishments based on their economic activity in Canada, Mexico, and the United States. It provides a hierarchical structure that groups businesses into various sectors, subsectors, industry groups, and industries. The NAICS code is a unique numerical identifier assigned to each business entity, allowing for consistent and comparable data collection and analysis across different industries and regions.")
