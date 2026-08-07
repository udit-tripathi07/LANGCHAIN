from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
model =ChatOllama(model="llama3.1:latest")

template1=PromptTemplate(
    template="Write a report on {topic}",
    input_variables={'topic'}
)

template2=PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables={'text'}
)

parser=StrOutputParser()

# instead of doing it manually we can make a pipeline using parser 

chain=template1 | model | parser | template2 | model | parser

result=chain.invoke({'topic':'MS Dhoni'})

print(result)