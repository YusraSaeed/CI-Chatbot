from  langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from chromadb_service import load_chunks
from chromadb_service import load_chunks
import logging

logging.basicConfig (
    level = logging.DEBUG,
    format = '[%(asctime)s] - [%(levelname)s] - %(message)s',
    filename= "./pdf_handler.log"
)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")


loader = PyPDFLoader('./Lecture 01 - Introduction to Parallel and Distributed Computing.pdf')

docs = loader.load() #list

# print(docs[0])

# print("Length: ", len(docs))


splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 20,
    length_function = len,
    is_separator_regex= False
)

chunks = []

for page in docs:
    text = page.page_content
    pieces = splitter.create_documents([text])
    chunks.extend(pieces)


# # load_chunks(chunks)
logging.warning (chunks[0])
# print(chunks[0])
# print("Length of chunk: ", len(chunks))