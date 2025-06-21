import os
import json
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Paths
PDF_DIR = "./data"
OUTPUT_DIR = "./ProcessedData"
EXTRACTED_FILE = os.path.join(OUTPUT_DIR, "extracted_texts.json")
CHUNK_FILE = os.path.join(OUTPUT_DIR, "chunks.json")

# Ensuring output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_text_from_pdfs(pdf_dir):
    documents = []
    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            path = os.path.join(pdf_dir, filename)
            with pdfplumber.open(path) as pdf:
                text = "\n".join([page.extract_text() or "" for page in pdf.pages])
                documents.append({"filename": filename, "content": text})
    return documents

def chunk_documents(documents, chunk_size=500, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    all_chunks = []
    for doc in documents:
        chunks = text_splitter.split_text(doc["content"])
        for chunk in chunks:
            all_chunks.append({
                "source": doc["filename"],
                "text": chunk
            })
    return all_chunks

if __name__ == "__main__":
    print("📄 Extracting text from PDFs...")
    docs = extract_text_from_pdfs(PDF_DIR)
    
    print("✂️ Splitting into chunks...")
    chunks = chunk_documents(docs)

    # Save results
    with open(EXTRACTED_FILE, "w", encoding="utf-8") as f:
        json.dump(docs, f, indent=2)

    with open(CHUNK_FILE, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)

    print(f"✅ Extraction and chunking completed. {len(chunks)} chunks saved.")
