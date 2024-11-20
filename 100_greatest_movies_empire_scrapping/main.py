import requests
from bs4 import BeautifulSoup




WEBSITE_URL = "https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(WEBSITE_URL) #website get response 
website_html = response.text #website html


soup = BeautifulSoup(website_html,"html.parser")# soup object
# print(soup.prettify())

all_movies = soup.find_all(name="h3",class_ = "listicleItem_listicle-item__title__BfenH") #this class came while inspecting a live website
# print(all_movies) #return list of all h3 elements containing the movies 

movie_titiles = [movie.getText() for movie in all_movies]#getText dont work on list so use list comprehension
movies = movie_titiles[::-1] 
# movie_titiles.reverse() #never store it into a variable otherwise it will return none 
# print(movie_titiles) #return a list of top 100 movies

# create a new file with movie.txt and list of movies 
with open("movie.txt",mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")