import os
import requests
from bs4 import BeautifulSoup
from newspaper import Article

# List of sources to fetch articles from
sources = [
    'https://www.npr.org/sections/news/',
    'https://www.nytimes.com/section/world',
    'https://www.bbc.com/news',
    'https://www.theguardian.com/international',
    'https://www.reuters.com/',
    # add more sources here
]

# Path to the README.md file to update
readme_path = 'README.md'

# Loop through sources and fetch latest articles
articles = []
for source in sources:
    response = requests.get(source)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles += soup.find_all('a', href=True)

# Filter articles by word count and plagiarism
filtered_articles = []
for article in articles:
    url = article['href']
    try:
        content = Article(url).text
        if len(content.split()) < 400 or len(content.split()) > 500:
            continue
        if Article(url).is_redundant():
            continue
        filtered_articles.append((article.text.strip(), url))
    except:
        continue

# Update README.md with article titles and links
if filtered_articles:
    readme = ''
    with open(readme_path, 'r') as f:
        readme = f.read()
    for article in filtered_articles:
        title, url = article
        if title not in readme:
            readme += f'\n- [{title}]({url})'
    with open(readme_path, 'w') as f:
        f.write(readme)
