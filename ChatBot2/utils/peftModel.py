from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from peft import PeftModel 
from utils.config import Config
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


class PeftQlora:

    # tokenizer 
    tokenizer = AutoTokenizer.from_pretrained(Config.model_name)
    # laod base model (flan t5 paticularlly)
    base_model = AutoModelForSeq2SeqLM.from_pretrained(Config.model_name)
    model = PeftModel.from_pretrained(base_model, Config.model_name)
    # Create a text-to-text generation pipeline using the loaded model and tokenizer
    text_gen_pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

    # Create a LangChain LLM model from the Hugging Face pipeline
    llm = HuggingFacePipeline(pipeline=text_gen_pipeline)


    def peftQlota(self):
        # Define a prompt template for the chain
        prompt_template = PromptTemplate(input_variables=["input_text"], template="{input_text}")

        # Create a LangChain LLM chain with the defined prompt template
        chain = LLMChain(llm=self.llm, prompt=prompt_template)

        return chain