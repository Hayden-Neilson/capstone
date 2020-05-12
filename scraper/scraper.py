from flask import Flask, render_template
import requests
import psycopg2
import sys
import bs4
from bs4 import BeautifulSoup
from inflection import titleize


import pandas as pd 
import time
import urllib.request
from bs4 import BeautifulSoup


conn = psycopg2.connect(
            dbname = "Capstone",
            user = "postgres",
            password = "Hneilson1",
            host = "localhost"
)

cur = conn.cursor()







URL = "https://www.indeed.com/jobs?q=junior+web+developer&l=utah"   

soup = BeautifulSoup(urllib.request.urlopen(URL).read(), 'lxml')

results = soup.find_all('div', attrs={'data-tn-component': 'organicJob'})



for suggestion in results:


    job = suggestion.find('a', attrs={'data-tn-element': "jobTitle"})
    if job:
        print('job:', job.text.strip())

    company = suggestion.find('span', attrs={"class":"company"})
    if company:
        print('company:', company.text.strip() )

    salary = suggestion.find('span',attrs={"class":"salaryText"})
    if salary:
        print("salaryText:", salary.text.strip())

    location = suggestion.find(attrs={'span':"location accessible-contrast-color-location"})
    if location:
        print("location:", location.text.strip())
        



        cur.execute("""INSERT INTO scraped_info (job, company, salary, location) VALUES('{}', '{}', '{}', '{}');""".format(job.text.strip(),(company.text.strip(), (salary.text.strip(), (location.text.strip() )),

        conn.commit()
        cur.close()

conn.close()