from bs4 import BeautifulSoup
import requests

date = input("What Year would you like to travel in ?? Write the date in this format ('YYYY-MM-DD'). ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"} #header
url = "https://www.billboard.com/charts/hot-100/" + date
# print(url)

response = requests.get(url=url,headers=header) #get response 
wensite_html = response.text #coverting to html

soup = BeautifulSoup(wensite_html,"html.parser") #soup object
# print(soup)

song_names_spans = soup.select("li ul li h3")
# print(song_names_spans)
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names) #return a list of all movies 