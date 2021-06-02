import json
import random

dataset = []

with open('output/Resorts.txt', 'r') as file:
    resorts = file.read().splitlines()

num = 1
for resort in resorts:
    dataset.append({
        "model": "db.resort",
        "pk": num,
        "fields": {
            "country_id": random.choice(range(1, 74)),
            "resort_name": resort
        }
    })

    num += 1

with open("Datasets/resorts.json", 'w') as file:
    file.write(json.dumps(dataset))
