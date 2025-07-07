# 🔍 GenAI Recommender System

A smart recommendation engine that suggests GenAI tools, models, and papers based on your query. Built using local embeddings, FAISS vector search, and Streamlit UI — no OpenAI APIs used.

## 🌟 Features
- Type a research question or topic
- Get relevant tools, models, or research papers
- Powered by `sentence-transformers` + `faiss`
- 100% local and open-source

## 📦 Tech Stack
- Python
- Streamlit
- Sentence-Transformers
- FAISS

## 🧪 Example Queries
- "Best tools to build a chatbot using LLMs"
- "Research papers on Retrieval-Augmented Generation"
- "Lightweight models like Phi-3 for deployment"

## 🚀 Live Demo
👉 [Click here to try it](https://genai-recommender-oz9v4jw2ptxqp7weuuttet.streamlit.app/)

## 🛠 How to Run Locally

```bash
pip install -r requirements.txt
python embedder.py
streamlit run app.py
