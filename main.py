from bs4 import BeautifulSoup
import requests

url = f"https://dev-korea.com/jobs"

page = requests.get(url)

soup = BeautifulSoup(page.text, "lxml")

jobs = soup.find("ul", class_="sc-bc0cf642-2 dghzaJ")

for job in jobs:
    title = job.find("p", class_="sc-d108aa72-7 kNJcyb")
    company = job.find("p", class_="sc-d108aa72-9 kCTOJP")
    
    if job.find("a", {"class" : "sc-d108aa72-12 drsGft"}) is not None:
        job_posting = job.find("a", {"class" : "sc-d108aa72-12 drsGft"}).get("href", None)
    elif job.find("a", {"class" : "sc-d108aa72-6 rFA-dA"}) is not None: # This is for when the company doesnt have a specific application process
        job_posting = url[:-5] + job.find('a', {'class' : 'sc-d108aa72-6 rFA-dA'}).get('href', None)
    else:
        job_posting = None

    job_info = {"Title" : title.text, "Company" : company.text, "Job Posting" : job_posting}
    
    print(job_info)

