import os
import requests
from bs4 import BeautifulSoup
import telegram

# Telegram bot token
bot_token = os.environ['BOT_TOKEN']

# Telegram chat ID
chat_id = os.environ['CHAT_ID']

# Google job page URL
url = "https://careers.google.com/jobs/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML response using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the links to the job postings
job_links = []
for job in soup.find_all('div', {'class': 'gc-card'}):
    link = job.find('a')
    if link:
        job_links.append(link['href'])

# Create a Telegram bot instance
bot = telegram.Bot(token=bot_token)

# Send the job links to the Telegram chat
if len(job_links) > 0:
    message = "New job postings:\n" + "\n".join(job_links)
    bot.send_message(chat_id=chat_id, text=message)
else:
    bot.send_message(chat_id=chat_id, text="No new job postings.")
