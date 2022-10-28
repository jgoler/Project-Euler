cur_largest = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		product = i * j
		product_str = str(product)
		if (product_str == product_str[::-1] and product > cur_largest):
			cur_largest = product
print(cur_largest)

# solution is 906609