import json

countries = []

with open('Resorts.json', 'r') as file:
    raw = file.read()
    content = json.loads(raw)
    [countries.append(i["Country"]) for i in content if i["Country"] not in countries]

# write countrys to file
with open('output/Countries.txt', 'a') as f:
    for x in countries:
        f.write(x + "\n")