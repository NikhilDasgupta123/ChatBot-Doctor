from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders.merge import MergedDataLoader
import bs4
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.config import Config

import streamlit as st



    


# # Load all web based 
def mergeLoader():
    st.session_state.HeartComponentsloader = WebBaseLoader(web_paths=(Config.path1,),
                 bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                     class_=("column two primary col-lg-8")
                 )))


    st.session_state.clevelandclinicloader = WebBaseLoader(web_paths=(Config.path2,),
                     bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                         class_=("bg-blue-050 py-rem56px","container mt-rem48px")
                     )))
    

    st.session_state.heartLocation = WebBaseLoader(web_paths=(Config.path3,),
                     bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                         class_=('pt-4 default-width','default-width')
                     )))
    
    st.session_state.viral_fever = WebBaseLoader(web_paths=(Config.path3,),
                     bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                         class_=('mw-body-content')
                     )))
    





    st.session_state.loader_all = MergedDataLoader(loaders = [st.session_state.HeartComponentsloader,st.session_state.clevelandclinicloader,st.session_state.heartLocation])

    return st.session_state.loader_all











# Split the Text
def textSplitter(loaderAll):
    # Text Document
    st.session_state.text_documents=loaderAll.load()

    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=5)
    documents=st.session_state.text_splitter.split_documents(st.session_state.text_documents)
    return documents


# def textSplitter(loader_all):
#     # Text Document
#     text_documents=loader_all.load()

#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=5)
#     documents=text_splitter.split_documents(text_documents)
#     return documents