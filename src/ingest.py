from langchain.embeddings import HuggingFaceEmbeddings
from data_converter import dataconveter
from langchain.vectorstores import FAISS
def ingestdata():
    embedding = HuggingFaceEmbeddings()

    docs = dataconveter()

    vector_store = FAISS.from_documents(docs, embedding)

    return vector_store
