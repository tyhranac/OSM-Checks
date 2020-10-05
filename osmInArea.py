import csv
import datetime
import json
import requests
import time

overpass_url = "http://overpass-api.de/api/interpreter"

# returns all national forest service ways/relations in WA
area_query = """
[out:json]
area["ISO3166-2"][admin_level=4];
wr[boundary=national_park](area);
out meta;
>;
out skel qt;
"""

park_request = requests.get(overpass_url, params={"data":area_query})

try:
    airport_req.raise_for_status()
except Exception as X:
    print("Request failed: {}".format(X))

park_data = park_request.json()

area_ids = {}

for element in park_data["elements"]:
    if element["type"] == "way":
        way_id = element["id"]
        area_id = int(way_id) + 2400000000
        name = element["tags"]["name"]
        area_ids.setdefault(name, area_id)
    elif element["type"] == "relation":
        rel_id = element["id"]
        area_id = int(rel_id) + 3600000000
        name = element["tags"]["name"]
        area_ids.setdefault(name, area_id)

features = {}

for k, v in area_ids.items():
    feature_query = """
    [out:json]
    node[natural=tree](area{});
    out meta;
    >;
    out skel qt;
    """.format(v)

    feature_req = requests.get(overpass_url, params={"data":featured_query})

    try:
        feature_req.raise_for_status()
    except Exception as X:
        print("Request failed: {}.\nWaiting one minute to retry...\n".format(X))
        time.sleep(60)
        feature_req = requests.get(overpass_url, params={"data":featured_query})

    
