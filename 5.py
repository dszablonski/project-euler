number_list = []
# This is 20 as there's no point in starting lower, each number needs to be divisible by the largest number in the
# number_list array
number = 20
has_completed = False

# Generates numbers between 2 and 20 (1 doesn't really matter in this case)
for i in range(2, 21):
    # Adds the numbers to the number_list array
    number_list.append(i)

# While the has_completed variable is false, this code will run
while not has_completed:
    # Run through each number in number_list
    for i in number_list:
        # If the number can be divided by the current number being ran through
        if number % i == 0:
            # and if the number being ran through is the last number in the array (ensures  that the number is
            # divisible by the entire array of numbers)
            if i == number_list[-1]:
                # sets has_completed to true, this will be the last run through the while loop
                has_completed = True
            # otherwise continue with the for loop
            else:
                continue
        # if the number isn't divisible by a number in the array, the for loop breaks
        else:
            break

    # if has_completed is false,
    if not has_completed:
        # the number variable will increment by the last number in the number_list array.
        # there's no point incrementing it by anything lower than the largest number
        number += number_list[-1]

    # If has_completed is true, the number will be printed.
    if has_completed:
        print(number)
