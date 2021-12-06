from bs4 import BeautifulSoup
import csv
import os


print(os.getcwd())
os.chdir("C:\\Users\\user\\Downloads\\assignments\\Module 10")
os.getcwd()


with open('index.html') as content:
    soup = BeautifulSoup(content, 'lxml')


all_articles = soup.find_all('div', class_='post')


csv_file = open('scraped_data.csv', 'w+', newline='')
writer = csv.writer(csv_file)


writer.writerow(['Headline', 'Link', 'Summary'])


for article in all_articles:
    headline = article.h3.a.text
    link = article.h3.a["href"]
    link = 'http://localhost:3000/{0}'.format(link)
    summary = article.p.text
    writer.writerow([headline, link, summary])
    

csv_file.close()

