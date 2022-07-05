file_name = "euler13.txt"
file = open(file_name, "r")
sum = 0

lines = file.readlines()

for i in lines:
    sum += int(i)

print(str(sum)[:10])

file.close()