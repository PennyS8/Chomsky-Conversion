import sys
import json
import os

class CFL:
    """
    Data structure for the input and output context-free-languages
    """
    def __init__(self, vars, terminals, rules, start_var):
        self.vars = vars
        self.terminals = terminals
        self.rules = rules
        self.start_var = start_var

def import_JSON(input_file_path):
    """
    Creates a CFL object from a JSON file

    Args:
        input_file_path (string): filepath location + file name
    """
    try:
        file = open(input_file_path, "r")
    except OSError:
        print ("Could not open/read file: " + input_file_path)
        sys.exit()

    try:
        dict = json.load(file)
    except json.JSONDecodeError as e:
        print("Invalid JSON syntax or file is not of type JSON: ", e)
        sys.exit()

    try:
        input_cfl = CFL(dict["vars"],
                        dict["terminals"],
                        dict["rules"],
                        dict["start_var"])
    except KeyError as e:
        print("Missing key in file: " + input_file_path + ": " + e)
        sys.exit()

    return input_cfl

def export_JSON(output_cfl, output_file_path):
    """
    Creates a JSON file from CFL object
    Note: will overwrite existing file if the filename already exists,

    Args:
        output_cfl (json dictionary): cfl data that will be exported.
        output_file_path (string): filepath location where modified
        data should be stored.
    """
    file_name = os.path.basename(output_file_path)

    if os.path.exists(output_file_path):
        sys.stdout.write("Warning!: Output file " + file_name +
            " was overwritten\n")

    with open(output_file_path, "w") as file:
        json.dump(output_cfl.__dict__, file, indent=4)