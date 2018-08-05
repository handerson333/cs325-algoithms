import sys
import string
import os
import csv
import numpy as np
import time

os.path.isfile("imp2cost.txt")
f = open("imp2cost.txt" , 'r')

file_read = csv.reader(f, delimiter=',')
a = []
for row in file_read:
	a.append(row)
cost = {}
for i in range(1, len(a)):
	temp = {}
	for j in range(1, len(a[0])):
		temp[a[0][j]] = int(a[i][j])
	cost[a[i][0]] = temp

os.path.isfile("imp2input.txt")
q = open("imp2input.txt", "r")
genes = []
for p in q:
	genes.append(p.split())
f.close()
cleanGene = []
for i in xrange(0, len(genes)):
	cleanGene.append(genes[i][0].split(','))
	
	
def cost_dict_calc(character1, character2, cost):
	if character1 == character2:
		return 0
	else:
		return int(cost[character1][character2])

def d_form(string1, string2, cost_dict):

	distance = np.zeros((len(string1)+1, len(string2)+1), dtype= np.int16)
	distance[0][0] = 0

	for i in xrange(len(string1) + 1):
		distance[i,0] = i * int(cost_dict[string1[i-1]]['-'])
		
	for j in xrange(len(string2) + 1):
		distance[0,j] = j * int(cost_dict['-'][string2[j-1]])
		
	for i in xrange(1, len(string1) + 1):
		for j in xrange(1, len(string2) + 1):
			distance[i][j] = min(distance[i-1,j-1] + cost_dict_calc(string1[i-1], string2[j-1], cost_dict),
								distance[i-1,j] + cost_dict_calc(string1[i-1], '-', cost_dict),
								distance[i,j-1] + cost_dict_calc('-', string2[j-1], cost_dict))
	
	alignment = []
	i = len(string1)
	j = len(string2)
	while i > 0  and j > 0:
		#minCost = min(distance[i-1, j], distance[i, j-1], distance[i-1, j-1])
		#if minCost == distance[i-1,j-1]:
		if distance[i-1, j-1] + cost_dict_calc(string1[i-1], string2[j-1], cost_dict) == distance[i, j]:
			alignment.append(align_pairs(i, j, string1, string2))
			i -= 1
			j -= 1
			
		#elif minCost == distance[i-1, j]:
		elif distance[i-1, j] + cost_dict_calc(string1[i-1], '-', cost_dict) == distance[i, j]:
			alignment.append(align_pairs(i, 0, string1, string2))
			i -= 1
			
		else:
			alignment.append(align_pairs(0, j, string1, string2))
			j -= 1
			
	while i > 0:
		alignment.append(align_pairs(i, 0, string1, string2))
		i -= 1
		
	while j > 0:
		alignment.append(align_pairs(0, j, string1, string2))
		j -= 1
		
	alignment.reverse()
	
	f = open("imp2output.txt", "a+")
	top = []
	bottom = []
	for(i, j) in alignment:
		top.append(i)
		bottom.append(j)
	for n in top:
		f.write(n)
	f.write(",")
	for n in bottom:
		f.write(n)
	f.write(":")
	f.write(str(distance[len(string1), len(string2)]))
	f.write("\n")
	f.close()
	
def align_pairs(i, j, seq1, seq2):
	n1 = seq1[i-1] if i>0 else '-'
	n2 = seq2[j-1] if j>0 else '-'
	return (n1,n2)
start = time.time()		
for i in range(0, len(cleanGene)):
	distance_set = d_form(cleanGene[i][0], cleanGene[i][1], cost)
end = time.time()
print(end-start)
