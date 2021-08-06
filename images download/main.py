from bs4 import *
import requests
import  os
def folder_create(images):
    try:
        folder_name = input("enter the folder name")
        os.mkdir(folder_name)
    except:
        print("folder exist with that name")
        folder_create()
    download_images(images, folder_name)

def download_images(images,folder_name):
    count = 0
    print(f"Total {len(images)} Image Found")
    if len(images) != 0:
        for i , image in enumerate(images):
            try:
                image_link = image["data_srcset"]
            except:
                try:
                    image_link = image["data_src"]
                except:
                    try:
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]
                        except:
                            pass
            try:
                r = requests.get(image_link).content
                try:
                    r = str(r,"utf-8")
                except UnicodeDecodeError:
                    with open(f"{folder_name}/images{i+1}.jpg","wb+") as f:
                        f.write(r)
                    count += 1
            except:
                pass
        if count == len(images):
            print("All images downloaded")
        else:
            print(f"total{count} Images downloaded out of len{len(images)}")

def main(url):
    r =requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    images = soup.findAll("img")
    folder_create(images)
url = input("Enter URL:-")
main(url)