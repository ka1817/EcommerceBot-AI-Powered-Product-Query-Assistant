from langchain_huggingface import HuggingFaceEmbeddings
from src.data_converter import dataconveter
from langchain_community.vectorstores import FAISS
def ingestdata():
    embedding = HuggingFaceEmbeddings()

    docs = dataconveter()

    vector_store = FAISS.from_documents(docs, embedding)

    return vector_store
