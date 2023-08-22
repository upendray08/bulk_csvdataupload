import csv
from faker import Faker
import random

# Number of records to generate
num_records = 1000  # Change this to the desired number of records

# Create a Faker generator
fake = Faker()

# Generate CSV data
csv_data = []
for _ in range(num_records):
    username = fake.user_name()
    email = fake.email()
    password = fake.password()
    csv_data.append([username, email, password])

# Write CSV data to a file
csv_file_path = 'data.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['username', 'email', 'password'])  # Write header
    csv_writer.writerows(csv_data)

print(f"{num_records} CSV records generated and saved to {csv_file_path}.")
