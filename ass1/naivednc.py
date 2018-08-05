import math
import sys, getopt
import string
import time


filename = sys.argv[1]
points, xpoints, ypoints = [], [], []
pointFile = open(filename, "r")

for l in pointFile:
	points.append(l.split())

for temp in range(len(points)):
	points[temp][0] = float(points[temp][0])
	points[temp][1] = float(points[temp][1])
	
for i in range(len(points)):
	xpoints.append(points[i])
	ypoints.append(points[i])
	
stored_min = []

xpoints.sort()




def distanceForm(p0, p1):
	return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
	

def crossPoints(masterY, delta):
	dm = delta
	d = []
	for i in range(len(masterY) - 1):
		j = i+1
		while j < len(masterY) and masterY[j][1] - masterY[i][1] <= delta:
			stored_min.append((distanceForm(masterY[i], masterY[j]), masterY[i], masterY[j]))
			d = distanceForm(masterY[i], masterY[j])
			dm = min(d, dm)
			j += 1
	return dm

	
def closestPair(points):	
	distances = []
	left, right = [], []
	distLeft, distRight = [], []
	
	if len(points) <= 3:
		for i in range(len(points)):
			for j in range(i+1, len(points)):
				stored_min.append((distanceForm(points[i], points[j]), points[i], points[j]))
				distances = distanceForm(points[i], points[j])
		return distances
	else:
		yLeft = []
		yRight = []
		#ypoints.sort()
		sepLine = len(points)/2
				
		distLeft = closestPair(points[:sepLine])

		distRight = closestPair(points[sepLine:])
		
		delta = min(distLeft, distRight)
		#print delta
		masterY = []
		
		for i in range(len(points)):
			if	points[i][0] >= sepLine - delta and points[i][0] <= sepLine + delta:
				masterY.append(points[i])
				
		masterY.sort(key=lambda i: i[1])
		min_pair = crossPoints(masterY, delta)
		
		return min_pair

start = time.time()	
closest_pairs = closestPair(xpoints)	

final_points = []


for i in range(len(stored_min)):
	if stored_min[i][0] == closest_pairs:
		if stored_min[i] not in final_points:
			final_points.append(stored_min[i])
		
		
final_points.sort(key=lambda i: i[1])
output = open("output_naivednc.txt", "w")
output.write(str(final_points[0][0]))
output.write("\n")	
	
for i in range(len(final_points)):
		if final_points[i][0] == final_points[0][0]:
			output.write(str(final_points[i][1]))
			output.write(str(final_points[i][2]))
			output.write("\n")
	
end = time.time()
print(end-start)