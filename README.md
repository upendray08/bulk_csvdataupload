# Bulk CSV Data Upload into MongoDB Database using Python

This guide provides step-by-step instructions on how to upload bulk CSV data into a MongoDB database using Python. This approach is particularly useful when you have a large amount of data to import.

## Prerequisites

- Python 3.x installed on your system.
- MongoDB installed and running.
- `pymongo` Python library installed. You can install it using: `pip install pymongo`.
-  `faker` python library installed . you can install it using: `pip install faker`
## Steps

1. **Prepare Your CSV Data**

   Ensure your CSV data is properly formatted and that the columns match the structure you want in the MongoDB collection.
   e.g(username,email,password) are the three columns in csv file 
2. **Create a Python Script**
   Create a python script (e.g. , `csv_fake_data_generator.py` to generate the fake (user,email,password) thousand of data.
   Create a Python script (e.g., `upload_csv_to_mongodb.py`) to handle the data upload process.
3. **Import Required Libraries**

   In your Python script, import the necessary libraries:

   ```python
   import csv
   from pymongo import MongoClient
   from faker import Faker
4. **How to setup and start This project in your local computer:**
   ```sh
   git clone https://github.com/your-username/your-project.git
   cd your-project
4. **Ensure MongoDB is running**
   Make sure that MongoDB is running locally
5. **generate csv data:**
   ```sh
   python csv_fake_data_generator.py
6. **upload csv data:**
   ```sh
   python upload_csv_to_mongodb.py
7. **New Changes Introduce in readme.md**
   here is changes
