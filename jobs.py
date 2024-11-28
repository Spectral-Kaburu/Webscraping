from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python+developer&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    # description = job.find('ul', class_="list-job-dtl clearfix").text
    company_name = job.find('h3', class_='joblist-comp-name').text.replace(" ", "")
    skills = job.find('span', class_='srp-skills').text
    experience = job.find('ul', class_='top-jd-dtl clearfix').text
    description = job.header.h2.a['href']
    if "card_travel0" in experience:
        print(f"Company Name:\n{company_name.strip()}")
        print(f"Required Skills:\n{skills.strip()}")
        print(f"Experience:\n{experience.strip()}\n")
        print(f"Description:{description}\n\n")