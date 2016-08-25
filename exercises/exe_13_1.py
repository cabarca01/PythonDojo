import pymongo

conn = pymongo.MongoClient("localhost")
db = conn.school

query = {
    "scores.type": "homework",
    "scores.score": {
        "$gte": 0,
        "$lte": 30
    }
}

projection = {
    "name": 1,
    "scores": 1,
    "_id": 0
}

cursor = db.students.find(query, projection)

for student in cursor:
    for scores in student['scores']:
        if scores['type'] == 'homework' and 0 <= scores['score'] <= 30:
            print "%-25s %.2f" % (student['name'], scores['score'])
