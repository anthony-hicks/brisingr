import argparse
import pathlib
import sys

from brisingr import Brisingr

if __name__ == "__main__":
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('files', nargs='*', default=sys.stdin)
    parser.add_argument('-i', '--in-place', action='store_true')

    brisingr = Brisingr()
    brisingr.set_parser(parser)

    args = brisingr.parse_args()

    if args.files == sys.stdin:
        args.files = sys.stdin.read().splitlines()

    if not brisingr.plugins.active:
        print('Specify something to be done.')
        parser.print_usage()
        sys.exit(1)

    for file in args.files:
        path = pathlib.Path(file)

        if not path.exists():
            print(f'File does not exist: {path}')
            continue

        result = brisingr.update(path)

        if args.in_place:
            path.write_text(result)
        else:
            print(result, end='')