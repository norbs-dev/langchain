import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    llm = ChatOllama(temperature=0, model='gemma3:270m')
    information = input('What you need to know: ')
    summary_template = "Give the information {information} create a summarize answer about it and fix the English grammar if is there any error"
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)

    
    


if __name__ == "__main__":
    main()
