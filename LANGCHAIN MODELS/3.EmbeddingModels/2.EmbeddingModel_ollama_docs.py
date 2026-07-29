from langchain_ollama import OllamaEmbeddings

model=OllamaEmbeddings(model="nomic-embed-text",dimensions=32)

documents=[
    "Delhi is the capital of India",
    "Paris is the capital of France",
    "Mosco is the capital of Russia"
]

response=model.embed_documents(documents)

print(str(response))