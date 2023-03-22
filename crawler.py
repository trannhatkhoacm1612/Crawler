# import requests
# from bs4 import BeautifulSoup
# import os

# def take_img_url(search):
#     querry = f"https://www.google.com/search?q={search}&source=lnms&tbm=isch"
#     response = requests.get(querry)
#     soup = BeautifulSoup(response.content,"html.parser")
#     img_urls = []
#     for img_tag in soup.find_all("img"):
#         try:
#             img_url = img_tag["src"]
#             if img_url.startswith("http") and not img_url.startswith("https://encrypted-tbn0.gstatic.com"):
#                 img_urls.append(img_url)
#         except KeyError:
#             pass
#     return img_urls



# def download(search,size):
#     i = 1
#     img_urls = take_img_url(search)
#     os.makedirs(search,exist_ok=True)
#     for url in img_urls:
#         response = requests.get(url)
#         with open(f'{i}.jpg', "wb") as file:
#             file.write(response.content)
#             i += 1
#         if i == size:
#             break
# download("dog",10)
import requests
from bs4 import BeautifulSoup
import os

def take_img_url(search):
    query = f"https://www.google.com/search?q={search}&source=lnms&tbm=isch"
    response = requests.get(query)
    soup = BeautifulSoup(response.content, "html.parser")
    img_urls = []
    for img_tag in soup.find_all("img"):
        try:
            img_url = img_tag["src"]
            print(img_url)
            if img_url.startswith("https"):
                img_urls.append(img_url)
        except KeyError:
            pass
    return img_urls

def download(search, size):
    i = 1
    img_urls = take_img_url(search)
    os.makedirs(search, exist_ok=True)
    for url in img_urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(os.path.join(search, f"{i}.jpg"), "wb") as file:
                file.write(response.content)
                i += 1
                if i > size:
                    break
        except requests.exceptions.HTTPError as e:
            print(f"Error downloading {url}: {e}")

download("dog",10)