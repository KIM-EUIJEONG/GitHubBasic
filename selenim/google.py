from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Chrome 드라이버 경로 설정 (chromedriver가 PATH에 있으면 생략 가능)
driver = webdriver.Chrome()

# Google 접속
driver.get("https://www.google.com/imghp?hl=ko&tab=ri&ogbl")


# 브라우저를 닫으려면 아래 코드 사용
# driver.quit()