def is_clear(location_and_name, log=False):
    try:
        with open(location_and_name, 'r') as f:
            if f.tell() == 0:
                if log:
                    print(f'"{location_and_name}" is clear')
                return True
            else:
                if log:
                    print(f'"{location_and_name}" is not clear')
                return False
    except FileNotFoundError as detail:
        print('Error:', detail)
    except PermissionError as detail:
        print('Error:', detail)
def append(location_and_name, text, log=False, newline=True):
    try:
        with open(location_and_name, 'a') as f:
                if newline:
                    if not is_clear(location_and_name):
                        f.write(f'\n{text}')
                    else:
                        f.write(text)
                else:
                    f.write(text)
        if log:
            print(f'appended "{text}" to "{location_and_name}"')
    except PermissionError as detail:
        print('Error:', detail)
def rewrite(location_and_name, text, log=False):
    try:
        with open(location_and_name, 'w') as f:
            f.write(text)
            if log:
                print(f'Rewritten {text} to {location_and_name}')
    except PermissionError as detail:
        print('Error:', detail)
def create_if_doesnt_exist(location_and_name, text, log=False):
    try:
        with open(location_and_name, 'x') as f:
            f.write(text)
            if log:
                print(f'Created {text} to {location_and_name}')
    except FileExistsError as detail:
        print('Error:', detail)
    except PermissionError as detail:
        print('Error:', detail)
def read(location_and_name, log=False):
    try:
        with open(location_and_name, 'r') as f:
            if log:
                print(f.read())
            return f.read()
    except FileNotFoundError as detail:
        print('Error:', detail)
    except PermissionError as detail:
        print('Error:', detail)
def clear(location_and_name, log=False):
    try:
        with open(location_and_name, 'w') as f:
            f.write('')
            if log:
                print(f'Cleared "{location_and_name}"')
    except FileNotFoundError as detail:
        print('Error:', detail)
    except PermissionError as detail:
        print('Error:', detail)
def delete(location_and_name):
    try:
        from os import remove
        remove(location_and_name)
        print('Deleted', location_and_name)
    except PermissionError as detail:
        print('Error:', detail)
    except FileNotFoundError as detail:
        print('Error:', detail)
def does_exist(location_and_name):
    try:
            read(location_and_name)
            return True
    except FileNotFoundError:
        return False
    except PermissionError as detail:
        print('Error:', detail)
def run(location_and_name):
    try:
        from subprocess import run
        run(location_and_name)
    except PermissionError as detail:
        print('Error:', detail)
    except FileNotFoundError as detail:
        print('Error:', detail)
    except OSError as detail:
        print('Error:', detail)