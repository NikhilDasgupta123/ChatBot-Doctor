from utils.promptTemplate import prompTemp
from .llmModel import loadModel
from langchain.chains import LLMChain, ConversationChain
import streamlit as st
from langchain.memory import ChatMessageHistory, ConversationBufferMemory






# def llmChain():    
#     chatbot_chain = LLMChain(
#         llm=loadModel(),
#         prompt=prompTemp(),
#     )
#     return chatbot_chain

def llmChain():    
    chatbot_chain = LLMChain(
    llm=loadModel(),
    prompt=prompTemp()
)
    return chatbot_chain