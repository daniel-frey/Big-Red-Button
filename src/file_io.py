import json


def read_file(filename):
    """Read a file and return the output.

    The input will consist of the file that you would like to open.
    The output will be the contents of the said file."""

    if type(filename) is not str:
        raise TypeError('the file must be a string.')

    try:
        with open(filename + '.json') as f:
            data = f.read()

            return data

    except FileNotFoundError:
        raise FileNotFoundError('the specified file was not found.')
    except IOError:
        raise IOError('Your file could not be read.')


def write_file(content, filename):
    """Write a new json file"""
    if type(content) is not str or type(filename) is not str:
        raise TypeError('Please enter a valid filename.')

    try:
        with open('./' + filename + '.json', 'w') as f:
            # data = json.dump(f, content)
            f.write(content)
            return ('Your file has been created.')
    except IOError:
        return ('Something went wrong, please try again.')


if __name__ == '__main__':
    print(read_file('sterile'))
