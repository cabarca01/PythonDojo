import pymongo

conn = pymongo.MongoClient("localhost")
db = conn.school

query = {
    "name": {"$regex": "^M"}
}

projection = {
    "name": 1,
    "_id": 0
}

cursor = db.students.find(query, projection)

for student in cursor:
    print student.get('name')
