import sys
#first arg is the weight, a; the next are the values

a = float(sys.argv[1]) #first arg in sys.argv is the file name
running_avg = float(sys.argv[2]) 

for n in range(3,len(sys.argv)):
	running_avg = a*float(sys.argv[n]) + (1-a)*running_avg

print(running_avg)