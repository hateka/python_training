import sys

param = sys.argv
end = len(param) 


for i in range(1, end):
	for j in range(i + 1, end):
		if param[i] > param[j]:
			tmp = param[j]
			param[j] = param[i]
			param[i] = tmp

del param[0]

print param 
