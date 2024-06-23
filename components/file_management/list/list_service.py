import math
import os
import pathlib

import shared.utils.exceptions as ex

def list_files(directory):
    """
    List all files in a directory
    :param directory:
    :return: list of files
    """
    try:
        directory = pathlib.Path(directory)
        for file in directory.iterdir():
            print(f"├── {file.name}")
    except ex.FileNotFoundError:
        return f"Directory {directory} not found"
    except ex.PermissionDeniedError:
        return f"Permission denied for directory {directory}"
    except Exception as e:
        return f"Error: {e}"

def list_date(directory):
    """
    List all files in a directory with their dates
    :param directory:
    :return: list of files with dates
    """
    import datetime
    try:
        directory = pathlib.Path(directory)
        for file in directory.iterdir():
            dt = datetime.datetime.fromtimestamp(file.stat().st_birthtime)
            dt_strf = dt.strftime("%d/%m/%Y %H:%M %p")
            print(f"├── {file.name} ({dt_strf})")
    except ex.FileNotFoundError:
        return f"Directory {directory} not found"
    except ex.PermissionDeniedError:
        return f"Permission denied for directory {directory}"
    except Exception as e:
        return f"Error: {e}"

def convert_size(size_bytes):
    """
    Convert file size in bytes to the most appropriate unit
    :param size_bytes:
    :return: size with unit as a string
    """
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def list_size(directory):
    """
    Show file sizes in a directory
    :param directory:
    :return: list of files with sizes
    """
    files = list_files(directory)
    if isinstance(files, list):
        files_with_size = []
        for file in files:
            file_path = os.path.join(directory, file)
            size = os.path.getsize(file_path)
            files_with_size.append(f"{file} ({convert_size(size)})")
        return files_with_size
    else:
        return files