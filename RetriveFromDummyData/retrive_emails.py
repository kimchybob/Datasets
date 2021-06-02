import json

emails = []

with open('Resorts.json', 'r') as file:
    raw = file.read()
    content = json.loads(raw)
    [emails.append(i['Email']) for i in content if i['Email'] not in emails]

# write countrys to file
with open('output/Emails.txt', 'a') as f:
    for x in emails:
        f.write(x + "\n")