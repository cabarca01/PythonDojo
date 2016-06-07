import json

fhandler = open("../data/bookstore.json")
JSONData = fhandler.read()

js = json.loads(JSONData)
total = 0.0
for item in js:
    currency = item["price"]["currency"]
    if currency == 'EUR':
        total += float(item.get("price").get("price")) * 1.14
    else:
        total += float(item.get("price").get("price"))

print "Total: %.2f" % total
