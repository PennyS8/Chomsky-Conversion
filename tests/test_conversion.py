import pytest

from src.main import *

@pytest.fixture()
def example_CFG():
    return CFL(["V", "W", "S"],
                ["a", "b"],
                [   {"LHS": "S", "RHS": ["_epsilon_", "V", "aSb"]},
		            {"LHS": "V", "RHS": ["aW", "Wb"]},
		            {"LHS": "W", "RHS": ["_epsilon_", "a", "b"]}],
                "S")

def test_import_JSON():
    input_file_path = "input_CFLs/example.json"
    cfl = import_JSON(input_file_path)
    assert cfl.variables == ["V", "W", "S"]
    assert cfl.terminals == ["a", "b"]
    assert cfl.production_rules == [{"LHS": "S", "RHS": ["_epsilon_", "V", "aSb"]},
		                            {"LHS": "V", "RHS": ["aW", "Wb"]},
		                            {"LHS": "W", "RHS": ["_epsilon_", "a", "b"]}]
    assert cfl.start_state == "S"

def test_export_JSON(example_CFG):
    output_file_path = "output_CFLs/example.json"
    export_JSON(example_CFG, output_file_path)
    # since we already proved that import_JSON works we can use it to
    # prove export_JSON works
    cfl = import_JSON(output_file_path)
    assert cfl.variables == ["V", "W", "S"]
    assert cfl.terminals == ["a", "b"]
    assert cfl.production_rules == [{"LHS": "S", "RHS": ["_epsilon_", "V", "aSb"]},
		                            {"LHS": "V", "RHS": ["aW", "Wb"]},
		                            {"LHS": "W", "RHS": ["_epsilon_", "a", "b"]}]
    assert cfl.start_state == "S"
