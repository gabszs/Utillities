

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

    except (FileExistsError, FileNotFoundError):  # if the file does not exist, returns false
        return False


def new_file(file_name: str, binary=False):
    """
    receives the file_name, and type('t': txt,'b': binary) and opens the file for read, if file
    does not exist, the function creates a new one with te name as file_name
    :param file_name: str
    :param binary: Bool
    :return: Bool
    """
    try:
        if binary:  # creates new BINARY file if user want to
            with open(file_name, f'xb+') as _:
                return True
        else:
            with open(file_name, f'xt+') as _: # creates new TXT file
                return True

    except (FileExistsError, FileNotFoundError, TypeError, ValueError):  # returns False if some exception raises
        return False


def name_age_txt(file_name, name='unknown', age='unknown', input_parameters=False):
    """
    add name and age to the file, the information going to be written as name;age for each line, set input_parameters
    as True if you don't wat to set name or age
    :param file_name: str
    :param name: str
    :param age: str
    :param input_parameters: Bool
    :return: Write the information in the file, but if exceptions happens, returns an exception
    """
    try:
        with open(file_name, "at") as file:  # using with to short the code e change to a more readable code
            if input_parameters:  # if user don't want to type the name and age, the function do it
                name = input('Type your name: ')
                age = input('Typer your age: ')
                file.write(f'{name};{age}\n')  # add name and age to the line in txt file, after break the line
            else:
                file.write(f'{name};{age}\n')  # add name and age to the line in txt file, after break the line
    except (TypeError, ValueError, FileExistsError, FileNotFoundError):
        raise Exception('The program could not add the information in the file')

def read_name_age(file_name, description=False):
    try:
        if description:
            print(f"REGISTERED PEOPLE\n{16*'-'}>")
        with open(file_name, "rt") as file:
            for line in file:
                name, age = str(line).split(';')
                print(f"name: {name}, age: {age}")

    except:
        print("Deu erro")

read_name_age('gab', description=True)


