import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액_1-200.csv"
f = open(filename, "w", encoding="euc_kr", newline='')
writer = csv.writer(f)

# 웹에 있는 항목 구분을 그대로 들고옴 = 보니까 탭으로 구분되어 있음
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split(("\t"))

print(type(title))
writer.writerow(title)

for page in range(1, 2):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:   # 의미 없는 데이터 skip
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)