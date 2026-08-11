import os
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

CHROMA_PATH = "chroma_db"

PROMPT_TEMPLATE = """
Answer only from the context provided below. If the context does not contain the answer, say the information is not available in the uploaded documents.

Context:
{context}

Question:
{question}
"""

def query_rag(question: str, top_k: int = 5):
    if not os.path.exists(CHROMA_PATH):
        return "No documents indexed yet.", []
    
    # Use FastEmbed (Free, runs locally, no API key needed)
    embedding_function = FastEmbedEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    
    # Search the DB
    results = db.similarity_search_with_score(question, k=top_k)
    
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=question)
    
    # Use Groq Llama3 (Free API)
    model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.1)
    response = model.invoke(prompt)
    
    sources = []
    for doc, _score in results:
        source_info = {
            "file": os.path.basename(doc.metadata.get("source", "Unknown")),
            "page": doc.metadata.get("page", 0) + 1  # 1-indexed pages
        }
        sources.append(source_info)
        
    return response.content, sources
