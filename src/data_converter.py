import pandas as pd
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
from dotenv import load_dotenv
from langchain_core.documents import Document


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def dataconveter():
    base_dir = os.path.dirname(os.path.dirname(__file__))  
    file_path = os.path.join(base_dir, "data", "flipkart_product_review.csv")

    product_data = pd.read_csv(file_path)
    product_data.head()
    data = product_data[["product_title", "review"]]
    product_list = []

    for index, row in data.iterrows():
        obj = {
            'product_name': row['product_title'],
            'review': row['review']
        }
        product_list.append(obj)

    docs = []
    for entry in product_list:
        metadata = {"product_name": entry['product_name']}
        doc = Document(page_content=entry['review'], metadata=metadata)
        docs.append(doc)
    
    return docs

if __name__=='__main__':
    docs=dataconveter()
    print(f"Sample Document:\n{docs[0].page_content}\n")