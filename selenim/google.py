from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import requests


# Chrome 드라이버 경로 설정 (chromedriver가 PATH에 있으면 생략 가능)
driver = webdriver.Chrome()

# Google 접속
driver.get("https://www.google.com/imghp?hl=ko&tab=ri&ogbl")

search_box = driver.find_element("name", "q")
search_box.click()
search_box.send_keys("애로우 잉글리시")
search_box.send_keys(Keys.RETURN)

elements = driver.find_elements(By.CLASS_NAME, ".YQ4gaf")
if elements:
    elements[0].click()

    time.sleep(2)  # 이미지가 로드될 때까지 잠시 대기

    images = driver.find_elements(By.CSS_SELECTOR, ".sFlh5c.FyHeAf")
    for img in images:
        src = img.get_attribute("src")
        print(src)

        # 이미지 저장 폴더 생성
        save_dir = "downloaded_images"
        os.makedirs(save_dir, exist_ok=True)

        # 클릭한 이미지의 큰 이미지 src 추출
        large_images = driver.find_elements(By.CSS_SELECTOR, ".n3VNCb")
        img_urls = []
        for img in large_images:
            src = img.get_attribute("src")
            if src and src.startswith("http"):
                img_urls.append(src)

        # 이미지 다운로드
        for idx, url in enumerate(img_urls):
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    ext = url.split('.')[-1].split('?')[0]
                    if ext.lower() not in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp']:
                        ext = 'jpg'
                    filename = os.path.join(save_dir, f"image_{idx}.{ext}")
                    with open(filename, "wb") as f:
                        f.write(response.content)
                    print(f"Downloaded: {filename}")
            except Exception as e:
                print(f"Failed to download {url}: {e}")

        # driver.quit()