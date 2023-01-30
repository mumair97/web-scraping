## Automating Web Scraping using Python Script
## automatically scrapes the data from the website and stores it in the database
# no need to run the vscode each time to scrap the data

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.coingecko.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

## find the target data
## find the first div with class coingecko-table
results = soup.find("div", {"class": "coingecko-table"}).find("tbody").find_all("tr") ## returns the first div with class coingecko-table


names = []
price = []
volume_24h = []
mkt_cap = []

for result in results:
    try:
        names.append(result.find("span", {"class": "lg:tw-flex font-bold tw-items-center tw-justify-between"}).get_text().strip())
    except:
        names.append("n/a")
    
    try:
        price.append(result.find("span", {"class": "no-wrap"}).get_text().strip())
    except:
        names.append("n/a")
        
    try:
        volume_24h.append(result.find("td", {"class": "td-liquidity_score lit text-right col-market"}).get_text().strip())
    except:
        volume_24h.append("n/a")
        
    try:
        mkt_cap.append(result.find("td", {"class": "td-market_cap cap col-market cap-price text-right"}).get_text().strip())
    except:
        mkt_cap.append("n/a")
        
        
# create a dataframe from the lists
# dictionary {key:value} of lists 
df_2 = pd.DataFrame({"Coin": names, "price": price, "24h_volume": volume_24h, "Market_Cap": mkt_cap})

# data frame to csv
df_2.to_csv("crypto_2.csv", index=False)