import json

dataset = []

catagories = (
    "First Timer Assistance",
    "Child Entertainment Services",
    "Tours",
    "Activities",
    "Virtual Lessons",
)

services = (
    (
        "First Timer Assistance",
    ),
    (
        "On Slope SnowBoarding",
        "On Slope Skiing",
        "Off Slope",
    ),
    (
        "Ski Tour Of The Slopes",
        "SnowBoard Tour Of The Slopes",
        "Walking Tour Of The Village",
        "Ebike BackCountry Touring",
        "Hiking",
    ),
    (
        "Ski BackCountry Touring",
        "SnowBoard BackCountry Touring",
        "SnowShoeing",
        "SnowMobiling",
        "Bike Riding",
    ),
    (
        "Skiing",
        "SnowBoarding",
    ),
)

num = 1
for catagory in catagories:
    for service in services[catagories.index(catagory)]:
        dataset.append({
            "model": "db.service",
            "pk": num,
            "fields": {
                "catagory_name": catagory,
                "service_name": service,
            }
        })

        num += 1

with open("Datasets/services.json", 'w') as file:
    file.write(json.dumps(dataset))
