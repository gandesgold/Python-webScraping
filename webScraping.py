<<<<<<< HEAD
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/Users/gandes.goldestan/Downloads/chromedriver")

books=[]
ratings=[]
#scores=[]
#votes=[]

driver.get("<a href="https://www.goodreads.com/list/show/7616.Motivational_and_Self_Improvement_Books"https://www.goodreads.com/list/show/7616.Motivational_and_Self_Improvement_Books</a>)

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class':'tableList js-dataTooltip'});
    book=a.find('div', attrs={'class':'bookTitle'})
    rating=a.find('div', attrs={'class':'minirating'})
    #score=a.find('div', attrs={'class':''})
    #vote=a.find('div', attrs={'class':''})
    books.append(name.text)
    ratings.append(name.text)
    #scores.append(name.text)
    #votes.append(name.text)

    df=pd.DataFrame({'Book Name':books, 'Ratings':ratings, 'Scores':scores, 'Votes':votes})
    df.to_csv('books.csv', index=False, encoding='utf-8')
=======
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
