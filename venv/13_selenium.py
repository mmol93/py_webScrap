from selenium import webdriver
import time

browser = webdriver.Chrome("D:/Python/pyWebScrap2/venv/chromedriver.exe")

# 1. 네이버 이동
browser.get("https://naver.com")

# 2. 로그인 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pass")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)
#5. id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("pw").clear()
browser.find_element_by_id("id").send_keys("new_naver_id")
browser.find_element_by_id("pw").send_keys("naver_pass")

browser.quit()