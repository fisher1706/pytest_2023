# https://www.codementor.io/@adammertz/writing-a-simple-pytest-hook-zc5wvoj5t
import pytest


def test_passed_three():
    assert True


# @pytest.mark.skip
def test_failed_two_three():
    assert False
