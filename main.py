import os
import requests
import csv
from datetime import datetime

ACCESS_TOKEN = os.getenv('FB_ACCESS_TOKEN')
PAGE_ID = '251848534689069'
LOG_FILE = 'follower_count_log.csv'

def fetch_follower_count():
    url = f'https://graph.facebook.com/v12.0/{PAGE_ID}?fields=followers_count&access_token={ACCESS_TOKEN}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('followers_count', None)
    else:
        print(f'Error fetching data: {response.status_code}')
        return None

def log_follower_count(count):
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, count])

if __name__ == '__main__':
    count = fetch_follower_count()
    if count is not None:
        log_follower_count(count)
