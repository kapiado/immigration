# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 21:59:07 2023

@author: katri
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Average Waiting Time")

st.markdown("# Average Waiting Time")

a = st.empty()
a.write("Insert details on waiting time and how it is attained here")

path = "C:/Users/katri/multipage_app/HTML Files/"

def WTvsNAICS():
    HtmlFile = open(path+"NAICSvsWaitingTime.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height=1500,width=1500)

def WTvsNumCases():
    HtmlFile = open(path+"AvgWTvsNumCasesperIndustry(RedLine).html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height=600)

def avgwait():    
    HtmlFile = open(path+"AvgWaitingTime.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height=600)

def WTvsYear():
    HtmlFile = open(path+"AverageWaitingTimebyYear.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height=600)

def WTvsNumEmp():
    HtmlFile = open(path+"WTvsNumEmp.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height=600)
    
def WTvsExpReq():
    HtmlFile = open(path+"WTvsExpReq.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height=600)
    
def WTvsJobState():
    HtmlFile = open(path+"WTvsJobState.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height=800,width=1000)
    
def nationality():
    HtmlFile = open(path+"Nationality.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height=600,width=1000)

def HighestEducation():
    HtmlFile = open(path+"HighestEducation.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height=600, width=1500)

    
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Year","Nationality","Highest Education","Industry","Number of Cases per Industry", "Number of Employees","Experience Required","Employer State"])

with tab1:
   avgwait()
   WTvsYear()

with tab2:
    nationality()
    
with tab3:
    HighestEducation()

with tab4:
   WTvsNAICS()
   
with tab5:
   WTvsNumCases()
   
with tab6:
    WTvsNumEmp()
    
with tab7:
    WTvsExpReq()
    
with tab8:
    WTvsJobState()
    