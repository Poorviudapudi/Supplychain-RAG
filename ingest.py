import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

CHROMA_PATH = "chroma_db"

def ingest_pdfs(file_paths):
    docs = []
    for path in file_paths:
        loader = PyPDFLoader(path)
        docs.extend(loader.load())
    
    # Chunking: 800-1200 chunk size, 100-200 overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_documents(docs)
    
    # Use FastEmbed (Free, runs locally, no API key needed)
    embeddings = FastEmbedEmbeddings()
    
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )
    return len(file_paths), len(chunks)

if __name__ == "__main__":
    # Test script
    base_dir = "data"
    pdf_files = [os.path.join(base_dir, f) for f in os.listdir(base_dir) if f.endswith('.pdf')]
    if pdf_files:
        files_processed, chunks_stored = ingest_pdfs(pdf_files)
        print(f"{files_processed} files processed, {chunks_stored} chunks stored")
    else:
        print("No PDFs found in data directory.")
