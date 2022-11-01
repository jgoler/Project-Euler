import sympy

count = 0
for i in range(2, 10000000):
	if sympy.isprime(i):
		count += 1
		if (count == 10001):
			print(i)


# solution is 104743
