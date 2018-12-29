import mock
import pytest
from . import Aws_deploy
from .Aws_deploy import greet_user, read_template, prompt_for_file
from .file_io import read_file, write_file


def test_cc_import():
    assert greet_user


# def test_greet_user(capsys):
#     """
#     """
#     greet_user()
#     captured = capsys.readouterr()
    # assert captured.out == 'AWS Deployment automation\nYou will need to have some prerequisites before you are able to begin\nYou will receive a series of prompts. Please read the questions carefully\nOnce the questions have finished, a json file will be written that will be used for deployment\nTo exit at any time, type "quit".\n'


# def test_prompt_for_file():
#     """ Need to test if file is "" that the
#     return is 'Please enter a filename: '
#     """
#     with mock.patch.object(__builtin__, 'input', lambda: ''):
#         assert prompt_for_file.function() == 'Please enter a filename: '


def test_prompt_for_file_filled(capsys):
    input_values = ['test']

    def mock_input(s):
        return input_values.pop(0)

    Aws_deploy.input = mock_input

    # prompt_for_file.main()
    prompt_for_file()
    out, err = capsys.readouterr()

    assert out == 'test'
    # assert err == ''


def test_prompt_for_file_empty(capsys):
    input_values = ['']

    def mock_input(s):
        return input_values.pop(0)

    Aws_deploy.input = mock_input

    # prompt_for_file.main()
    prompt_for_file()
    out, err = capsys.readouterr()

    assert out == 'Please enter a filename: '
    # assert err == ''


def test_read_template_exit():
    """
    """
    pass
#     with pytest.raises(SystemExit) as e:
#             mymodule.will_exit_somewhere_down_the_stack()
#     assert e.type == SystemExit



# def test_run_template():
#     """
#     """


def test_prompt_the_user():
    """This will test taking in a template,
    """
    pass
