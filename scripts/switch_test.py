import pytest
from switch_connect import interface


def get_con():
    return interface

def tests_con():
    assert get_con()[0] == 'ssh admin:cisco@192.168.1.254 -p 2241'
    assert get_con()[1] == 'ssh cisco:cisco@192.168.2.254 -p 30022'