import json

dataset = []

types = (
    "Savings Account",
    "Checking Account",
    "Retirement Account",
    "Money Market Deposit Account",
    )

num = 1
for i in types:
    dataset.append({
        "model": "db.bankaccounttype",
        "pk": num,
        "fields": {
            "type_name": i
        }
    })

    num += 1

with open("Datasets/bankaccounttypes.json", 'w') as file:
    file.write(json.dumps(dataset))
