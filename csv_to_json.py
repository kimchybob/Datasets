import csv
import json
from sys import argv

array = []

path = argv[1]
output_path = argv[2]

# opens csv file and makes content a list
with open(path, encoding='utf-8') as file:
    content = csv.DictReader(file)
    [array.append(i) for i in content]

# outputs list as json file
with open(output_path, 'w', encoding='utf-8') as jsonfile: 
    jsonString = json.dumps(array, indent=4)
    jsonfile.write(jsonString)