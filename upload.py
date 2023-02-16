import requests

def download_image_bad(data):
    if "pages" in data["query"]:
        pages = data["query"]["pages"]
        for page in pages:
            image_url = pages[page]["imageinfo"][0]["url"]
            response = requests.get(image_url)

            with open(f"images/{page}.jpg", "wb") as f:
                f.write(response.content)
                #print(response.content)

    else:
        print("url is fake")