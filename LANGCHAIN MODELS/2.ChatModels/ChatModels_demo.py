from langchain_ollama import ChatOllama

model=ChatOllama(model="llama3.1:latest",temperature=0)

response=model.invoke("What is the capital of India")

# gives output and some additional model as well
print(response) 