import json
import os
from faker import Faker

# Initialize Faker
fake = Faker()

# Create a directory to store JSON files if it doesn't exist
os.makedirs("json_files", exist_ok=True)

# Function to generate random data for a person
def generate_person():
    name = fake.first_name()
    last_name = fake.last_name()
    city = fake.city()
    address = fake.address().replace("\n", ", ")
    return {"name": name, "last_name": last_name, "city": city, "address": address}

# Create 100 JSON files
for i in range(1, 201):
    person_data = generate_person()
    filename = f"small_file_problem/person_{i}.json"
    with open(filename, "w") as json_file:
        json.dump(person_data, json_file, separators=(',', ':'))
        json_file.write('\n')  # Add newline after each JSON object
    print(f"Generated {filename}")

print("All files generated successfully.")
