amount = 200
num_ways = [0] * (amount+1)
num_ways[0] = 1
coins = [1,2, 5, 10, 20, 50, 100, 200]

for c in coins:
	for i in range(c, amount+1):
		num_ways[i] += num_ways [i-c] 


print(num_ways[200])