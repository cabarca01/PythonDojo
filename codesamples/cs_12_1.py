import json
import urllib

address = raw_input("Enter Location: ")
url = "http://python-data.dr-chuck.net/geojson?"

service_url = url + urllib.urlencode({"sensor": "false", "address": address})
print("Retrieving %s" % service_url)

try: response = json.loads(urllib.urlopen(service_url).read())
except: response = None

if response is None or response.get("status") != "OK":
    print("Failed to obtain information from service")
else:
    print("Address:  %s" % response["results"][0]["formatted_address"])
