from bs4 import BeautifulSoup
import requests
import pandas as pd

data = []
page = requests.get('https://scrapethissite.com/pages/simple/')
soup = BeautifulSoup(page.content, 'html.parser')

country = soup.find_all('div', class_='col-md-4 country')

for c in country:
        country = c.find('h3', class_='country-name').text
        capital = c.find('span', class_='country-capital').text
        population = c.find('span', class_='country-population').text
        area = c.find('span', class_='country-area').text

        data.append({
            'Country': country,
            'Capital': capital,
            'Population': population,
            'Area': area
        })

df = pd.DataFrame(data)

df.to_csv('country.csv', index=False, encoding="utf-8")
>>>>>>> update file
