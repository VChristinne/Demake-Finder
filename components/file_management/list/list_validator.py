import os

def is_valid_directory(directory):
    """
    Check if a directory is valid
    :param directory:
    :return: boolean
    """
    return os.path.isdir(directory) and os.access(directory, os.R_OK)
