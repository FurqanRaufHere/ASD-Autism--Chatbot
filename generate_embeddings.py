import os
import json
import numpy as np
import faiss
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

# Paths
CHUNK_FILE = "./ProcessedData/chunks.json"
INDEX_FILE = "./ProcessedData/faiss_index.index"
METADATA_FILE = "./ProcessedData/metadata.json"

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load chunks
with open(CHUNK_FILE, "r", encoding="utf-8") as f:
    chunks = json.load(f)

# Embed chunks
print("🧠 Generating embeddings...")
texts = [chunk["text"] for chunk in chunks]
embeddings = model.encode(texts, show_progress_bar=True)

# Convert to numpy float32 for FAISS
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, INDEX_FILE)
print(f"✅ FAISS index saved to {INDEX_FILE}")

# Save metadata (chunk text and source file)
metadata = [{"text": chunk["text"], "source": chunk["source"]} for chunk in chunks]
with open(METADATA_FILE, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)
print(f"📎 Metadata saved to {METADATA_FILE}")
