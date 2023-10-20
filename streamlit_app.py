import pandas as pd
import streamlit as st
#from Homepage import home
from Overview import overview
from Sidebar import sideBar
from Employee_Profile import employeeprofile
#from dataCleaning import v2
#from backendInterface import interface
#from methodology import methMain
#from dataDescription import dataDesc
#from clustering import clustMain
#from results import resultMain
#from ml import mlMain

def initializeSideBar():
    if "counter" not in st.session_state:
        st.session_state.counter = 0
        home()

    selection = sideBar()
    if selection[0]:
        overview()
        st.session_state.counter = 1
    if selection[1]:
        employeeprofile()
    #if selection[2]:
    #    dataDesc()
    #if selection[3]:
    #    methMain()
    #if selection[4]:
    #    clustMain()
    #if selection[5]:
    #    mlMain()
    #if selection[6]:
    #    resultMain()

def main():
    initializeSideBar()

if __name__ == '__main__':
    with open("style.css") as f:
     st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html = True)
    main()
