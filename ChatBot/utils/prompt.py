from langchain_core.prompts import ChatPromptTemplate


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