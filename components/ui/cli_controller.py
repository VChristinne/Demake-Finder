import argparse
import sys

from components.file_management.list.list_service import list_files, list_size, list_date
from components.file_management.list.list_validator import is_valid_directory

def main():
    parser = argparse.ArgumentParser(description="List files in a directory")
    parser.add_argument("directory", help="Directory to list")
    parser.add_argument("-l", "--list", help="List files", action="store_true")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
    parser.add_argument("-s", "--size", help="Show file sizes", action="store_true")
    parser.add_argument("-d", "--date", help="Show file dates", action="store_true")
    args = parser.parse_args()
    directory = args.directory

    if is_valid_directory(directory):
        if args.list:
            list_files(directory)
        elif args.size:
            list_size(directory)
        elif args.date:
            list_date(directory)
    else:
        print(f"Directory {directory} is not valid")
        sys.exit(1)


if __name__ == "__main__":
    main()
