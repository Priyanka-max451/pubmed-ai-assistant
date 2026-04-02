from Bio import Entrez

Entrez.email = "your_email@gmail.com"  # put your email

def fetch_pubmed(query, max_results=1):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    ids = record["IdList"]

    papers = []

    for pubmed_id in ids:
        fetch = Entrez.efetch(db="pubmed", id=pubmed_id, retmode="xml")
        data = Entrez.read(fetch)

        article = data['PubmedArticle'][0]['MedlineCitation']['Article']
        title = article.get('ArticleTitle', '')

        abstract = ""
        if 'Abstract' in article:
            abstract = " ".join(article['Abstract']['AbstractText'])

        papers.append({
            "title": title,
            "abstract": abstract
        })

    return papers