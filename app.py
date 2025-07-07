import os
os.environ["STREAMLIT_WATCH_USE_POLLING"] = "true"


import streamlit as st
from recommender import recommend

st.set_page_config(page_title="GenAI Recommender", layout="centered")

st.title("🔍 GenAI Recommender System")
st.markdown("Ask something like: *'best tools for fine-tuning LLMs'* or *'RAG papers'*")

query = st.text_input("Enter your query")

if query:
    with st.spinner("Finding relevant tools and resources..."):
        results = recommend(query)
        for item in results:
            st.subheader(f"{item['title']} ({item['type']})")
            st.write(item["description"])
            st.markdown(f"[🔗 Visit]({item['url']})", unsafe_allow_html=True)
