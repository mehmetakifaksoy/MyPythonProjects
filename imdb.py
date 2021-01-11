import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("tbody", {"class":"lister-list"}).find_all
print(html)


for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    
    year = tr.find("td",{"class":"titleColoum"}).find("span").text
    rating = tr.find("td",{"class":"titleColoum imdbdRating"}).text
    count+=1

    print(f"{count}- film : {title} yıl: {year} değerlendirme : {rating"})


