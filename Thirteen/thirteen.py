number_file = open("numbers.txt", 'r')
sum = 0
for i in range(100):
   line = number_file.readline()
   sum += int(line)
   
solution = str(sum)[0:10]
print(solution)

# solution is 5537376230
