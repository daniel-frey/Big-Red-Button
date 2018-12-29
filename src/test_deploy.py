
import pytest
from . import Aws_deploy
from .Aws_deploy import greet_user, read_template, prompt_for_file
from .file_io import read_file, write_file


def test_cc_import():
    assert greet_user


def test_greet_user():
    """
    """
    greet_user()
    assert True


# def test_prompt_for_file():
#     """ Need to test if file is "" that the
#     return is 'Please enter a filename: '
#     """
#     with mock.patch.object(__builtin__, 'input', lambda: ''):
#         assert prompt_for_file.function() == 'Please enter a filename: '


def test_prompt_for_file_filled():
    input_values = ['test']

    def mock_input(s):
        return input_values.pop(0)

    Aws_deploy.input = mock_input
    prompt = prompt_for_file()

    assert prompt == 'test'


# def test_prompt_for_file_empty():
#     input_values = ['', 'test_2']

#     def mock_input(s):
#         return input_values.pop(0)

#     Aws_deploy.input = mock_input
#     prompt1 = prompt_for_file()
#     prompt2 = prompt_for_file()

#     assert prompt1 == 'Please enter a filename: '
#     assert prompt2 == 'test_2'


def test_read_template_correct_type():
    """
    """
    input_values = 'testType'

    read_template(input_values)
    assert True


# def test_read_template_wrong_type():
#     """
#     """
#     input_values = 'wrongType'
#     with pytest.raises(IOError) as e:
#             read_template(input_values)
#     assert e.type == IOError


def test_read_template_exit():
    """
    """
    input_values = 'exit'
    with pytest.raises(SystemExit) as e:
            read_template(input_values)
    assert e.type == SystemExit

# def test_run_template():
#     """
#     """


def test_prompt_the_user():
    """This will test taking in a template,
    """
    pass
