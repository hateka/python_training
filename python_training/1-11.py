import sys

param = sys.argv
end = len(param)

j = 1

for i in range(1, end):
	if j % 2 == 0:
		left = int(param[i - 1])
		right = int(param[i])

		if left == 0 and right == 0:
			break

		if left > right :
			print str(right) + ' ' + str(left)
		else:
			print str(left) + ' ' + str(right)

	j+=1