from langchain_community.llms import HuggingFaceHub
from utils.config import Config
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from peft import PeftModel 
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

os.environ['HUGGINGFACEHUB_API_TOKEN']=os.getenv('api_key')




class model:

    ### Pre trained model
    def flanT5():
        llm_hf = HuggingFaceHub(
        repo_id = Config.model,
        model_kwargs= Config.generation_params
    )
        return llm_hf
    


    ### Fine tuned model 

    # # tokenizer 
    # tokenizer = AutoTokenizer.from_pretrained(Config.finetuned_peft_model)
    # # laod base model (flan t5 paticularlly)
    # base_model = AutoModelForSeq2SeqLM.from_pretrained(Config.finetuned_peft_model)
    # model = PeftModel.from_pretrained(base_model, Config.finetuned_peft_model)
    # # Create a text-to-text generation pipeline using the loaded model and tokenizer
    # text_gen_pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

    # # Create a LangChain LLM model from the Hugging Face pipeline
    # llm = HuggingFacePipeline(pipeline=text_gen_pipeline)


