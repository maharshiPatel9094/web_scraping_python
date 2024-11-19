from bs4 import BeautifulSoup
# if our HTML parser is not working theen we have to get lxml 
# import lxml 
# soup = BeaitifulSoup(contents,"lxml")

# open website file
with open("./website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents,"html.parser")

# print(soup.title)# <title>Maharshi's Personal Site</title>
# print(soup.title.name) #title -> gives the HTML tag name
# print(soup.title.string) #gives the inner string in title tag
# print(soup.prettify()) #give our website html with indented 

# getting first tag
# print(soup.a) #give first anchor tag
# print(soup.p) #give fist paragrph tag

# get all particular tag
all_anchor_tag = soup.find_all(name="a")#gives all anchor tag
# print(all_anchor_tag)

# getting text from all anchor tags 
for tag in all_anchor_tag:
    text = tag.getText() 
    # print(text)
    # get value of any desired tag
    tag = tag.get("href")
    # print(tag)
    
# finding element with particular id 
heading = soup.find(name="h1",id="name")
# print(heading)
# we did not used class because it is an reserved word
section_heading = soup.find(name="h3",class_="heading")
# print(section_heading)
# print(section_heading.string)
# print(section_heading.name)


# targetting first a tag
all_anchor_tag = soup.find_all(name="a")#gives all anchor tag
# print(all_anchor_tag)
# print(all_anchor_tag[0])
# print(all_anchor_tag[0].getText())

# give first matching item in list 
# select the anchor tag which is inside the p tag
company_url = soup.select_one(selector="p a")
# slecting with particular id
name = soup.select_one(selector="#name")

# print(company_url)
# print(name)

# selecting all tag with a particular id or class and gives us a list of that particular tag
headings = soup.select(selector=".heading")
print(headings)