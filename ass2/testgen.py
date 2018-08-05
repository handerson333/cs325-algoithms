import sys
import string
import os
import csv
import numpy as np
import random

#make the input file
filename = "imp2input.txt"
file = open(filename,'w')
#get the cla
amount = sys.argv[1]
random.seed(a=None)
amount = int(amount)
rng = [0]*amount

def make_array( amount ):
	for i in range(0,amount):
		temp = random.randint(1,4)
		if temp == 1:
			temp = 'A'
		elif temp == 2:
			temp = 'T'
		elif temp == 3:
			temp = 'G'
		else:
			temp = 'C'
			
	        rng[i] = temp

		with open(filename,'a') as f:
			f.write(temp)



for j in range(0,20):
	make_array(amount)
	with open(filename,'a') as f:
		if j % 2 == 0:
			f.write(',')
		else:
			f.write("\n")





