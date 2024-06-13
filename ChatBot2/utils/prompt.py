from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate

## Pretrained Prompt 

def promptText():
    # Prompt
    prompt = ChatPromptTemplate.from_template(
"""
Answer the questions based on Body Heart related only
Please provide the most accurate response based on the question in five line
If question is out of context then show the text This is Heart Doctor
<context>
{context}
<context>
Questions:{input}

"""
)
    
    return prompt

# def promptText():
#     # Define a prompt template for the chain
#     prompt_template = PromptTemplate(input_variables=["input_text"], template="{input_text}")
#     return prompt_template