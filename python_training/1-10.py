import sys

param = sys.argv
end = len(param)

for i in range(1, end):
	num = int(param[i])

	if num > 0:
		print 'Case ' + str(i) + ': ' + str(param[i])
