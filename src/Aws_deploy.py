from file_io import read_file, write_file
from textwrap import dedent
import re
import sys


def greet_user():
    """Greet the user upon application start."""
    ln_1 = 'AWS Deployment automation'
    ln_2 = 'You will need to have some prerequisites before you are able to begin'
    ln_3 = 'You will receive a series of prompts. Please read the questions carefully'
    ln_4 = 'Once the questions have finished, a json file will be written that will be used for deployment'
    ln_5 = 'To exit at any time, type "quit".'

    print(dedent(f'''
        {'*' * 70}

        {'{:^70}'.format(ln_1)}

        {'{:^70}'.format(ln_2)}
        {'{:^70}'.format(ln_3)}
        {'{:^70}'.format(ln_4)}

        {'{:^70}'.format(ln_5)}

        {'*' * 70}
        '''))


def prompt_for_file():
    """Prompt the user for a filename"""
    file = ''
    while file is '':
        file = input('Please enter a filename: ')
        if input is '':
            print('Please enter a filename: ')
    return file


def read_template(file):
    """Take the user input, read the file."""
    if file.lower() == 'exit':
        exit()

    try:
        content = read_file(file)
        if '%' in content:
            return [True, content]

        return [False, 'Incorrect filetype was chosen']
    except FileNotFoundError:
        return [False, 'The specified file does not exist']
    except IOError:
        return [False, 'There was an error reading this file']
    except Exception:
        return [False, 'Something else went wrong']


def run_template(ec2instance_template):
    """Take in the ec2 instance template"""
    if ec2instance_template[0] is False:
        print(ec2instance_template[1])
    else:
        answers = re.findall(r'\%.*?\#', ec2instance_template[1])
        ec2instance_template[1] = re.sub(r'\%.*?\#', '%#', ec2instance_template[1])

        for i in range(len(answers)):
            answers[i] = answers[i].strip('%#')

        user_answers = prompt_the_user(answers)

        print(len(tuple(user_answers)))
        ec2instance_template[1] = ec2instance_template[1].format(*tuple(user_answers))

        return ec2instance_template


def prompt_the_user(answers):
    """Take in the template and format the output"""
    print('Beginning template creation \n')
    answers_out = []

    for i in range(len(answers)):
        user_input = input(answers[i] + ': ')
        if user_input == 'exit':
            exit()

        answers_out.append(user_input)

    return answers_out


def user_output(template_output):
    """Take in the template, and prompt the user"""
    if template_output[0] is True:
        print('Your template: \n\n')
        print(template_output[1])
        user_input = input('Type "y" to save: ').lower()

        if user_input == 'exit':
            exit()
        if user_input == 'y':
            user_filename = input('Please enter the name you would like to use: ')
            print(write_file(template_output[1], user_filename))
    else:
        print('There was a problem, please try again')


def exit():
    sys.exit()


def run():
    greet_user()
    while True:
        empty_template = read_template(prompt_for_file())
        completed_template = run_template(empty_template)
        user_output(completed_template)
        user_input = input('Would you like to create another instance? y/n')
        if user_input.lower == 'y':
            continue

        exit()


if __name__ == '__main__':
    run()
