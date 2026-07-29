from langchain_ollama import OllamaLLM
model = OllamaLLM(model="llama3.1")
response = model.invoke("What is the capital of India")
print(response)

# from langchain_openai import OpenAI

# from dotenv import load_dotenv 

# load_dotenv()

# llm=OpenAI(model='gpt-3.5-turbo-instruct')

# result=llm.invoke("who is 2011 cricket world cup winning captain")
# print(result)
