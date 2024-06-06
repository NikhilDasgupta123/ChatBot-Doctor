from langchain_community.llms import HuggingFaceHub

import os
from dotenv import load_dotenv
load_dotenv()

os.environ['HUGGINGFACEHUB_API_TOKEN']=os.getenv('api_key')


def flanT5():
    llm_hf = HuggingFaceHub(
    repo_id = 'google/flan-t5-xxl',
    model_kwargs={'temperatur':0.8}
)
    return llm_hf