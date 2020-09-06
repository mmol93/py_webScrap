import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

for i in range(1, 6):

    print("페이지:", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all('li', attrs={"class":re.compile("^search-product")})

    for item in items:
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print("<****광고상품임*****>")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()
        # 애플 제품 제외
        if "Apple" in name:
            # print("<Apple 제품 제외>")
            continue
        price = item.find("strong", attrs={"class":"price-value"}).get_text()


        rating = item.find("em", attrs={"class":"rating"})
        if rating:
            rate = rating.get_text()
        else:
            # print("*****평점 없는 상품******")
            continue
        rating_count = item.find("span", attrs={"class":"rating-total-count"})
        if rating_count:
            rating_count = rating_count.get_text()
            rating_count = rating_count[1:-1]
        else:
            # print("*****평점수 없는 상품******")
            continue
        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        # 리뷰 50개 이상, 평점 4.5 이상,
        if float(rate) >= 4.5 and int(rating_count) >= 50 :
            # print(name, price, rate, rating_count)
            print("제품명: {}".format(name))
            print("가격: {}".format(price))
            print("평점: {}점 {}개".format(rate,rating_count))
            print("바로가기: {}".format("https://www.coupang.com"+link))
            print("-"*20) # 제품별 구분선