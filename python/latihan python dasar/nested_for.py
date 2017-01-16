print "nested foo on prime number case among 1 t0 20"

for i in range(1,20):
	count_zero_remainder = 0 
	for j in range (1, i+1):
		num_remainder = i%j
		print num_remainder
		if num_remainder == 0:
			count_zero_remainder = count_zero_remainder + 1
	if count zero_remainder == 2:
		print i, "is a prime number"
	else:
		print i, "it is not a prime number"
