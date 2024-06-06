import streamlit as st
from utils.chain import llmChain
from utils.modelLoader import (mergeLoader,textSplitter)
from utils.vectorDB import db



if 'vector' not in st.session_state:
    # Load all web based and text document
    load = mergeLoader()

    # Text splitter 
    documents = textSplitter(load)

    db(documents)


# Title
st.title('Doctor')

# Input Text
prompt=st.text_input("Search the topic about heart....")

retireved_results = st.session_state.vector_db.similarity_search(prompt)

# Invoke Chain
if prompt:
    st.write(retireved_results[0].page_content)