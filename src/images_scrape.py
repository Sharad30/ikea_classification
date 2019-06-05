import urllib.request
from bs4 import BeautifulSoup
import requests
import json
import os
import random
import shutil


def create_test_set():
    train_path = 'data/train'
    test_path = 'data/test'
    product_list = ['bed', 'chair', 'desk', 'kitchen']
    for product in product_list: 
        image_path_list = random.sample(os.listdir(f'{train_path}/{product}'), 120)
        for i, image_path in enumerate(image_path_list): 
            shutil.move(f'{train_path}/{product}/{image_path}', f'{test_path}/{i}_{product}.jpg')


def scrape_images(product_name, start, end):
    """This function will take in single product name and scrape images from ikea website
        based on the range specified from start to end.
    
    Arguments:
        product_name {string} -- name of the product for which you want to scrape images
        start {int} -- index to denote start number of image
        end {int} -- index to denote end number of image
    """

    url = f"https://w16804f45.api.esales.apptus.cloud/api/v1/panels/product-search?\
            sessionKey=695f7741-892e-4ff3-3cc2-db634b51be1c&customerKey=54fa9e75-8fdd-4af3-307f-72830c8b9e62&\
            market=INEN&arg.window_first={start}&arg.window_last={end}&arg.search_phrase={product_name}&\
            arg.sort_by=relevance%20desc&arg.catalog_root=category_catalog_inen%3A%27root%27&\
            arg.catalog_filter=type%3A%27functional%27%20OR%20type%3A%27products%27&\
            arg.nr_catalog_categories=3&arg.locale=en_IN&arg.filter=market%3A%27INEN%27"
    string = requests.get(url).content
    json_obj = json.loads(string)
    for i, product in enumerate(json_obj['mainResult'][1]['products'], start=start):
        product_id = product['key'].split('_')[0]
        last_3_digit_product_id = product_id[-3:]
        required_image_url = f"https://www.ikea.com/in/en/products/{last_3_digit_product_id}/{product_id}-compact-fragment.html"
        
        html = urllib.request.urlopen(required_image_url)
        soup = BeautifulSoup(html, "html.parser")

        imgs = soup.findAll("div", {"class":"image-claim-height"})
        for img in imgs:
            img_url = img.img['src'].split("imgurl=")[0]
            with open(f'data/train/{product_name}/{i}.jpg','wb') as f:
                f.write(requests.get(img_url).content)
                print(f"Downloaded {i} {product_name} image successfully")

if __name__ == "__main__":

    # products = ['kitchen']
    # for product in products:
    #     scrape_images(product, 1, 1353)

    create_test_set()