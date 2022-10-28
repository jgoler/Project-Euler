num = 2**1000
running_sum = 0
str_num = str(num)
for i in range(len(str_num)):
	running_sum += int(str_num[i])
print(running_sum)

#answer is 1366