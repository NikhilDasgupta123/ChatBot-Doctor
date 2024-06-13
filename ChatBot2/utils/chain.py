# from utils.model import flanT5
from utils.prompt import promptText
from langchain.chains import LLMChain
from utils.config import Config 
from utils.model import model


# Chain
def llmChain():
    chain = LLMChain(llm=model.llm,prompt=promptText())
    return chain