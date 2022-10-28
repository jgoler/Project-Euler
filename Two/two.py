term_one = 1
term_two = 1
new_term = 2
sum = 0
while (new_term < 4000000):
	if (new_term % 2 == 0):
		sum += new_term
	placeholder = term_two
	term_two = new_term
	term_one = placeholder
	new_term = term_one + term_two
print(sum)

# solution is 4613732
