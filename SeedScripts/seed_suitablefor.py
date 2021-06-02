import json

dataset = []

suitable_for = (
    "Toddlers / 3-5yo",
    "Kids / 6-12yo",
    "Teens / 13-17yo",
    "Adult / 18-64yo",
    "Senior / 65+",
)

num = 1
for i in suitable_for:
    dataset.append({
        "model": "db.suitablefor",
        "pk": num,
        "fields": {
            "suitable_for": i
        }
    })

    num += 1

with open("Datasets/suitablefor.json", 'w') as file:
    file.write(json.dumps(dataset))
