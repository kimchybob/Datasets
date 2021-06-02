import json

dataset = []

with open('output/Countries.txt', 'r') as file:
    content = file.read().splitlines()

num = 1
for i in content:
    dataset.append({"model": "db.country",
        "pk": num,
        "fields": {
            "country_name": i
        }
    })

    num += 1

with open("Datasets/country.json", 'w') as file:
    file.write(json.dumps(dataset))
