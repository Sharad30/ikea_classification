import urllib.request
from bs4 import BeautifulSoup
import requests

def download_image(image_url):
        local_filename = image_url.split('/')[-1].split("?")[0]

        with open(local_filename, 'wb') as f:
            f.write(chunk)

def scrape_images()
    url = "https://www.ikea.com/in/en/cat/armchairs-chaise-longues-16239/"
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    imgs = soup.findAll("div", {"class":"image-claim-height"})
    for i, img in enumerate(imgs, start=1):
        img_url = img.img['src'].split("imgurl=")[0]
        with open(f'../data/images/{i}.jpg','wb') as f:
            f.write(requests.get(img_url).content)
        break