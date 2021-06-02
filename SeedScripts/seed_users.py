import json
from faker import Faker
from passlib.hash import pbkdf2_sha256
import random
import pytz

fake = Faker()

# fake.date()
# fake.sentence()

dataset = []

genders = ('male', 'female', 'not_specified')

with open('output/Countries.txt', 'r') as file:
    countries = file.read().splitlines()

with open('output/Emails.txt', 'r') as file:
    emails = file.read().splitlines()

with open('output/PhoneNumber.txt', 'r') as file:
    phone_numbers = file.read().splitlines()

with open('output/ImageLinks.txt', 'r') as file:
    image_links = file.read().splitlines()

primary_key = 1
for user in emails:
    rand_list = []
    [rand_list.append(random.randint(1, 56)) for i in range(random.randint(1, 5))]

    dataset.append({
        "model": "db.user",
        "pk": primary_key,
        "fields": {
            "password": pbkdf2_sha256.hash(fake.first_name()),
            "last_login": str(fake.date_time(tzinfo=pytz.UTC)),
            "is_superuser": False,
            "email": user,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "bio": fake.sentence(),
            "gender": random.choice(genders),
            "dob": str(fake.date()),
            "mobile_number": random.choice(phone_numbers),
            "profile_picture": random.choice(image_links),
            "country": random.choice(range(1, 74)),
            "is_active": bool(random.getrandbits(1)),
            "skiing_level": random.choice(range(8)),
            "snowboarding_level": random.choice(range(8)),
            "signup_step": random.choice(range(1, 5)),
            "groups": [],
            "user_permissions": [],
            "languages": rand_list,
        }
    })

    primary_key += 1

with open("Datasets/user.json", 'w') as file:
    file.write(json.dumps(dataset))
