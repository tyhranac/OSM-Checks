from xml.dom.minidom import parse
import xml.dom.minidom
import math
import matplotlib.pyplot as plt

"""
Radius and equation from GIS Fundamentals 5th Ed. by Paul Bolstad
"""

def gc_distance(point1, point2):
	"""returns distance between point1 (lat, lon) and point2 (lat, lon) in km using great circle equation"""
	lon1, lat1 = point1[0], point1[1]
	lon2, lat2 = point2[0], point2[1]
	lat1, lat2, lon1, lon2 = map(math.radians, [lat1, lat2, lon1, lon2])
	radius = 6378 # WGS84 equatorial radius in km

	trig = math.sin(lat1) * math.sin(lat2) + math.cos(lat1)\
				 * math.cos(lat2) * math.cos(lon1 - lon2)

	if trig >= 1:
		distance = 0
	else:
		distance = radius * math.acos(trig)

	return distance


def class_distance(json_file_path):
	"""returns total distance of ways for a given classification"""
	ways = json.load(open(json_file_path))

	total_distance = 0
	coords = []

	for feature in ways["features"]:
		if feature["geometry"]["type"] == "LineString":
			way_distance = 0
			for coord in feature["geometry"]["coordinates"]:
				coords.insert(0, coord)
				if len(coords) < 2:
					continue
				else:
					p1 = coords[0]
					p2 = coords[1]
					way_distance += gc_distance(p1, p2)
					coords.pop()

			total_distance += way_distance

	return total_distance


def class_piechart(class_dict):
	"""plots a piechart of classification proportions, returns true"""
	labels, sizes = class_dict.keys(), class_dict.values()
	figure = plt.figure()
	ax = figure.add_axes([0, 0, 1, 1])
	ax.axis('equal')
	ax.pie(sizes, labels = labels, autopct='%1.2f%%')
	plt.show()

	return True


def main():
	class_proportions = {}

	class_proportions["primary"] = class_distance(<xml file path>)
	class_proportions["secondary"] = class_distance(<xml file path>)
	class_proportions["tertiary"] = class_distance(<xml file path>)

	class_piechart(class_proportions)

	
if __name__ == "__main__":
	main()
