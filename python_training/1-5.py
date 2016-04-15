import sys

param = sys.argv

if param[1] < param[2]:
	print param[1] +' < '+ param[2]
elif param[1] > param[2]:
	print param[1] + ' > ' + param[2]
elif param[1] == param[2]:
	print param[1] + ' == ' + param[2]
