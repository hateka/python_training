import sys

param = sys.argv
end = len(param)

for i in range(1, end):
	param[1] = int(param[1])
	param[2] = int(param[2])
	param[3] = int(param[3])
	param[4] = int(param[4])
	param[5] = int(param[5])

	if param[1] < 0 or param[2] < 0 or param[1] > 100 or param[2] > 100:
		print 'param is valid'
	if param[3] < 0 or param[4] < 0 or param[3] > 100 or param[4] > 100 or param[5] > 100:
		print 'param is valid'

	w = param[3] + param[5]
	h = param[4] + param[5]
	
	if w > param[1] or h > param[2]:
		print 'NO'
		break
	else:
		print 'YES'
		break
