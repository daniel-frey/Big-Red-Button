import pytest
import Aws_deploy


def test_welcome(capsys):
    """
    """
    Aws_deploy.welcome()
    captured = capsys.readouterr()
    assert captured.startswith('Welcome to our AWS deployment helper. \n')


def test_read_file():
    """
    """
    contents = Aws_deploy.read_file('../templates/ec2instance_template.json')
    assert contents.startswith('Make Me A Video Game!')
