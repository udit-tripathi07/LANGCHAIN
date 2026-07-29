from langchain_ollama import OllamaEmbeddings

model=OllamaEmbeddings(model="nomic-embed-text",dimensions=32)

response=model.embed_query("Delhi is the capital of India")

print(str(response))