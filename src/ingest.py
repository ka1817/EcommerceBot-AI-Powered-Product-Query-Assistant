from langchain_huggingface import HuggingFaceEmbeddings
from src.data_converter import dataconveter
from langchain_community.vectorstores import FAISS
def ingestdata():
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L6-v2")

    docs = dataconveter()

    vector_store = FAISS.from_documents(docs, embedding)

    return vector_store
