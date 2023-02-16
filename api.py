import requests
from PIL import Image
import shutil
import urllib.request
import os

def get_images(bird_name):

    url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&uselang=en&generator=search&gsrsearch=filetype:bitmap%7Cdrawing%20-fileres:0%20%7B{bird_name}%7D&gsrlimit=50&gsroffset=1&gsrinfo=totalhits%7Csuggestion&gsrprop=size%7Cwordcount%7Ctimestamp%7Csnippet&prop=info%7Cimageinfo%7Centityterms&inprop=url&gsrnamespace=6&iiprop=url%7Csize%7Cmime&iiurlheight=180&wbetterms=label"
    headers = {'User-Agent': 'VSCode/1.70.2 (https://lhs.fuhsd.org//; sanya.badhe@gmail.com)'}

    response = requests.get(url, headers)

    return response.json()

def get_image_link(data):
    links = []
    for page in data['query']['pages'].items():
        imageinfo = page.get('imageinfo', [])
        for info in imageinfo:
            if "upload.wikimedia.org" in info.get('url', ""):
                links.append(info['url'])
    return links


def download_image(links, bird_name):
    for i, link in enumerate(links):
        r = requests.get(link).content
        with open(f"images/{bird_name}_{i}.jpg", "wb+") as handler:
            handler.write(r)
>>>>>>> 9de96587851ab5ab459c93fcd1f882458184e31b



bird_name = "emu"
data = get_images(bird_name)
links = get_image_link(data)
download_image(links, bird_name)
