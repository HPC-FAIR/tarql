import sys
import os
import rdflib
import json
import pprint

from collections import Counter
from rdflib import Graph, plugin
from rdflib.serializer import Serializer


def main(argv):
	inputfile = argv[0]
	g = Graph()
	g.parse(inputfile, format="nt")

	# print(len(g)) # prints 2

	# for stmt in g:
	#    pprint.pprint(stmt)

	j = g.serialize(format='json-ld', indent=4).decode('utf-8')

	# print(j)
	name = os.path.splitext(inputfile)[0]
	outputname = os.path.join(name + "." + "json")

	with open(outputname, 'w') as f:
	    f.write(str(j))
	f.close()

if __name__ == "__main__":
        main(sys.argv[1:])

