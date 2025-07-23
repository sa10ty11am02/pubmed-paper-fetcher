import argparse
import os
from aganitha.fetcher import search_pubmed, fetch_details
from aganitha.filter import filter_non_academic_papers
import csv

def save_to_csv(results, filename):
    """
    Save the final filtered paper info into a CSV file.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            "PubmedID",
            "Title",
            "PublicationDate",
            "NonAcademicAuthors",
            "CompanyAffiliations",
            "CorrespondingAuthorEmail"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in results:
            writer.writerow({
                "PubmedID": row["PubmedID"],
                "Title": row["Title"],
                "PublicationDate": row["PublicationDate"],
                "NonAcademicAuthors": "; ".join(row["NonAcademicAuthors"]),
                "CompanyAffiliations": "; ".join(row["CompanyAffiliations"]),
                "CorrespondingAuthorEmail": row["CorrespondingAuthorEmail"]
            })

def main():
    parser = argparse.ArgumentParser(description="Fetch and filter PubMed papers with non-academic authors.")
    parser.add_argument("query", help="PubMed query to search for papers")
    parser.add_argument("-f", "--file", help="Output CSV file name", default="output/results.csv")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug info")

    args = parser.parse_args()

    if args.debug:
        print(f"Searching PubMed for: {args.query}")

    ids = search_pubmed(args.query, max_results=20)

    if args.debug:
        print(f"Found {len(ids)} papers")

    papers = fetch_details(ids)
    filtered = filter_non_academic_papers(papers)

    if args.debug:
        print(f"Filtered to {len(filtered)} papers with non-academic authors")

    os.makedirs(os.path.dirname(args.file), exist_ok=True)
    save_to_csv(filtered, args.file)

    print(f"✅ Results saved to: {args.file}")

if __name__ == "__main__":
    main()
