from xml.dom.minidom import parse
import xml.dom.minidom
import math
import matplotlib.pyplot as plt

"""
Radius and equation from GIS Fundamentals 5th Ed. by Paul Bolstad
"""

def gc_distance(point1, point2):
	"""returns distance between point1 (lat, lon) and point2 (lat, lon) using great circle equation"""
	lat1, lon1 = point1[0], point1[1]
	lat2, lon2 = point2[0], point2[1]
	lat1, lat2, lon1, lon2 = map(math.radians, [lat1, lat2, lon1, lon2])
	radius = 6378 # WGS84 equatorial radius in km

	distance = radius * math.acos(math.sin(lat1) * math.sin(lat2) \
		+ math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))

	return distance


"""
XML DOM parsing code from https://www.tutorialspoint.com/python/python_xml_processing.htm
"""

def class_distance(xml_file_path):
	"""returns total distance between nodes of a given classification"""
	DOMTree = parse(xml_file_path)
	elements = DOMTree.documentElement
	nodes = elements.getElementsByTagName("node")

	total_distance = 0
	coords = []

	for node in nodes:
		if node.hasAttribute("lat") and node.hasAttribute("lon"):
			coords.insert(0, (float(node.getAttribute("lat")), float(node.getAttribute("lon"))))
		if len(coords) < 2:
			continue
		else:
			p1 = coords[0]
			p2 = coords[1]
			total_distance += gc_distance(p1, p2)
			coords.pop()

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

	class_proportions["primary"] = class_distance("kent_primary_bbox.xml")
	class_proportions["secondary"] = class_distance("kent_secondary_bbox.xml")
	class_proportions["tertiary"] = class_distance("kent_tertiary_bbox.xml")

	class_piechart(class_proportions)

	
if __name__ == "__main__":
	main()
