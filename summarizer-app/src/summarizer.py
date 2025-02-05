from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate


def summarize_text(text, number):
    # Initialize the OpenAI model
    llm = OpenAI(openai_api_key="sk-svcacct-38lVsQJmAnpHYYGlwHLRfemYH6XipJ83Bn4AHnE19lo8NioSbNQshLh_0Ie6gFHT3BlbkFJgi4LuRlCOMye2qnlGRAGY4_JQCoLousyuBpUsrPte0HftMthAZWRdreWw1EFRdQA")


    prompt = PromptTemplate.from_template(
        "Summarize the following text ({text}) into this number ({number}) of sentences. The summary MUST NOT be longer than the given number of sentences!!!"
    )

    question = prompt.format(text=text, number=number)
    summary = llm.invoke(question)
    return summary
