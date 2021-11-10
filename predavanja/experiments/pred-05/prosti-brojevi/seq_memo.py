import argparse
import csv
from math import sqrt


DEFAULT_MAX_NUM = 1000

_CACHED_PRIMES = None
def _regen_cached_primes(max_num):
    max_potential_prime = max_num + 1

    global _CACHED_PRIMES
    _CACHED_PRIMES = set([2]) # seed the prime cache

    for num in range(3, max_potential_prime+1, 2): # only odd numbers can be primes
        if is_prime(num): # cumulatively build the prime cache
            _CACHED_PRIMES.add(num)

def is_prime(num):
    if num in _CACHED_PRIMES:
        return True

    for prime in _CACHED_PRIMES:
        if num % prime == 0:
            return False

    return True

def gen_input_params(max_num):
    for x in range(1, max_num+1):
        for y in range(1, max_num+1):
            num = x * y + 1
            yield x, y, num

def analyze_prime_matrix(max_num):
    _regen_cached_primes(max_num)

    for x, y, num in gen_input_params(max_num):
        yield x, y, num, is_prime(num)

def store_prime_matrix(results):
    with open(__file__ + '.csv', 'w') as out:
        report = csv.writer(out)

        for x, y, num, is_prime in results:
            report.writerow([x, y, num, int(is_prime)])

def main():
    # Setup command line option parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        '--max-num',
        metavar='DIM',
        type=int,
        default=DEFAULT_MAX_NUM,
        help=f"Compute a prime matrix with the size of DIM*DIM, where DIM is {DEFAULT_MAX_NUM} by default",
    )
    args = parser.parse_args()

    results = analyze_prime_matrix(args.max_num)
    store_prime_matrix(results)

if __name__ == "__main__":
    main()
