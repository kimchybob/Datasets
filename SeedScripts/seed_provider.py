import json
from random import randint, getrandbits
from faker import Faker

fake = Faker()

dataset = []

with open("Datasets/services.json", "r") as file:
    services = json.loads(file.read())

with open("Datasets/resorts.json", "r") as file:
    resorts = json.loads(file.read())

with open("Datasets/suitablefor.json", "r") as file:
    suitablefor = json.loads(file.read())

num = 1
for provider in range(1, 249):

    rand_services = []
    for i in range(randint(1, 10)):
        service = randint(1, len(services))
        if service not in rand_services:
            rand_services.append(service)

    rand_resorts = []
    for i in range(randint(1, 5)):
        resort = randint(1, len(resorts))
        if resort not in rand_resorts:
            rand_resorts.append(resort)

    rand_suitablefor = []
    for i in range(randint(1, 5)):
        _suitablefor = randint(1, len(suitablefor))
        if _suitablefor not in rand_suitablefor:
            rand_suitablefor.append(_suitablefor)

    if bool(getrandbits(1)):
        dataset.append({
            "model": "db.provider",
            "pk": num,
            "fields": {
                "user_id": provider,
                "provider_bio": fake.sentence(),
                "services": rand_services,
                "suitable_for": rand_suitablefor,
                "resorts": rand_resorts,
            }
        })

        num += 1

with open("Datasets/providers.json", 'w') as file:
    file.write(json.dumps(dataset))
