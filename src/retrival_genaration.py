from src.ingest import ingestdata
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os 
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from src.query_rewritting import query_rewriting
GROQ_API_KEY=os.getenv('GROQ_API_KEY')
def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 3})

    PRODUCT_BOT_TEMPLATE = """
    Your ecommerce bot is an expert in product recommendations and customer queries.
    It analyzes product titles and reviews to provide accurate and helpful responses.
    Ensure your answers are relevant to the product context and refrain from straying off-topic.
    Your responses should be concise and informative.

    CONTEXT:
    {context}

    QUESTION: {question}

    YOUR ANSWER:
    """

    prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)
    llm = ChatGroq(api_key=GROQ_API_KEY,model="llama-3.3-70b-versatile")

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain


if __name__ == '__main__':
    vstore = ingestdata()

    chain = generation(vstore)

    question = "which product has the highest rating"
    rewritten_query = query_rewriting(question)

    response = chain.invoke(question)

    print(f"Response: {response}")
