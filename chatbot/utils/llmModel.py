from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain.chat_models import AzureChatOpenAI
from utils.config import Confg
load_dotenv()



# def loadModel():        
#     llm = ChatGoogleGenerativeAI(model="gemini-pro",
#                                      google_api_key = os.getenv('google-api'),
#                                      temperature=0,max_output_tokens=20)
#     return llm

def loadModel():
    llm = AzureChatOpenAI(
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_deployment=Confg.model_name,
    model_name=Confg.model_name,
    temperature=0.1)

    return llm