from langchain_ollama import OllamaEmbeddings

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding=OllamaEmbeddings(model="nomic-embed-text",dimensions=32)

docs=[
        "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query="Tell me about MS Dhoni"

doc_embed=embedding.embed_documents(docs)

query_embed=embedding.embed_query(query)

# gives the similarity score of query with each index of doc
scores=cosine_similarity([query_embed],doc_embed)[0] 

# now give them index and sort them according to their score values and print max

index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(docs[index])
print("Similarity Score=",score)
