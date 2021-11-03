import argparse
import csv
from math import sqrt


DEFAULT_MAX_NUM = 1000


def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

def gen_input_params(max_num):
    for x in range(1, max_num+1):
        for y in range(1, max_num+1):
            num = x * y + 1
            yield x, y, num

def analyze_prime_matrix(max_num):
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
