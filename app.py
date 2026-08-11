import streamlit as st
import os
from ingest import ingest_pdfs
from rag import query_rag

st.set_page_config(page_title="Supply Chain RAG", layout="wide")

st.title("Supply Chain Documents Assistant")

with st.sidebar:
    st.header("Upload Documents")
    uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
    if st.button("Index"):
        if uploaded_files:
            if not os.environ.get("GROQ_API_KEY"):
                st.error("Please set the GROQ_API_KEY in the .env file.")
            else:
                os.makedirs("temp_uploads", exist_ok=True)
                file_paths = []
                for file in uploaded_files:
                    file_path = os.path.join("temp_uploads", file.name)
                    with open(file_path, "wb") as f:
                        f.write(file.getvalue())
                    file_paths.append(file_path)
                
                with st.spinner("Indexing documents... (This may take a minute)"):
                    files_processed, chunks_stored = ingest_pdfs(file_paths)
                st.success(f"{files_processed} files processed, {chunks_stored} chunks stored")
                
                for path in file_paths:
                    os.remove(path)
        else:
            st.warning("Please upload files first.")

st.header("Ask a Question")
question = st.text_input("Enter your question:")
if st.button("Submit"):
    if not os.environ.get("GROQ_API_KEY"):
        st.error("Please set the GROQ_API_KEY in the .env file.")
    elif question:
        with st.spinner("Finding answer..."):
            answer, sources = query_rag(question, top_k=5)
            st.markdown("### Answer")
            st.write(answer)
            st.markdown("### Sources")
            for source in sources:
                st.caption(f"- Document: {source['file']}, Page: {source['page']}")
    else:
        st.warning("Please enter a question.")
