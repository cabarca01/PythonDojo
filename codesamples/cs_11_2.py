import xml.etree.ElementTree as xmltree

fhandler = open("../data/bookstore.xml")
XMLData = fhandler.read()

tree = xmltree.fromstring(XMLData)
bookstore = tree.findall("book")
total = 0.0
for book in bookstore:
    currency = book.find("price").get("currency")
    if currency == 'EUR':
        total += float(book.find("price").text) * 1.14
    else:
        total += float(book.find("price").text)

print "Total: %.2f" % total
