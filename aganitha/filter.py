# papers/filter.py

from typing import List, Dict

# Words that usually mean academic affiliation
ACADEMIC_KEYWORDS = ["university", "institute", "college", "school", "hospital", "centre", "center", "department", "faculty", "laboratory", "lab"]

# Words that may indicate a company
COMPANY_KEYWORDS = ["pharma", "inc", "biotech", "therapeutics", "lifesciences", "biosciences", "labs", "solutions", "genomics"]

def is_non_academic(affiliation: str) -> bool:
    """
    Returns True if the affiliation looks like it's from a company (not academic).
    """
    affiliation_lower = affiliation.lower()

    # If any academic keyword is present, consider it academic
    for word in ACADEMIC_KEYWORDS:
        if word in affiliation_lower:
            return False

    # If company keywords exist, it is non-academic
    for word in COMPANY_KEYWORDS:
        if word in affiliation_lower:
            return True

    # Otherwise unsure — treat as academic
    return False

def filter_non_academic_papers(papers: List[Dict]) -> List[Dict]:
    """
    Returns only those papers that have at least one non-academic author.
    Also attaches company affiliations and author names.
    """
    filtered = []

    for paper in papers:
        non_academic_authors = []
        companies = []

        for author in paper.get("Authors", []):
            aff = author.get("affiliation", "")
            if is_non_academic(aff):
                non_academic_authors.append(author["name"])
                companies.append(aff)

        if non_academic_authors:
            filtered.append({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "PublicationDate": paper["PublicationDate"],
                "NonAcademicAuthors": non_academic_authors,
                "CompanyAffiliations": companies,
                "CorrespondingAuthorEmail": find_corresponding_email(paper.get("Authors", []))
            })

    return filtered

def find_corresponding_email(authors: List[Dict]) -> str:
    """
    Heuristically picks the first non-empty email as the corresponding author.
    """
    for author in authors:
        email = author.get("email", "")
        if email:
            return email
    return ""
