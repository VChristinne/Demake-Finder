import argparse

from components.file_management.list.list_service import list_files, show_size
from components.file_management.list.list_validator import is_valid_directory

def main():
    parser = argparse.ArgumentParser(description="List files in a directory")
    parser.add_argument("directory", help="Directory to list")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
    parser.add_argument("-r", "--recursive", help="List files recursively", action="store_true")
    parser.add_argument("-s", "--size", help="Show file sizes", action="store_true")
    parser.add_argument("-d", "--date", help="Show file dates", action="store_true")
    args = parser.parse_args()
    directory = args.directory

    if is_valid_directory(directory):
        if args.size:
            files = show_size(directory)
        else:
            files = list_files(directory)
        if isinstance(files, list):
            for file in files:
                print(f"├── {file}")
        else:
            print(files)  # Error message
    else:
        print(f"Directory {directory} is not valid")


if __name__ == "__main__":
    main()
