from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_ollama import ChatOllama

model=ChatOllama(model="llama3.1:latest")

messages=[
    SystemMessage(content='You are a helpful teacher'),
    HumanMessage(content='Explain me Langchain')
]

result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)