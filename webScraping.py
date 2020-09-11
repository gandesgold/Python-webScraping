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