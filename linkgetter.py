import api

with open('birdlist.txt', 'r') as file:
    for line in file:
        bird_name = line.strip()
        # get image links for current bird
        data = api.get_images(bird_name)
        links = api.get_image_link(data)
        # create new file for current bird in links directory
        filename = f"links/{bird_name}.txt"
        with open(filename, 'w') as bird_file:
            for link in links:
                bird_file.write(link + '\n')