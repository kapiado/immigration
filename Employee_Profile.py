# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 21:59:07 2023

@author: katri
"""

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

def employeeprofile():
        st.markdown("# Employee Profile")
            
        c = st.empty()
        c.write("The Employee Profile includes key information about the demographic of employees in our dataset, who undergo the green card application process in the United States. This includes their education, salary, nationality, profession, major and layoff history. In the profile, we present visual representations of the data related to Immigration Backlog. We will explore the trend of immigration backlog overtime, in terms of applications received and waiting time for approval, for example. By examining these factors, we aim to gain insights into the patterns and changes within the immigration backlog, enabling a better understanding.")
        path = "HTML Files/"
        updatedpath = "HTML Files/Updated HTML Files/"
        
        def WTvsYear():
                HtmlFile = open(updatedpath+"Avgwtperyr.html", 'r', encoding='utf-8')
                source_code = HtmlFile.read() 
                print(source_code)
                components.html(source_code,height=600) 
                
        def NumCasesvsNAICSTop10():
                HtmlFile = open(updatedpath+"OccvsNumCases.html", 'r', encoding='utf-8')
                source_code = HtmlFile.read() 
                print(source_code)
                components.html(source_code,height=1000, width=1000)
        
        def NumCasesvsNAICSBot10():
                HtmlFile = open(updatedpath+"OccvsNumCasesBottom10.html", 'r', encoding='utf-8')
                source_code = HtmlFile.read() 
                print(source_code)
                components.html(source_code,height=1000, width=1000)
                        
        def WTvsNAICSTop10():
                HtmlFile = open(updatedpath+"AvgWTperOcc.html", 'r', encoding='utf-8')
                source_code = HtmlFile.read() 
                print(source_code)
                components.html(source_code,height=1000, width=1000)  
        
        def WTvsNAICSTBot10():
                HtmlFile = open(updatedpath+"AvgWTperOccBottom10.html", 'r', encoding='utf-8')
                source_code = HtmlFile.read() 
                print(source_code)
                components.html(source_code,height=1000, width=1000)  
                        
        def WTvsSalary():
                HtmlFile = open(path+"WTvsEmployeeSalary (3).html", 'r', encoding='utf-8')
                source_code = HtmlFile.read() 
                print(source_code)
                components.html(source_code,height=500)
                    
        def NumCasesvsSalary():
                HtmlFile = open(path+"NumCasesvsSalary (2).html", 'r', encoding='utf-8')
                source_code = HtmlFile.read() 
                print(source_code)
                components.html(source_code,height=500)
                    
        def unitofpay():
                HtmlFile = open(path+"unitofPaygraph.html", 'r', encoding='utf-8')
                source_code = HtmlFile.read() 
                print(source_code)
                components.html(source_code,height=600)
                        
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
                    
                        
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Year","Industry","Nationality","Salary","Unit of Pay","Highest Education"])
        	
        with tab1:
                WTvsYear()
                       
        with tab2:
                NumCasesvsNAICSTop10()
                NumCasesvsNAICSBot10()
                WTvsNAICSTop10()
                WTvsNAICSBot10()
        
        with tab3:
                nationality()
                        
        with tab4:
                NumCasesvsSalary()
                WTvsSalary()
                        
        with tab5:
                unitofpay()
                        
        with tab6:
                HighestEducation()
                
        if 'rest' not in st.session_state:
                st.session_state.rest = 0
                
        def set_stage():
                employeeprofile()
           
            
            
