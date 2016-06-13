import urllib
from bs4 import BeautifulSoup

url = "http://python-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
a_tags = soup("a")

print a_tags[2].get("href", None)
