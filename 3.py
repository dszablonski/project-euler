primes = []
limit = 100000
number = 600851475143
result = []


def get_primes(upper):
    results = []
    for cp in range(2, upper + 1):
        for i in range(2, cp):
            if cp % i == 0:
                break
        else:
            results.append(cp)

    return results


primes = get_primes(limit)


for j in primes:
    if number % j == 0:
        result.append(j)

print(result)
