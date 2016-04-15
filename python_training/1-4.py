import sys
import math

buffer = sys.stdin.read()
buffer = int(buffer)


h = int(buffer / 3600)

m = int((buffer - (h * 3600)) / 60)

s = int((buffer - (h * 3600)) - (m * 60))


print str(h) + ':' + str(m) + ':' + str(s)

