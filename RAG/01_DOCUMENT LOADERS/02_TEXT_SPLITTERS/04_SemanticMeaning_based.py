from langchain_experimental.text_splitter import SemanticChunker
from langchain_ollama import OllamaEmbeddings

text="""Artificial intelligence is transforming many industries by allowing computers to perform tasks that normally require human intelligence. Machine learning is one of the most important branches of artificial intelligence.

Machine learning systems learn patterns from data and use those patterns to make predictions. Supervised learning uses labeled examples, while unsupervised learning discovers patterns in data without predefined labels.

Deep learning is a specialized area of machine learning that uses neural networks with many layers. These models are particularly effective for images, speech, and natural language processing.

Natural language processing focuses on enabling computers to understand and generate human language. Modern NLP systems often use transformer architectures and large language models.

Retrieval Augmented Generation combines language models with external knowledge sources. A RAG system retrieves relevant information from documents and provides that information to the language model as context.

Vector databases are commonly used in RAG systems to store embeddings. Embeddings represent the semantic meaning of text as numerical vectors, allowing the system to retrieve information based on meaning rather than exact keyword matches.
"""

splitter=SemanticChunker(
    OllamaEmbeddings(model="nomic-embed-text"),
breakpoint_threshold_type="standard_deviation",
breakpoint_threshold_amount=1      
   )

result=splitter.create_documents([text])
print(len(result))
print(result[0])