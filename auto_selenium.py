from selenium import webdriver
import urllib.request
import time

# tim gi nhap day
image_tag = ""
image_num = 1000
driver = webdriver.Chrome()

driver.get("https://www.google.com.vn/imghp")

search_box = driver.find_element_by_name("q")
search_box.send_keys(image_tag)
search_box.submit()

image_urls = []
while len(image_urls) < image_num:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    images = driver.find_elements_by_css_selector(".rg_i")
    for image in images:
        image_url = image.get_attribute("src")
        if image_url.startswith("http") and not image_url.startswith("https://encrypted-tbn0.gstatic.com"):
            image_urls.append(image_url)
    image_urls = list(set(image_urls))

for i, image_url in enumerate(image_urls[:1000]):
    urllib.request.urlretrieve(image_url, f"image_{i}.jpg")

driver.quit()
