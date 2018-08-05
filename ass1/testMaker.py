import random

output = open("Test10^2.txt", "w")

for i in range(0, 100):
	output.write(str(random.randint(-200,200)))
	output.write(" ")
	output.write(str(random.randint(-200,200)))
	output.write("\n")
	
output.close()

output = open("Test10^3.txt", "w")

for i in range(0, 1000):
	output.write(str(random.randint(-2000,2000)))
	output.write(" ")
	output.write(str(random.randint(-2000,2000)))
	output.write("\n")
	
output.close()

output = open("Test10^4.txt", "w")

for i in range(0, 10000):
	output.write(str(random.randint(-2000,2000)))
	output.write(" ")
	output.write(str(random.randint(-2000,2000)))
	output.write("\n")
	
output.close()

output = open("Test10^5.txt", "w")

for i in range(0, 100000):
	output.write(str(random.randint(-2000,2000)))
	output.write(" ")
	output.write(str(random.randint(-2000,2000)))
	output.write("\n")
	
output.close()
