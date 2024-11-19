from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

# load env variables 
load_dotenv()

# get env variables 
url = os.getenv("WEBSITE_URL")

# here we will use static website link start with https://
# if we want to do it live some things may change 

response = requests.get(url=url)
# similar to file.read() when we open the file 
hacker_webpage= response.text# soup object
soup = BeautifulSoup(hacker_webpage,"html.parser")


# getting single articles
title = soup.title# print(title)
article = soup.find(name="a",class_ = "storylink")# print(news_list)
article_text = article.getText()
article_link =article.get("href")
article_upvote = soup.find(name="span",id= "score_24129693").getText()


# getting list of articles
article_lists = []
article_links = []
article_list = soup.find_all(name="a",class_="storylink")
print(article_list)#get the list of articles
for article in article_list:
    text = article.getText()
    article_lists.append(text)
    link = article.get("href")
    article_links.append(link)


# converting pivotes to display text 
# int(article_upvote[0].split()[0]) -> give us the integer value of upvotes 

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span",class_ = "score")]

# finding the most popular article and link and point
largest_number_upvote = max(article_upvotes) #give the largest number in the upvot list 
largest_number_upvote_index = article_upvotes.index(largest_number_upvote)
print(f"Highest rated news text is {article_lists[largest_number_upvote_index]} and the link is {article_links[largest_number_upvote_index]} and points are {article_upvotes[largest_number_upvote_index]}")
