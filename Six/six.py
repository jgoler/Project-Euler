sum_squares = 0
sum = 0
for i in range(1, 101):
	sum_squares += i**2
for j in range(1, 101):
	sum += j
square_sum = sum*sum
print(square_sum - sum_squares)

#solution is 25164150
