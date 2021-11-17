import argparse
import csv
import os

from PIL import Image


def analyze_prime_matrix_report(filename):
    with open(filename, 'r') as fp:
        report = csv.reader(fp)

        prime_coords = [
            (int(x) - 1, int(y) - 1) # 1-index to 0-index
            for x, y, _, is_prime in report
            if int(is_prime) == 1
        ]

        image_width = max(x for x, _ in prime_coords) + 1
        image_height = max(y for _, y in prime_coords) + 1

        return (image_width, image_height), prime_coords

def store_prime_matrix_as_image(filename, image_size, prime_coords):
    with Image.new(size=image_size, mode='1') as img:
        # 1 (white color) denotes that a specific prime coord is a prime
        # 0 (black color) denotes that a specific prime coord is NOT a prime (``Image.new`` does this for us by default)
        for xy in prime_coords:
            img.putpixel(xy, 1)

        img.save(filename)

def main():
    # Setup command line option parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filename',
        help='Prime matrix report to visualize, in CSV format'
    )
    args = parser.parse_args()

    image_size, prime_coords = analyze_prime_matrix_report(args.filename)
    store_prime_matrix_as_image(os.path.basename(args.filename + '.png'), image_size, prime_coords)

if __name__ == "__main__":
    main()
