import argparse
import pathlib
import sys

import standardize

if __name__ == "__main__":
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('files', nargs='*', default=sys.stdin)
    parser.add_argument('-i', '--in-place', action='store_true')

    for option, help in standardize.OPTIONS.items():
        parser.add_argument(f'--{option}', action="store_true", help=help)

    args = parser.parse_args()
    
    if args.files == sys.stdin:
        args.files = sys.stdin.read().splitlines()

    modifications = [k for k, v in vars(args).items() if v and k in standardize.OPTIONS]

    if not modifications:
        print('Specify something to be done.')
        parser.print_usage()
        sys.exit()

    for file in args.files:
        path = pathlib.Path(file)

        if not path.exists():
            print(f'File does not exist: {path}')
            continue

        result = standardize.update(path, modifications)

        if args.in_place:
            path.write_text(result)
        else:
            print(result, end='')