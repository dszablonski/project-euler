sum_of_squares = 0
square_of_sums = 0

for j in range(1, 101):
    square_of_sums += j
    sum_of_squares += (j*j)

square_of_sums *= square_of_sums

difference = square_of_sums - sum_of_squares

print(sum_of_squares)
print(square_of_sums)
print(difference)

limit = 1000000000
sums = limit*(limit+1)/2
sums_sq = (2*limit + 1)*(limit+1)*limit/6
print((sums*sums)-sums_sq)