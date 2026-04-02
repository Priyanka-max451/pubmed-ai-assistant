from Bio import Entrez

Entrez.email = "priyankakuradagi@gmail.com"

def fetch_pubmed(query, max_results=3):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    ids = record["IdList"]

    papers = []

    for pubmed_id in ids:
        handle = Entrez.efetch(db="pubmed", id=pubmed_id, rettype="abstract", retmode="text")
        data = handle.read()

        lines = data.split("\n")
        title = lines[0] if lines else "No title"
        abstract = " ".join(lines[1:]) if len(lines) > 1 else "No abstract available"

        papers.append({
            "title": title,
            "abstract": abstract
        })

    return papers
