# main.py
import pymongo

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Database Name
dataBase = client["neurolabDB"]

# Collection Name
collection = dataBase["products"]

# Sample data
d = {
    "companyName": "Abdoul_iNeuron",
    "product": "Affordable AI Course",
    "courseOffered": "Machine Learning"
}

# Insert above records in the collection
record = collection.insert_one(d)

# Let's Verify all the records inserted with all the fields
all_record = collection.find()

# Printing all records present in the collection
for idx, record in enumerate(all_record):
    print(f"{idx}: {record}")
