from dotenv import load_dotenv
import streamlit as st
# from utils.memory import config
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from utils.agents import fetch_data_from_mysql
from utils.chains import llmChain
from utils.agents import sqlAgent





# Define a function to get the bot's response
def invoke_chain(chat_history, user_input, mysql_data):
    response = llmChain().run({"chat_history": chat_history, "user_input": user_input, "mysql_data": mysql_data})
    return response






def main():
    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Function to format chat history for the prompt
    def format_chat_history(messages):
        chat_history = ""
        for message in messages:
            role = "User" if message["role"] == "user" else "Bot"
            chat_history += f"{role}: {message['content']}\n"
        return chat_history
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Initial welcome message from the assistant
    initial_message = "Hello! How can I assist you today?"
    st.session_state.messages.append({"role": "assistant", "content": initial_message})
    with st.chat_message("assistant"):
        st.markdown(initial_message)
    
    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
    
        # Fetch data from MySQL using the SQL agent
        mysql_data = fetch_data_from_mysql(prompt)
    
        # Format chat history
        chat_history = format_chat_history(st.session_state.messages)
    
        # Display assistant response in chat message container
        with st.spinner("Generating response..."):
            response = invoke_chain(chat_history, prompt, mysql_data)
            with st.chat_message("assistant"):
                st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    

if __name__ == '__main__':
    main()