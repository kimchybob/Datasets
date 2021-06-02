import json

dataset = []

types = (
    "Mastercard",
    "Visa",
    )

num = 1
for i in types:
    dataset.append({
        "model": "db.cardtype",
        "pk": num,
        "fields": {
            "type_name": i
        }
    })

    num += 1

with open("Datasets/cardtype.json", 'w') as file:
    file.write(json.dumps(dataset))
