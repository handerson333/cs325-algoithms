import math
import sys, getopt
import string
import time

start = time.time()
		
filename = sys.argv[1]
points = []
pointFile = open(filename, "r")

for l in pointFile:
	points.append(l.split())
	
for temp in range(len(points)):
	points[temp][0] = float(points[temp][0])
	points[temp][1] = float(points[temp][1])	
		

def distanceForm(p0, p1):
	return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
	
distances = []

for i in range(len(points)):
	if i == len(points):
		break
	for j in range(i+1, len(points)):
		distances.append((distanceForm(points[j], points[i]), points[i], points[j]))

distances.sort()		
			
output = open("output_Brute.txt", "w")
output.write(str(distances[0][0]))
output.write("\n")

for i in range(len(distances)):
	if distances[i][0] == distances[0][0]:
		output.write(str(distances[i][1]))
		output.write(str(distances[i][2]))
		output.write("\n")
	

	
output.close()

end = time.time()

print(end-start)