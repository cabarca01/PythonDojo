import pymongo

conn = pymongo.MongoClient("localhost")
db = conn.school

query = {
    "$or": [{"name": {"$exists": False}},
            {"name": {"$exists": True, "$eq": ""}}]
}

projection = {
    "_id": 1
}

cursor = db.students.find(query, projection)

for student in cursor:
    print student.get('_id')
