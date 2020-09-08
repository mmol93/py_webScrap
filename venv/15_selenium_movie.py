import requests
from bs4 import BeautifulSoup


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
url = "https://play.google.com/store/movies/top?hl=jp"
res = requests.get(url, headers=headers)

res.raise_for_status()


soup = BeautifulSoup(res.text, "lxml")


movies = soup.find_all("div", attrs={"class":"uMConb V2Vq5e POHYmb-T8c9cb YEDFMc-T8c9cb y1APZe-T8c9cb q9QOMe"})
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

# with open("movie.html", "w", encoding='utf8') as f:
#     f.write(soup.prettify()) #html 파일을 보기쉽게 표기