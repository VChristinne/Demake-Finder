import os

def list_files(directory):
    """
    List all files in a directory
    :param directory:
    :return: list of files
    """
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        return f"Directory {directory} not found"
    except PermissionError:
        return f"Permission denied for directory {directory}"
    except Exception as e:
        return f"Error: {e}"
