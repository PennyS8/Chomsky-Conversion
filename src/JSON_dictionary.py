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
    Note: it will not create a file if the file already exists,
    but instead will overwrite existing file with that file name.
    """
    file_name = os.path.basename(output_file_path)

    if os.path.exists(output_file_path):
        print("\nWarning!: Output file " + file_name +
                " already existed in folder 'output_CFLs' and is now overwritten\n")

    with open(output_file_path, "w") as file:
        json.dump(output_cfl.__dict__, file, indent=4)