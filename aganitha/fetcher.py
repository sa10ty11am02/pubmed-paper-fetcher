# papers/fetcher.py

from typing import List, Dict, Any
from Bio import Entrez
import xml.etree.ElementTree as ET

# PubMed API requires an email to identify the requester
Entrez.email = "satyammaurya9444@gmail.com"  # ✅ Always use your real email

def search_pubmed(query: str, max_results: int = 10) -> List[str]:
    """
    Search PubMed for the given query and return a list of PubMed IDs.
    """
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    results = Entrez.read(handle)
    handle.close()
    return results["IdList"]

def fetch_details(pubmed_ids: List[str]) -> List[Dict[str, Any]]:
    """
    Fetch detailed information for a list of PubMed IDs.
    """
    ids = ",".join(pubmed_ids)
    handle = Entrez.efetch(db="pubmed", id=ids, retmode="xml")
    records = Entrez.read(handle)
    handle.close()

    papers = []

    for article in records['PubmedArticle']:
        try:
            article_data = article['MedlineCitation']['Article']
            pubmed_id = article['MedlineCitation']['PMID']
            title = article_data.get('ArticleTitle', '')
            pub_date = article_data.get('Journal', {}).get('JournalIssue', {}).get('PubDate', {})
            date = f"{pub_date.get('Year', '')}-{pub_date.get('Month', '')}"

            authors = article_data.get('AuthorList', [])
            author_info = []
            for author in authors:
                if 'AffiliationInfo' in author:
                    aff = author['AffiliationInfo'][0].get('Affiliation', '')
                    name = f"{author.get('ForeName', '')} {author.get('LastName', '')}"
                    email = extract_email(aff)
                    author_info.append({
                        "name": name,
                        "affiliation": aff,
                        "email": email
                    })

            papers.append({
                "PubmedID": pubmed_id,
                "Title": title,
                "PublicationDate": date,
                "Authors": author_info
            })

        except Exception as e:
            print(f"Error processing article: {e}")

    return papers

def extract_email(affiliation: str) -> str:
    """
    Extracts email from the affiliation string if present.
    """
    import re
    match = re.search(r'[\w\.-]+@[\w\.-]+', affiliation)
    return match.group(0) if match else ''
