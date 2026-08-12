from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

loader = TextLoader("example.txt")
docs = loader.load()

model=ChatOllama(model="llama3.1:latest")
prompt=PromptTemplate(
    template="Write a 2 line summary of document-\n {paragraph}",
    input_variables=['paragraph']
)

parser=StrOutputParser()

chain=prompt | model | parser

# print(docs)
# print(docs[0])
# print(docs[0].page_content)
print(chain.invoke({'paragraph':docs[0].page_content}))