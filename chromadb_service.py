import os
# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import shutil

load_dotenv()

def load_chunks(docs):
    embeddings = OpenAIEmbeddings( #converts in 0 and 1
        model = 'text-embedding-ada-002'
    )
    vectorstore = Chroma(
        persist_directory = "./chromadb", 
        embedding_function = embeddings,
        collection_name = "test_collecttion"
    )

    print("Addinng documents to vectorestore")

    Chroma.add_documents(vectorstore, docs)

    print("Documents added to vectorstore")

def retriever(question):
    embeddings = OpenAIEmbeddings(
        model = 'text-embedding-ada-002'
    )
    vectorstore = Chroma(
        persist_directory = "./chromadb", 
        embedding_function = embeddings,
        collection_name = "test_collecttion"
    )

    docs = vectorstore.similarity_search(question, 5)
    # docs = vectorstore._similarity_search_with_relevance_scores(question, 3)

    return docs

# documents = retriever("what is parallel computing")

# for i in documents:
#     print(i, "\n\n")