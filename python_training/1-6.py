import sys

param = sys.argv


if param[1] < param[2] and param[1] < param[3]:
	print 'Yes'
elif param[1] < param[2] and param[2] < param[3]:

	print 'Yes'
else:
	print 'No'
	
