from decimal import *
getcontext().prec = 50

max = input ("Enter Number of Iterations: ")

if max < 2:
	print "Input must be larger than 2"
	
runsum = Decimal(0.0)
	
for x in xrange(1, max):
	runsum = runsum + (Decimal(1.000) / x)
	print runsum