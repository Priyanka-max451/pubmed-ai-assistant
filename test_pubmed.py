from pubmed_fetch import fetch_pubmed
from summarizer import summarize_text

papers = fetch_pubmed("diabetes")

for p in papers:
    if p["abstract"]:
        print("TITLE:", p["title"])
        print("SUMMARY:", summarize_text(p["abstract"]))
        print("------")