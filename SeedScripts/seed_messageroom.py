import json
import random

dataset = []

with open("Datasets/user.json", "r") as file:
    users = json.loads(file.read())

for i in range(1, 201):
    send_user = random.randint(1, len(users))
    reciver_user = random.randint(1, len(users))

    # if send_user same as reciver_user; keep changing reciver_user until it != send_user.
    while reciver_user == send_user:
        reciver_user = random.randint(1, len(users))

    dataset.append({
        "model": "db.messageroom",
        "pk": i,
        "fields": {
            "sender_user_id": send_user,
            "reciever_user_id": reciver_user,
        }
    })

with open("Datasets/messageroom.json", 'w') as file:
    file.write(json.dumps(dataset))
