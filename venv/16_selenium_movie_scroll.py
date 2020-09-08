from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

#페이지 이동
url = "https://play.google.com/store/movies?hl=kr"
browser.get(url)

import time
interval = 2 # 2초에 한번씩 내리기

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scroll(0,document.body.scrollHeight)")

    # 페이지 로딩
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height
print("스크롤 완료")