import csv
from pymongo import MongoClient

# MongoDB connection settings
mongo_uri = "mongodb://localhost:27017"  # Update with your MongoDB URI
db_name = "UserData"  # Update with your database name
collection_name = "users"  # Update with your collection name

# Establish MongoDB connection
client = MongoClient(mongo_uri)
db = client[db_name]
collection = db[collection_name]

# Read CSV and insert and also update if already inserted same data data into MongoDB
with open('./data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        user_data = {
            "user": row["username"],
            "email": row["email"],
            "password": row["password"]
        }
        
        # Define a query to find existing user by email
        query = {"email": user_data["email"]}
        
        # Use update_one with upsert to handle duplicates
        collection.update_one(query, {"$set": user_data}, upsert=True)

# Close the MongoDB connection
client.close()

print("CSV data uploaded to MongoDB successfully.")
