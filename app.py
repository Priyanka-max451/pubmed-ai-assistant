import streamlit as st
from pubmed_fetch import fetch_pubmed
from summarizer import summarize_text, answer_question

# Page config
st.set_page_config(page_title="AI Research Assistant", layout="wide")

st.title("🧠 AI Research Paper Assistant")
st.markdown("Search, summarize, and interact with real PubMed research papers using AI")

# Input
query = st.text_input("🔍 Enter topic (e.g., diabetes, cancer)")

# Button
if st.button("🚀 Search & Analyze"):

    if not query:
        st.warning("Please enter a topic")

    else:
        papers = fetch_pubmed(query, max_results=3)

        # DEBUG (remove later)
        st.write("DEBUG:", papers)

        if not papers:
            st.error("No papers found")
        else:
            for i, paper in enumerate(papers):

                st.markdown("---")
                st.subheader(f"📄 Paper {i+1}")
                st.write(f"**Title:** {paper['title']}")

                # Abstract
                abstract = paper.get("abstract", "")
                if abstract:
                    with st.expander("📖 View Abstract"):
                        st.write(abstract)
                else:
                    st.warning("No abstract available")

                # Summary
                if st.button(f"🧠 Generate Summary {i}", key=f"sum_{i}"):
                    with st.spinner("Generating summary..."):
                        summary = summarize_text(abstract)
                    st.success(summary)

                # Q&A
                st.markdown("### 💬 Ask a Question")

                q_key = f"q_{i}"
                btn_key = f"btn_{i}"

                # Store question in session
                if q_key not in st.session_state:
                    st.session_state[q_key] = ""

                # Input box
                question = st.text_input(
                    f"Ask question for Paper {i+1}",
                    key=q_key
                )

                # Button
                if st.button(f"Get Answer for Paper {i+1}", key=btn_key):
                    if question.strip() == "":
                        st.warning("Please enter a question")
                    else:
                        with st.spinner("Thinking..."):
                            answer = answer_question(abstract, question)
                        st.success(answer)