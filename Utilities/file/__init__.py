

def check_file(file_name: str):
    """
    file_name: str
    Check if the file_name is in the directory of the project, if the file does not exist, the function
    creates a new one with the name file_name
    :param file_name: str
    :return: Bool
    """
    try:
        with open(file_name, "rt") as _:  # r = read, t = text(txt)
            return True

    except (FileExistsError, FileNotFoundError):
        return False


def new_file(file_name: str, file_type: str):
    """
    receives the file_name, and type('t': txt,'b': binary) and opens the file for read, if file
    does not exist, the function creates a new one with te name as file_name
    :param file_name: str
    :param file_type: str
    :return: Bool
    """
    if file_type in 't' or file_type in 'b':
        try:
            with open(file_name, f'w{type}+') as _:
                return True
        except (FileExistsError, FileNotFoundError, TypeError, ValueError):
            return False
    else:
        return False

