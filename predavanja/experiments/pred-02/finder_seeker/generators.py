import fnmatch
import itertools
import os


def debug_stream(stream, start=0, stop=None):
    for item in itertools.islice(stream, start, stop):
        print(item)

def find_files(top_dir='.'):
    for dirpath, _, filenames in os.walk(top_dir):
        for name in filenames:
            yield os.path.join(dirpath, name)

def filter_filenames(filenames, pattern):
    for name in filenames:
        if fnmatch.fnmatchcase(name, pattern):
            yield name

def parse_file(filenames):
    for name in filenames:
        with open(name) as fp:
            for line in fp:
                yield line.strip()

def filter_lines(lines, pattern):
    for line in lines:
        if pattern in line:
            yield line

def pipeline(top_dir):
    filenames = find_files(top_dir)
    filenames = filter_filenames(filenames, '*.csv')
    filenames = filter_filenames(filenames, '*T12*')

    lines = parse_file(filenames)
    lines = filter_lines(lines, '2017')

    return lines

def main():
    stream = pipeline(top_dir=os.path.expanduser('~/fax'))

    debug_stream(stream, start=0, stop=10)

if __name__ == "__main__":
    main()
