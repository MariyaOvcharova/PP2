import csv

data = [
    {'first_name': 'Azriel', 'last_name': 'Tagirovich', 'phone_number': '+88005553535'},
    {'first_name': 'Lusinda', 'last_name': 'Kasatkina', 'phone_number': '+77777777777'}
]

fields = ['first_name', 'last_name', 'phone_number']

with open('num.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
