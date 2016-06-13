import urllib

html_obj = urllib.urlopen("http://www.pythonlearn.com/code/intro-short.txt")
html_data = html_obj.read()
print html_data
