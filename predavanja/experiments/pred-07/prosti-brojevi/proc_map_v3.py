import argparse
import concurrent.futures
import csv
from math import sqrt
from multiprocessing import cpu_count


DEFAULT_MAX_NUM = 1000


def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

def param_sweep(max_num, calc_from_coord):
    for x in range(1, max_num+1):
        for y in range(1, max_num+1):
            yield calc_from_coord(x, y)

def gen_input_params(max_num):
    return (
        param_sweep(max_num, calc_from_coord=lambda x, y: x),
        param_sweep(max_num, calc_from_coord=lambda x, y: y),
        param_sweep(max_num, calc_from_coord=lambda x, y: x * y + 1),
    )

def _worker(x, y, num):
    return x, y, num, is_prime(num)

def analyze_prime_matrix(max_num, concurency):
    with concurrent.futures.ProcessPoolExecutor(max_workers=concurency) as executor:
        yield from executor.map(
            _worker,
            *gen_input_params(max_num),
            chunksize=max_num**2, # BAD: chunksize too big
        )

def store_prime_matrix(results):
    with open(__file__ + '.csv', 'w') as out:
        report = csv.writer(out)
        for x, y, num, is_prime in results:
            report.writerow((x, y, num, int(is_prime)))

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
    parser.add_argument(
        '-c',
        '--concurency',
        metavar='CPUs',
        type=int,
        default=cpu_count(),
        help="Compute in parallel mode, use all CPUs by default",
    )
    args = parser.parse_args()

    results = analyze_prime_matrix(args.max_num, args.concurency)
    store_prime_matrix(results)

if __name__ == "__main__":
    main()
