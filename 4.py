digits0 = []
digits1 = []
products_of_digits = []
list_of_palindromes = []


def digit_gen():
    result = []

    for i in range(100, 1000):
        result.append(i)

    return result


def product_of_arrays(arr1, arr2):
    result = []

    for j in arr1:
        for k in arr2:
            result.append(j * k)

    return result


def check_if_palindrome(number):
    starting_point = int(len(str(number)) / 2)

    first = str(number)[:starting_point]
    last = str(number)[-starting_point:][::-1]

    if first == last:
        return True


digits0 = digit_gen()
digits1 = digit_gen()
products_of_digits = product_of_arrays(digits0, digits1)
products_of_digits.sort()

for product in products_of_digits:
    if check_if_palindrome(product):
        list_of_palindromes.append(product)
    else:
        continue

print(list_of_palindromes)
