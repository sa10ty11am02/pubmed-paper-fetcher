# Aganitha Paper Fetcher
This is a submission for the Aganitha take-home exercise.

# 📄 Project: get-papers-list

A Python command-line tool that fetches research papers from **PubMed** based on a user-defined query, filters papers that have at least one **non-academic author** affiliated with a **pharmaceutical or biotech company**, and outputs the results to a CSV file.

---

## 🧱 Project Structure

.
├── src/
│   ├── get_papers/
│   │   ├── __init__.py
│   │   ├── fetcher.py          # Handles API calls to PubMed
│   │   ├── filters.py          # Applies heuristics to identify non-academic authors
│   │   ├── utils.py            # Utility functions (email parsing, affiliations, etc.)
│   │   └── cli.py              # CLI logic using argparse
├── tests/
│   ├── test_fetcher.py
│   ├── test_filters.py
│   └── test_utils.py
├── README.md
├── pyproject.toml              # Poetry configuration
└── poetry.lock


---

## ⚙️ Installation

Make sure Python 3.8+ and [Poetry](https://python-poetry.org/docs/#installation) are installed.

```bash
git clone https://github.com/<your-username>/get-papers-list.git
cd get-papers-list
poetry install

poetry run get-papers-list "<your PubMed query>" [options]
-h or --help → Show help.

-d or --debug → Show debug logs.

-f filename.csv or --file filename.csv → Output to CSV. If not provided, prints to console.

poetry run get-papers-list "cancer AND treatment" -f results.csv

poetry run pytest

🔍 How It Works
Fetches papers using PubMed's E-Utilities API.

Filters:

Authors with non-academic emails (not ending in .edu, .ac, .gov)

Affiliations containing terms like Pharma, Inc., Ltd., Biotech, etc.

Extracts data:

Title, PubMed ID, Publication Date

Authors + their affiliations

Corresponding Author Email

Exports the filtered results to a CSV.

🛠 Tech Stack
Python

Poetry

argparse (CLI)

Pytest (Testing)

Requests / HTTPX (API Calls)

Typing / Pydantic (optional, for structure)

📦 Publishing (Optional)
To install from TestPyPI:

bash
Copy
Edit
pip install --index-url https://test.pypi.org/simple/ get-papers-list

📄 License
MIT License

🙏 Acknowledgments
PubMed for their API and datasets

OpenAI ChatGPT for structure suggestions

Python community tools and packages

Built with ♥ by Satyam Maurya



