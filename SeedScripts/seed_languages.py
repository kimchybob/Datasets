import json

dataset = []

with open('output/languages.txt', 'r') as file:
    content = file.read().splitlines()

num = 1
for i in content:
    dataset.append({
        "model": "db.language",
        "pk": num,
        "fields": {
            "language": i
        }
    })

    num += 1

with open("Datasets/language.json", 'w') as file:
    file.write(json.dumps(dataset))
