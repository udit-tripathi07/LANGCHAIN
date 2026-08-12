from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text="""# Artificial Intelligence

Artificial Intelligence enables computers to perform tasks that normally require human intelligence.

## Machine Learning

Machine Learning allows computers to learn patterns from data without being explicitly programmed.

### Supervised Learning

Supervised learning uses labeled data to train models for prediction and classification.

### Unsupervised Learning

Unsupervised learning finds hidden patterns in unlabeled data.

## Deep Learning

Deep Learning uses neural networks with multiple layers to learn complex patterns from large datasets.
"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=300,
    chunk_overlap=0,
   
)
result=splitter.split_text(text)
print(len(result))
print(result[0])