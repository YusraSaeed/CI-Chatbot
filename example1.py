
# import os
# import shutil
# from dotenv import load_dotenv
# from langchain_chroma import Chroma
# from langchain_openai import OpenAIEmbeddings,ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# load_dotenv()
# def load_chunks(docs):
#     embeddings = OpenAIEmbeddings( #converts in 0 and 1
#         model = 'text-embedding-ada-002'
#     )
#     vectorstore = Chroma(
#         persist_directory = "./chromadb", 
#         embedding_function = embeddings,
#         collection_name = "test_collecttion"
#     )

#     print("Addinng documents to vectorestore")

#     Chroma.add_documents(vectorstore, docs)

#     print("Documents added to vectorstore")

# def retriever():
#     embeddings = OpenAIEmbeddings(
#         model = 'text-embedding-ada-002'
#     )
#     vectorstore = Chroma(
#         persist_directory = "./chromadb", 
#         embedding_function = embeddings,
#         collection_name = "test_collecttion"
#     )

#     # docs = vectorstore.similarity_search(question, 5)
#     # docs = vectorstore._similarity_search_with_relevance_scores(question, 3)

#     return vectorstore.as_retriever()

# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)


# LLM = ChatOpenAI(model = 'gpt-4o-mini')
# retriever = retriever()
# prompt = ChatPromptTemplate.from_template(
#     """You can answer any question from this data
#     {data}
#     """
# )
# # chain = prompt | LLM | StrOutputParser() # | is pipe. Give output of prev as an input to next 
# chain = (
#     {"data" : retriever | format_docs, "question" : RunnablePassthrough()} |prompt |LLM | StrOutputParser 
# )

# print(chain.invoke("what is parallel computing"))
# # print(chain.invoke({"question" : "dogs"}))

# # response = chain.stream({"question" : "dog"})

# # for chunk in response:
# #     print(chunk, end= "", flush= True)




# chat service with chroma
import os
import shutil
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
load_dotenv()



def load_chunks(docs):
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(
        persist_directory="./chromadb",
        embedding_function=embeddings,
        collection_name="test_collection",
    )
    print("Adding documents to vectorstore")
    Chroma.add_documents(vectorstore, docs)
    print("Documents added to vectorstore")

def get_retriver():
    embeddings = OpenAIEmbeddings(
        model='text-embedding-ada-002'
    )
    vectorstore = Chroma(
        persist_directory="./chromadb",
        embedding_function=embeddings,
        collection_name="test_collection",
    )

    return vectorstore.as_retriever()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)




LLM = ChatOpenAI(model='gpt-4o-mini')
retriver = get_retriver()
prompt = ChatPromptTemplate.from_template(
    """You can answer any question from this data
    {data}

    This is the question: {question}
    """
)
chain = ( 
    {"data": retriver | format_docs, "question": RunnablePassthrough()}
    | prompt 
    | LLM 
    | StrOutputParser())

# print(chain.invoke("what is parallel computing?"))


# response = chain.stream({"question": "dogs"})
# for r in response:
#     print(r, end="",flush=True)


