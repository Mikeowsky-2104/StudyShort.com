from os import system, name
from bs4 import BeautifulSoup
import requests
import csv

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

page_to_scrape = requests.get("https://quotes.toscrape.com/").text
soup = BeautifulSoup(page_to_scrape, "html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)
writer.writerow(["QUOTES", "AUTHORS"])

for quote, author in zip(quotes, authors):
  print(quote.text + " - " + author.text)
  print("\n")
  writer.writerow([quote.text + " - " + author.text])
file.close()
