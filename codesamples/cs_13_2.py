import pymongo

conn = pymongo.MongoClient("localhost")
db = conn.school
students = db.students
cursor = students.find({"scores.score": {"$lt": 3.5}}, {"name": 1, "scores":1})

for doc in cursor:
    print doc