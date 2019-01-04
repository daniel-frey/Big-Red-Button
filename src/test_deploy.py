import sys
import pytest
from . import menu
# from . import ec2instance_template



def test_cc_import():
    """
    """
    assert menu.signage




def test_clear_screen(capsys):
    """ tests clear screen method - if method returns true then method works
    """
    menu.clear_screen()
    out, err = capsys.readouterr()
    assert True
    assert err == ''
    assert out == ''


def test_exit_system():
    """ tests exit method - checks the type in this function
    """
    with pytest.raises(SystemExit) as e:
        menu.exit()
        assert e.type == SystemExit


def test_user_password():
    """
    """
    input_values = ['testhost', 'testhost']

    def mock_input(s):
        return input_values.pop(0)

    menu.getpass.getpass = mock_input
    words = menu.user_passwords()

    assert words is None


def test_user_password_invalid():
    """
    """
    input_values = ['testhost', 'not_testhost', 'continue', 'testhost', 'testhost']

    def mock_password(s):
        return input_values.pop(0)

    def mock_input(s):
        return input_values.pop(0)

    menu.getpass.getpass = mock_password
    menu.input = mock_input
    words = menu.user_passwords()

    assert words is None

# def test_json_write():
#     """
#     """
#     aws_host = 'test host'
#     security_groups = 'testgroup'
#     aws_security_groups = ''
#     region = 'us-west-2a'
#     output_format = 'JSON'
#     image_id = 'ami-0bbe6b35405ecebdb'
#     db_name = 'Testdatabase'
#     db_instance_id = 'instanceDB'
#     db_storage = 20
#     db_instance_class = 'db.t2.micro'
#     db_engine = 'postgres'
#     db_user_name = 'testuser'
#     db_user_password = 'password'
#     key_name = 'dummykey'

#     menu.write_json()
#     assert rds_json_data['DBName'] == 'Testdatabase'


# def test_exit_output(capsys):
#     """ tests exit method - checks the output in this function
#     """
#     menu.exit()
#     out, err = capsys.readouterr()

#     assert err == ''
#     assert out == 'Thank you for using the application'


# def test_prompt_for_file():
#     """ Need to test if file is "" that the
#     return is 'Please enter a filename: '
#     """
#     with mock.patch.object(__builtin__, 'input', lambda: ''):
#         assert prompt_for_file.function() == 'Please enter a filename: '


# def test_display_menu_inputs_1():
#     # assert menu.aws_host == 'Input Needed'
#     # os.system('aws ec2 delete-security-group --group-name securegroup')
#     input_values = ['1', 'testhost', '4', 'securegroup', '6', 'testdb', '7', 'dbtestinstance', '8', '50', '11',  'testuser', '12', "password", '14', 'testgroup-key', 'q']

#     def mock_input(s):
#         return input_values.pop(0)

#     menu.input = mock_input
#     menu.display_menu()

    # assert menu.aws_host == 'testhost'


# def test_display_menu_inputs_1(capsys):

#     input_values = ['1']

#     def mock_input(s):
#         return input_values.pop(0)

#     menu.input = mock_input
#     out, err = capsys.readouterr()

#     assert err == ''
#     assert out == 'Enter a file name (press enter to select default ec2_host): '


# def test_prompt_for_file_empty():
#     input_values = ['', 'test_2']

#     def mock_input(s):
#         return input_values.pop(0)

#     Aws_deploy.input = mock_input
#     prompt1 = prompt_for_file()
#     prompt2 = prompt_for_file()

#     assert prompt1 == 'Please enter a filename: '
#     assert prompt2 == 'test_2'


# def test_read_template_correct_type():
#     """
#     """
#     input_values = 'testType'

#     read_template(input_values)
#     assert True


# def test_read_template_wrong_type():
#     """
#     """
#     input_values = 'wrongType'
#     with pytest.raises(IOError) as e:
#             read_template(input_values)
#     assert e.type == IOError


# def test_read_template_exit():
#     """
#     """
#     input_values = 'exit'
#     with pytest.raises(SystemExit) as e:
#             read_template(input_values)
#     assert e.type == SystemExit

# def test_run_template():
#     """
#     """


# def test_prompt_the_user():
#     """This will test taking in a template,
#     """
#     pass
