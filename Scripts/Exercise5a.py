#Exercise 5a
#Allowing inputs to your script with sys.argv[]
#Try running with: ENV859 "100 meters" 100 17.6

import sys
className = sys.argv[1]
distance = sys.argv[2]
print(distance)
A = sys.argv[3]
B = sys.argv[4]
print(int(A)+float(B))

