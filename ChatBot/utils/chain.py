from utils.model import flanT5
from utils.prompt import promptText
from langchain.chains import LLMChain
from utils.config import Config 

# Chain
def llmChain():
    chain = LLMChain(llm=flanT5(),prompt=promptText(), verbose=True)
    return chain