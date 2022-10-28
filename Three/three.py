import math
import sympy

cur_largest = 0
highest_num = math.floor(math.sqrt(600851475143))
for i in range(1, highest_num):
	if (600851475143 % i == 0 and sympy.isprime(i)):
		cur_largest = i
print(cur_largest)

# solution is 6857