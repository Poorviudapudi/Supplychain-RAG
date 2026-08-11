from fastapi import FastAPI, UploadFile, File
from typing import List
from pydantic import BaseModel
import os
import shutil
import sys
# Add parent directory to path so ingest and rag can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ingest import ingest_pdfs
from rag import query_rag
from langchain_chroma import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

app = FastAPI(title="Supply Chain RAG API")

class AskRequest(BaseModel):
    question: str
    top_k: int = 5

@app.post("/ingest")
async def ingest(files: List[UploadFile] = File(...)):
    # Save uploaded files temporarily
    os.makedirs("temp_uploads", exist_ok=True)
    file_paths = []
    for file in files:
        file_path = f"temp_uploads/{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        file_paths.append(file_path)
    
    files_count, chunks_count = ingest_pdfs(file_paths)
    
    # Cleanup temp files
    for path in file_paths:
        os.remove(path)
        
    return {"files": files_count, "chunks": chunks_count}

@app.post("/ask")
async def ask(request: AskRequest):
    answer, sources = query_rag(request.question, request.top_k)
    return {"answer": answer, "sources": sources}

@app.get("/stats")
async def stats():
    db = Chroma(persist_directory="chroma_db", embedding_function=FastEmbedEmbeddings())
    try:
        total_chunks = db._collection.count()
    except:
        total_chunks = 0
    return {
        "collection_name": "langchain",
        "total_chunks": total_chunks,
        "embedding_model": "FastEmbed",
        "llm_model": "llama-3.3-70b-versatile"
    }
