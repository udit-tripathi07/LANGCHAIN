from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path='BOOKS',
    glob='*.pdf', # want to load the pdf files only
    loader_cls=PyPDFLoader
)
# docs=loader.load()     # slow as it loads all the pages at once
docs=loader.lazy_load()  # load generators, load 1 page at a time and use it 
# print(len(docs)) # total number of pages in all the pdfs
# print(docs[1].page_content)

for documents in docs:               # runs slowly for load function and fast for lazy load
    print(documents.metadata) 
