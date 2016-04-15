import sys

buffer = sys.stdin.read().split()


buffer[0] = int(buffer[0])
buffer[1] = int(buffer[1])

area = buffer[0] * buffer[1]
length = (buffer[0] + buffer[1]) * 2

print str(area) + ' ' + str(length)
