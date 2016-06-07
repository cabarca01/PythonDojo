import xml.etree.ElementTree as xmltree

fhandler = open("../data/bookstore.xml")
XMLData = fhandler.read()

tree = xmltree.fromstring(XMLData)
book = tree.find("book")

print "Title : %s" % book.find("title").text
print "Author: %s" % book.find("author").text
print "Price : %s %.2f" % (book.find("price").get("currency"), float(book.find("price").text))
