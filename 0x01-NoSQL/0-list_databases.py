#!/usr/bin/env python3

from pymongo import MongoClient

# Connect to the MongoDB instance
client = MongoClient()

# Get the list of all databases
dbs = client.list_database_names()

# Print the databases
print("Databases:")
for db in dbs:
    print(db)
