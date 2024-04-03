# PythonJobScraper (IN PROGRESS)

Description

    This Python script is designed to scrape job listings from the website https://dev-korea.com/jobs. It utilizes the libraries Requests and BeautifulSoup for HTML parsing.

Current Functionality

    Fetches HTML content from the target URL.
    Parses the HTML to locate the relevant job listing section.
    Extracts the following data for each job:
        Job Title
        Company Name
        Job Posting Link (if available)

Important Notes

    This project is incomplete. It demonstrates the basic structure and initial functionality but requires further development to be fully operational.
    Some job postings may link directly to the application page, while others link to the company website in general. The script attempts to handle both scenarios.

Usage (Current State)

    Ensure you have Python 3 installed.
    Install the required libraries: pip install requests beautifulsoup4
    Run the script: python main.py

Expected Output

    The script will print a series of dictionaries to the console, each containing extracted job information.