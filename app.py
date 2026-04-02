import streamlit as st
from pubmed_fetch import fetch_pubmed
from summarizer import summarize_text, answer_question

# Page config
st.set_page_config(page_title="AI Research Assistant", layout="wide")

# Header
st.title("🧠 AI Research Paper Assistant")
st.markdown("Search, summarize, and interact with real PubMed research papers using AI")

# Input
query = st.text_input("🔍 Enter topic (e.g., diabetes, cancer, heart disease)")

# Button
if st.button("🚀 Search & Analyze"):
    if not query:
        st.warning("Please enter a topic")
    else:
        with st.spinner("Fetching research papers..."):
            papers = fetch_pubmed(query)

        if not papers:
            st.error("No papers found")
        else:
            for i, paper in enumerate(papers, 1):
                with st.container():
                    st.markdown(f"## 📄 Paper {i}")

                    # Title
                    st.markdown(f"**Title:** {paper['title']}")

                    # Optional link (if added in backend)
                    if "url" in paper:
                        st.markdown(f"[🔗 View Full Paper]({paper['url']})")

                    # Show abstract toggle
                    if st.checkbox(f"📖 Show Abstract (Paper {i})"):
                        st.info(paper["abstract"])

                    # SUMMARY
                    if paper["abstract"]:
                        with st.spinner("Generating summary..."):
                            summary = summarize_text(paper["abstract"])

                        st.markdown("### 🔍 Summary")
                        st.markdown(summary)
                    else:
                        st.warning("No abstract available")

                    # Q&A SECTION
                    st.markdown("### 💬 Ask a Question")

                    question = st.text_input(
                        f"Ask something about Paper {i}",
                        key=f"question_{i}"
                    )

                    if question:
                        with st.spinner("Thinking..."):
                            answer = answer_question(
                                paper["abstract"][:1500],
                                question
                            )

                        st.markdown("#### 🤖 Answer")
                        st.success(answer)

                    st.divider()
                    