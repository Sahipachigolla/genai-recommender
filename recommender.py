import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
with open("data/resources.json") as f:
    data = json.load(f)

index = faiss.read_index("vector_store/index.faiss")

def recommend(query, top_k=5):
    q_embed = model.encode([query])
    D, I = index.search(np.array(q_embed), top_k)
    results = [data[i] for i in I[0]]
    return results
