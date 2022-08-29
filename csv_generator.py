import csv
import random
import string

rows = [
    ['first_name', 'last_name', 'phone_number', 'stocks', ]
]

limit = int(1e6)


def rand_slug():
    len = random.randint(8, 20)
    return ''.join(random.choice(string.ascii_letters) for _ in range(len))


def rand_phone_number():
    return ''.join(random.choice(string.digits) for _ in range(10))


for _ in range(limit):
    rows.append([
        rand_slug(), rand_slug(), rand_phone_number(), random.randint(0, int(1e6))
    ])

with open('sample.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

