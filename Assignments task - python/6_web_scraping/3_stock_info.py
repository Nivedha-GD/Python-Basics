#3

import requests
from bs4 import BeautifulSoup


profile_page = f'https://finance.yahoo.com/quote/BLK/holders/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
response = requests.get(profile_page, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')


with open("webpage_content.txt", "w", encoding="utf-8") as file:
    file.write(response.text)

print("HTML content saved to webpage_content.txt")
import pandas as pd
from bs4 import BeautifulSoup

with open("webpage_content.txt", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

table_section = soup.find('section', {'data-testid': 'holders-top-institutional-holders'})

table = table_section.find('table')

headers = [header.text for header in table.find_all('th')]

rows = []
for row in table.find_all('tr')[1:]:  
    columns = row.find_all('td')
    rows.append([col.text.strip() for col in columns])

df = pd.DataFrame(rows, columns=headers)

df
