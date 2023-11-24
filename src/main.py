import sys
import os
import json

# conversion operation files:
from start_variable import add_new_start_rule
from epsilon_products import remove_epsilons
from useless_rules import remove_useless_rules
from unit_products import remove_unit_products
from terminal_products import isolate_terminals
from nonterminal_groups import remove_nonterminal_groups

# helper functions:
from helper import new_var
from helper import check_proper_form



class CFL:
    """
    Data structure for the input and output context-free-languages
    """
    def __init__(self, variables, terminals, production_rules, start_state):
        self.variables = variables
        self.terminals = terminals
        self.production_rules = production_rules
        self.start_state = start_state



def main(current_path):
    """"
    Main function will convert all CFL files within the input_CFLs directory
    Then store the output into the output_CFLs directory with the same file
    name as the input CFL file
    """
    input_directory = "input_CFLs"
    output_directory = "output_CFLs"

    current_input_directory = os.path.join(current_path, input_directory)
    current_output_directory = os.path.join(current_path, output_directory)

    current_input_directory = os.path.join(current_path, input_directory)
    current_output_directory = os.path.join(current_path, output_directory)

    # loop through input_CFLs directory and convert the CFG's to CNF
    for filename in os.listdir(current_input_directory):
        output_file_path = os.path.join(current_output_directory, filename)
        input_file_path = os.path.join(current_input_directory, filename)

        if not os.path.isfile(input_file_path):
            print("File at " + input_file_path + " is not of JSON file format")
        else:
            os.chmod(input_file_path, 0o777)
            
            # import JSON file as a python dictionary
            cfl = import_JSON(input_file_path)

            # TODO: remove print()'s once program is finished
            print("\ninput_CFL: ")
            print(cfl.variables)
            print(cfl.terminals)
            print(cfl.production_rules)
            print(cfl.start_state)

            convert_cfl(cfl)

            # TODO: remove print()'s once program is finished
            print("\noutput_CFL: ")
            print(cfl.variables)
            print(cfl.terminals)
            print(cfl.production_rules)
            print(cfl.start_state)

            # export python dictionary as a JSON file
            export_JSON(cfl, output_file_path)



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
        input_cfl = CFL(dict["variables"],
                        dict["terminals"],
                        dict["production_rules"],
                        dict["start_state"])
    except KeyError as e:
        print("Missing key in file: " + input_file_path + ": " + e)
        sys.exit()

    return input_cfl



def convert_cfl(cfl):
    """
    Helper function for main()
    Convert the CFL obj into Chomsky Normal Form
    """
    try:
        # NOTE: it's unconventional to have integers as variables in a CFL.

        check_proper_form(cfl)

        add_new_start_rule(cfl)

        # TODO: eliminate_useless_rules)(cfl)

        remove_epsilons(cfl)

        # TODO: eliminate_unit_productions)(cfl)

        # TODO: eliminate_terminal_nonterminal(cfl)

        # TODO: eliminate_nonterminal_groups(cfl)

    # TODO: instead of exiting, send an invalid input report with the input_file_path
    # then continue to the next file in the input-CFLs directory.
    except TypeError as e:
        print("Mismatch type detected: " + e)
        sys.exit()

    except AttributeError as e:
        print("Invalid key in data: " + e)
        sys.exit()



def export_JSON(output_cfl, output_file_path):
    """
    Creates a JSON file from CFL object
    Note: it will not create a file if the file already exists,
    but instead will overwrite existing file with that file name.
    """
    if os.path.exists(output_file_path):
        print("Warning: Output file at: " + output_file_path +
                " already existed, and is now overwritten")
    with open(output_file_path, "w") as file:
        json.dump(output_cfl.__dict__, file, indent=4)



if __name__ == "__main__":
    main(os.getcwd())
