import sys

param = sys.argv
end = len(param)

for i in range(1, end):
	param[i] = int(param[i])

	if i < 5:
		if param[i] < 0 or param[i] > 100:
			print 'param is valid'
	else:
		if  param[i] > 100:
			print 'param is valid'
	W = int(param[1])
	H = int(param[2])

	w = int(param[3]) + int(param[5])
	h = int(param[4]) + int(param[5])

	if w > W or h > H:
		print 'NO'
		break
	else:
		print 'YES'
		break
