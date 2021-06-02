import json
from random import choice

dataset = []

with open('output/ImageLinks.txt', 'r') as file:
    image_links = file.read().splitlines()

for i in range(1, 500):
    dataset.append({
        "model": "db.gallery",
        "pk": i,
        "fields": {
            "user_id": choice(range(1, 249)),
            "image_link": choice(image_links)
        }
    })

with open("Datasets/gallery.json", 'w') as file:
    file.write(json.dumps(dataset))
