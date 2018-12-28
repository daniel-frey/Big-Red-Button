import re


def read_file(raw):
    """function to read file
    """
    with open(raw) as f:
        return f.read()


def write_file(path, contents):
    """ function to write to file
    """
    with open(path, 'w') as wf:
        wf.write(contents)


def build_keys(contents):
    """ this method will find the {} characters in the .txt file
    it uses a first and second variable to iterate through each set
    these are stored as a list """
    word_list = list()
    second = 0
    num_brackets = contents.count('{')
    for i in range(num_brackets):
        first = contents.find('{', second) + 1
        second = contents.find('}', first)
        found_word = contents[first:second]
        word_list.append(found_word)
    return (word_list)


def build_stripped(contents):
    """This removes the keys from the raw txt leaving a stripped text """
    regex = r"\{.*?\}"
    output = re.sub(regex, '{}', contents)
    return output


def parse(raw):
    """ parse pulls together tow functions: build keys and build stripped """
    prompts = build_keys(raw)
    stripped = build_stripped(raw)
    return prompts, stripped


def greeting():
    """ This presents user with initial message explaining our helper.
    """
    print('Welcome to our AWS deployment helper. \nIn order to use this product, you will need an AWS account.\n You will need to install the AWS Command Line Interface, \n and configure your files  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html \n \n Please proceed once completed')


def run():
    """ run controls the call stack for the game"""
    greeting()
    # raw =
    read_file(./ec2instance_template.json)
    parse()


if __name__ == '__main__':
    run()
