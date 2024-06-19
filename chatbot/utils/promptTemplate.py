from langchain.prompts import PromptTemplate
from langchain.memory import ChatMessageHistory
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
import streamlit as st



def prompTemp():
    # Create a prompt template for the chatbot that includes chat history
    prompt_template = PromptTemplate(
        input_variables=["chat_history", "user_input", "mysql_data"],
        template="{chat_history}\nUser: {user_input}\nMySQL Data: {mysql_data}\nBot: "
    )

    return prompt_template

        
    


