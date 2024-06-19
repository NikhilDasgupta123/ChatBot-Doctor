from langchain_community.agent_toolkits import create_sql_agent
from utils.llmModel import loadModel
from utils.db import mySQL
import streamlit as st

def sqlAgent():
    
    # Create an SQL agent using the LLM and SQL database
    agent_executor = create_sql_agent(
        loadModel(), 
        db=mySQL(),
        agent_type="openai-tools", 
        verbose=True, 
        handle_parsing_errors=True
    )

    return agent_executor


# Define function to fetch data from MySQL using the SQL agent
def fetch_data_from_mysql(user_input):
    try:
        # Run the agent executor with user input to fetch data
        response = sqlAgent().run(user_input)
        return response
    except Exception as e:
        st.error(f"Error fetching data from MySQL: {e}")
        return ""