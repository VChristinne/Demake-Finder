import argparse

from components.file_management.list.list_service import list_files
from components.file_management.list.list_validator import is_valid_directory

def main():
    parser = argparse.ArgumentParser(description="List files in a directory")
    parser.add_argument("directory", help="Directory to list")
    args = parser.parse_args()
    directory = args.directory

    if is_valid_directory(directory):
        files = list_files(directory)
        if isinstance(files, list):
            print("Files: ")
            for file in files:
                print(file)
        else:
            print(files)  # Error message
    else:
        print(f"Directory {directory} is not valid")


if __name__ == "__main__":
    main()
