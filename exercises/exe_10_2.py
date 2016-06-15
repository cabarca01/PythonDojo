import urllib
from bs4 import BeautifulSoup

html_doc = urllib.urlopen("http://python-data.dr-chuck.net/comments_208240.html").read()

parsedHtml = BeautifulSoup(html_doc, "html.parser")
tabledata = parsedHtml.find_all("td")

name = None
comments = None
table = list()

for data in tabledata:
    if data.span is not None:
        comments = data.span.string
    else:
        name = data.string

    if name is not None and comments is not None:
        table.append((int(comments), name))
        name = None
        comments = None

table.sort(reverse=True)

count = 0
for comment, name in table:
    print "%-15s %d" % (name, comment)
    count += 1
    if count == 10:
        break
