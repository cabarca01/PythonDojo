import pymongo

conn = pymongo.MongoClient("localhost")
db = conn.school
students = db.students
cursor = students.find({"name": "Marcus Blohm"}, {"name": 1, "scores.score": 1})

for doc in cursor:
    print doc
