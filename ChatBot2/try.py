from langchain_community.llms import HuggingFaceHub
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders.merge import MergedDataLoader
import bs4
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)


import time

import streamlit as st 
import os
from utils.config import Config
from dotenv import load_dotenv
load_dotenv()

# Hugging Face Model key
os.environ['HUGGINGFACEHUB_API_TOKEN']=os.getenv('api_key')



# Load Model 
llm_hf = HuggingFaceHub(
    repo_id = 'google/flan-t5-xxl',
    model_kwargs={'temperatur':0.1}
)








# Making RAG Application
# HeartComponentsloader = WebBaseLoader(web_paths=("https://www.cincinnatichildrens.org/health/h/heart-components",),
#                      bs_kwargs=dict(parse_only=bs4.SoupStrainer(
#                          class_=("column two primary col-lg-8")

#                      )))

# clevelandclinicloader = WebBaseLoader(web_paths=("https://my.clevelandclinic.org/health/body/21704-heart",),
#                      bs_kwargs=dict(parse_only=bs4.SoupStrainer(
#                          class_=("bg-blue-050 py-rem56px","container mt-rem48px")

#                      )))





# # load all web based
# loader_all = MergedDataLoader(loaders = [HeartComponentsloader,clevelandclinicloader])
# # Text Document
# text_documents=loader_all.load()


# # Split the Text
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=5)
# documents=text_splitter.split_documents(text_documents)

if 'vector' not in st.session_state:
    st.session_state.HeartComponentsloader = WebBaseLoader(web_paths=("https://www.cincinnatichildrens.org/health/h/heart-components",),
                     bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                         class_=("column two primary col-lg-8")

                     )))
    
    st.session_state.clevelandclinicloader = WebBaseLoader(web_paths=("https://my.clevelandclinic.org/health/body/21704-heart",),
                     bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                         class_=("bg-blue-050 py-rem56px","container mt-rem48px")

                     )))

    # load all web based
    st.session_state.loader_all = MergedDataLoader(loaders = [st.session_state.HeartComponentsloader,st.session_state.clevelandclinicloader])

    # Text Document
    st.session_state.text_documents=st.session_state.loader_all.load()

    # Split the Text
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=5)
    documents=st.session_state.text_splitter.split_documents(st.session_state.text_documents)





    # create the open-source embedding function
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    st.session_state.vector_db=FAISS.from_documents(documents,embedding_function)




# Prompt
prompt=ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}

"""
)


# Chain
chain = LLMChain(llm=llm_hf,prompt=prompt)


# Document Chain
document_chain = create_stuff_documents_chain(llm=llm_hf,prompt=prompt)



# Title
st.title('Heart Doctor')

prompt=st.text_input("Search the topic about heart....")

retireved_results = st.session_state.vector_db.similarity_search(prompt)

if prompt:
    st.write(retireved_results[0].page_content)