import pytest

from src import main
from src.main import *


# fixture is not equal to cfl object, both test_conversion2 and test_conversion1 should pass
@pytest.fixture()
def example_CFG():
    return main.CFL(["V", "W", "S"],
                    ["a", "b"],
                    [   {"LHS": "S", "RHS": ["_epsilon_", "V", "aSb"]},
		                {"LHS": "V", "RHS": ["aW", "Wb"]},
		                {"LHS": "W", "RHS": ["_epsilon_", "a", "b"]}],
                    "S")


def test_conversion1():
    input_file_path = "input_CFLs/example.json"
    cfl = import_JSON(input_file_path)
    assert cfl.variables == ["V", "W", "S"]
    assert cfl.terminals == ["a", "b"]
    assert cfl.production_rules == [{"LHS": "S", "RHS": ["_epsilon_", "V", "aSb"]},
		                            {"LHS": "V", "RHS": ["aW", "Wb"]},
		                            {"LHS": "W", "RHS": ["_epsilon_", "a", "b"]}]
    assert cfl.start_state == "S"

def test_conversion2():
    input_file_path = "input_CFLs/example.json"
    cfl = import_JSON(input_file_path)
    assert cfl == example_CFG
