import unittest

from index import *
import pytest

class test_index(unittest.TestCase):

    def test_add(self):
        assert add(1, 2) == 3
        assert add(1, "asdf") == "Invalid Input"

    def test_subtract(self):
        assert subtract(1, 2) == 3
        assert subtract(1, "asdf") == "Invalid Input"

    def test_multiply(self):
        assert multiply(1, 2) == 3
        assert multiply(1, "asdf") == "Invalid Input"

    def test_divide(self):
        assert divide(1, 2) == 3 
        assert divide(1, "asdf") == "Invalid Input"

