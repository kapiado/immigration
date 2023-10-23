import pandas as pd
import streamlit as st

def methMain():
    st.title("Data Cleaning")
    st.write(" ")
    st.header("Descriptive Inputs")
    #st.subheader("Categorical Encoding")
    st.write("")
    columns_included = "Descriptive Columns Used"

    columns_dropped = 'Descriptive Columns Not Used'

    col1, col2 = st.columns(2)

    with col1:
        st.write('**Included**')
        st.write('' + columns_included)

    with col2:
        st.write('**Dropped**')
        st.write('' + columns_dropped)
    #st.caption("        More columns dropped due to high level of nulls, irrelenvant info about the medical center, or redundancy")
    st.write("")

    st.header("Predictive Inputs")
    st.write("")
    columns_included = "Predictive Columns Used"

    columns_dropped = 'Predictive Columns Not Used'

    col1, col2 = st.columns(2)

    with col1:
        st.write('**Included**')
        st.write('' + columns_included)

    with col2:
        st.write('**Dropped**')
        st.write('' + columns_dropped)
    #st.caption("        More columns dropped due to high level of nulls, irrelenvant info about the medical center, or redundancy")
    st.write("")

    if 'rest' not in st.session_state:
        st.session_state.rest = 0
                
    def set_stage():
        methMain()
