primes = []
length = 0
limit = 500000


def get_primes(upper):
    results = []
    for cp in range(2, upper + 1):
        for i in range(2, cp):
            if cp % i == 0:
                break
        else:
            print(cp)
            results.append(cp)

    return results


print(get_primes(limit)[10000])