import json

image_links = []

with open('json/Resorts-legacy.json', 'r') as file:
    raw = file.read()
    content = json.loads(raw)
    [image_links.append(i['image']) for i in content if i['image'] not in image_links]

# write countrys to file
with open('output/ImageLinks.txt', 'a') as f:
    for x in image_links:
        f.write(x + "\n")