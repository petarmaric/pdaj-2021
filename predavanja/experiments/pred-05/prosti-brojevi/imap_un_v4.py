import argparse
import csv
from math import sqrt
from multiprocessing import cpu_count, Pool


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

def _worker(args):
    x, y, num = args
    return x, y, num, is_prime(num)

# Not really necessary, as 'Pool._map_async' has a decent enough 'chunksize'
# heuristic, at least for some cases
def guesstimate_optimal_chunk_size(max_num, concurency):
    total_iterations = max_num**2

    # return 1 # BAD: chunksize too small
    # return total_iterations # BAD: chunksize too big

    # DECENT: Each child process *should* have one matrix row to bite at
    return max_num

def analyze_prime_matrix(max_num, concurency):
    with Pool(processes=concurency) as pool:
        yield from pool.imap_unordered(
            _worker,
            gen_input_params(max_num),
            chunksize=guesstimate_optimal_chunk_size(max_num, concurency),
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
