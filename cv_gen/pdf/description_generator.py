from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
def gen_description(skill_list, n):
    skill_list = ' '.join(skill_list)
    prompt = PromptTemplate.from_template("""
        Write me a description for my self to put on my Resume based on the following list of skills I have {skill_list} and {n} years of experience in less than 100 words, Each line should have \n character.
    """
    )
    
    model = ChatOpenAI(model = 'gpt-3.5-turbo')

    chain = prompt | model | StrOutputParser()

    return chain.invoke( {'skill_list':skill_list, 'n':n} )
