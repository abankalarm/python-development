from bs4 import BeautifulSoup
import requests
from PIL import Image
from PIL.Image import core as _imaging
from io import Bytes10



search = input("enter search term")
params = { "q": search }
r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("cite").text

    if item_href and item_text:
        print (item_text)
        print(item_href)
        print("\n")


search1 = input("enter search term")
params1 = { "q": search }
r1 = requests.get("http://www.bing.com/search", params=params1)

soup1 = BeautifulSoup(r1.text, "html.parser")
results1 = soup1.findAll("a", {"classs": "iusc"})

for item in results1:
    img_obj = requests.get(item.attrs["href"])
    title = item.attrs["href"].split("/")[-1]
    img = Image.open(Bytes10(img_obj.content))
    img.save("./" + title, img.format)