from sentence_transformers import SentenceTransformer
import json
import numpy as np
import faiss
import os

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load data
with open("data/resources.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Embed descriptions
descriptions = [item["description"] for item in data]
embeddings = model.encode(descriptions, show_progress_bar=True)

# Create vector store
dim = embeddings[0].shape[0]
index = faiss.IndexFlatL2(dim)
index.add(np.array(embeddings))

# Ensure folder exists
os.makedirs("vector_store", exist_ok=True)

# Save index
faiss.write_index(index, "vector_store/index.faiss")

print("✅ Vector index created and saved.")
