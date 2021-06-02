import json
import random
from faker import Faker

fake = Faker()

dataset = []

with open("Datasets/messageroom.json", "r") as file:
    message_rooms = json.loads(file.read())

for i in range(1, 1000):
    message_room = random.choice(message_rooms)

    message_room_id = message_room['pk']
    send_user_id = message_room['fields']['sender_user_id']

    dataset.append({
        "model": "db.message",
        "pk": i,
        "fields": {
            "user_id": send_user_id,
            "message_room_id": message_room_id,
            "message_content": fake.sentence(),
            "created_time": str(fake.date_time()),
        }
    })

with open("Datasets/messages.json", 'w') as file:
    file.write(json.dumps(dataset))
