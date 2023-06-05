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
# page = st.sidebar.selectbox('Go to', ['Overview', 'Average Waiting Time', 'Employee Profile'])

# Use session state to store the current page
current_page = st.session_state.get('current_page', 'Home')

# Update the current page if a new page is selected
if current_page != page:
    st.session_state.current_page = page
    
# Raw file URL on GitHub
file_url = 'https://github.com/kapiado/immigration/blob/main/'

# Define the GitHub repository details
owner = 'kapiado'
repo = 'immigration'

# Define the page Python file URLs
home_url = f'https://raw.githubusercontent.com/{owner}/{repo}/blob/main/1_Overview.py'
about_url = f'https://raw.githubusercontent.com/{owner}/{repo}/main/about.py'
contact_url = f'https://raw.githubusercontent.com/{owner}/{repo}/main/contact.py'

# Fetch the page Python file from the URL
def fetch_page_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

# Import and run the page Python file
def run_page(page_file):
    spec = importlib.util.spec_from_loader('module.name', loader=None)
    module = importlib.util.module_from_spec(spec)
    exec(page_file, module.__dict__)

# Define the page navigation
def navigate_pages():
    st.sidebar.header('Navigation')
    page = st.sidebar.radio('Go to', ['Home', 'About', 'Contact'])
    if page == 'Home':
        page_file = fetch_page_file(home_url)
    elif page == 'About':
        page_file = fetch_page_file(about_url)
    elif page == 'Contact':
        page_file = fetch_page_file(contact_url)
    run_page(page_file)

def main():
    navigate_pages()

if __name__ == '__main__':
    main()
    
# Render different pages based on the selected option
#if page == 'Overview':
    #overview = "1_Overview.py"
    # Retrieve the file content
    #response = requests.get(file_url+overview)
    #file_content = response

    # Display the file content
    #st.code(file_content, language='python')
#elif page == 'Average Waiting Time':
    #avgwaittime = importlib.import_module('Average Waiting Time')
    #avgwaittime.render()
#elif page == 'Employee Profile':
    #emp = importlib.import_module('Employee Profile')
    #emp.render()
