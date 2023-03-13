import requests
from bs4 import BeautifulSoup

# Scrape job postings from Oracle
oracle_url = 'https://www.oracle.com/corporate/careers/job/'
oracle_response = requests.get(oracle_url)
oracle_soup = BeautifulSoup(oracle_response.content, 'html.parser')
oracle_jobs = oracle_soup.find_all('a', class_='jobtitle')

with open('oracle.txt', 'w') as f:
    for job in oracle_jobs:
        f.write(job.text.strip() + '\n')

# Scrape job postings from Twitter
twitter_url = 'https://careers.twitter.com/en/work-for-twitter/openings.html'
twitter_response = requests.get(twitter_url)
twitter_soup = BeautifulSoup(twitter_response.content, 'html.parser')
twitter_jobs = twitter_soup.find_all('h2', class_='title')

with open('twitter.txt', 'w') as f:
    for job in twitter_jobs:
        f.write(job.text.strip() + '\n')

# Scrape job postings from Google
google_url = 'https://careers.google.com/jobs/'
google_response = requests.get(google_url)
google_soup = BeautifulSoup(google_response.content, 'html.parser')
google_jobs = google_soup.find_all('h2', class_='gc-title')

with open('google.txt', 'w') as f:
    for job in google_jobs:
        f.write(job.text.strip() + '\n')

# Scrape job postings from GitHub
github_url = 'https://github.com/about/careers'
github_response = requests.get(github_url)
github_soup = BeautifulSoup(github_response.content, 'html.parser')
github_jobs = github_soup.find_all('a', class_='opening')

with open('github.txt', 'w') as f:
    for job in github_jobs:
        f.write(job.text.strip() + '\n')

# Scrape job postings from Reddit
reddit_url = 'https://www.redditinc.com/careers'
reddit_response = requests.get(reddit_url)
reddit_soup = BeautifulSoup(reddit_response.content, 'html.parser')
reddit_jobs = reddit_soup.find_all('h3', class_='job-title')

with open('reddit.txt', 'w') as f:
    for job in reddit_jobs:
        f.write(job.text.strip() + '\n')
