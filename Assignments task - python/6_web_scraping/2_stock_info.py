#2

import requests
from bs4 import BeautifulSoup
import pandas as pd
details1 = []
def scrap_page():
    page = 'https://finance.yahoo.com/markets/stocks/52-week-gainers/?start=0&count=100'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
    response = requests.get(page, headers=headers)
    soup = BeautifulSoup(response.text, 'html')
    stocks2 = []
    table = soup.find('table', class_="markets-table")
    
    for row in table.find_all('tr')[1:11]:
        link = row.find('a') 
        if link:
            company_code_span = link.find('span', class_="symbol")
            company_name_span = link.find('span', class_="longName")
            company_code = company_code_span.text.strip() if company_code_span else "N/A"
            company_name = company_name_span.text.strip() if company_name_span else "N/A"
        cols = row.find_all('td')
        Week_Change = cols[8].text.strip().replace(',', '').replace('%', '')
        Total_Cash = cols[6].text.strip()
            
        details1.append({
                "Name": company_name,
                "code": company_code,
                "52-week change": Week_Change,
                "Total cash": Total_Cash,
                        
                })
        
    return details1
def weekchange():
    details1 = scrap_page()
    df = pd.DataFrame(details1)
    df['52-week change'] = pd.to_numeric(df['52-week change'], errors='coerce')
    sorted_df = df.sort_values(by="52-week change", ascending=False)
    top_10 = sorted_df.head(10)
    return top_10
weekchange()




