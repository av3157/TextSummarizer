from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate


def summarize_text(text, number):
    # Initialize the OpenAI model
    llm = OpenAI(openai_api_key="insert key here")


    prompt = PromptTemplate.from_template(
        "Summarize the following text ({text}) into this number ({number}) of sentences. The summary MUST NOT be longer than the given number of sentences!!!"
    )

    question = prompt.format(text=text, number=number)
    summary = llm.invoke(question)
    return summary
