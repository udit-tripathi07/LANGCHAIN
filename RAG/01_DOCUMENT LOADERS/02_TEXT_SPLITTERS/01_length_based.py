from langchain_text_splitters import CharacterTextSplitter

text="""**CharacterTextSplitter** is a basic text splitter in LangChain that divides large text into smaller chunks using a specified separator, such as a newline (`\n`) or space. It allows you to control the size of each chunk with `chunk_size` and preserve context between chunks using `chunk_overlap`. This splitter is useful for preparing documents for embeddings and retrieval in RAG applications. However, because it splits based on fixed separators, it may sometimes break sentences or paragraphs, making `RecursiveCharacterTextSplitter` a better choice for most real-world use cases.
"""

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)
result=splitter.split_text(text)
print(result)