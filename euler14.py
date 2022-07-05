# Function to get next term in the sequence.
def next_collatz_term(begin:int):
    if (begin % 2 == 0):
        return begin/2
    if (begin % 2 != 0):
        return begin*3 + 1

# Function to generate a sequence given a beginning term.
def collatz_sequence(beginning_term:int):
    # Begins the sequence array by inserting the beginning term.
    sequence = [beginning_term]
    # Variable we will be working with.
    current_term = beginning_term
    # Loops until the breaking condition. (Not guaranteed to work though.)
    while current_term != 1:
        # Generates the next term in the sequence.
        next_term = int(next_collatz_term(current_term))
        # Appends it to the end of the sequence array.
        sequence.append(next_term)
        # Sets the value of the current term to the term just calculated.
        current_term = next_term

    # Once break condition is met, return the sequence array.
    return sequence

size = 1
starting_number = 0;

# Loops through all numbers 1 through 999999
for i in range(1, 1000000):
    print("Iteration: " + str(i))
    # Variable of the current length of the sequence being calculated.
    temp = len(collatz_sequence(i))
    # If its larger than the current size variable...
    if (temp > size):
        # Set size equal to the current iteration of the sequence.
        size = temp
        # Set the starting number to thte current one with the largest sequence.
        starting_number = i


print("LARGEST SEQUENCE OF SIZE: " + str(size) + "\nOF STARTING NUMBER: " + str(starting_number))