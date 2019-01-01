"""Imports."""
import sys
import os
import pyfiglet

aws_host = 'aws_import'
security_group = 'Input Needed'
region = 'US-WEST-2'
output_format = 'JSON'


def signage():
    """Creates ascii display for CMD."""
    result = pyfiglet.figlet_format("AWS Automator")
    print(result)


def display_menu():
    """."""
    answer = ''
    global file
    while answer != 'quit' or answer != 'exit' or answer != 'q':
        signage()
        print(f'1.  Current Host Name (ex: aws.json): \033[1;33m { aws_host } \033[0;0m')
        print(f'2.  Current Region: \033[1;33m { region } \033[0;0m')
        print(f'3.  Current Security Group Name: \033[1;31m { security_group } \033[0;0m')
        print(f'4.  Current output format: \033[1;33m { output_format } \033[0;0m')
        print(f'5.  Current output format: \033[1;33m { output_format } \033[0;0m')
        print(f'6.  Current output format: \033[1;33m { output_format } \033[0;0m')
        print(f'7.  Current output format: \033[1;33m { output_format } \033[0;0m')
        print(f'8.  Current output format: \033[1;33m { output_format } \033[0;0m')
        print(f'9.  Current output format: \033[1;33m { output_format } \033[0;0m')
        print(f'10. Current output format: \033[1;33m { output_format } \033[0;0m')
        print(f'11. Current output format: \033[1;33m { output_format } \033[0;0m')
        print('12. Display File')

        answer = input('\n(e) Execute (q) Quit (h) Help \nPlease Enter a Selection: ')
        if answer == 'h' or answer == '?':
            print('\nHELP MENU TO GO HERE\n')
            input('Press ENTER to continue...')

        elif answer == 'q' or answer == 'quit' or answer == 'exit':
            exit()

        elif answer == '1':
            file = input('Enter a file name (press enter to select default): ')
            if file is '':
                file = 'aws_import'

    def write_to_file():
            print(file)
            print(security_group)
            print(region)
            print(output_format)


def clear_screen():
    """Clears the screen."""
    os.system('clear')
    return


def exit():
    """Function to exit gracefully."""
    sys.exit('\n\nThank you for using the application\n\n')


if __name__ == '__main__':
    try:
        clear_screen()
        display_menu()
    except KeyboardInterrupt:
        print('\n\nThank you for using the application\n\n')
