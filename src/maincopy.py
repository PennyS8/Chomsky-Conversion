import sys
import os
import json
# conversion operation files
from start_variable import add_new_start_rule
from useless_rules import remove_useless_rules
from epsilon_products import remove_epsilons
from unit_products import remove_unit_products
from terminal_products import isolate_terminals
from nonterminal_groups import remove_nonterminal_groups
# helper function files:
from helper import ne


class CFL:
    """
    Data structure for the input and output context-free-languages
    """
    def __init__(self, vars, terminals, rules, start_var):
        self.vars = vars
        self.terminals = terminals
        self.rules = rules
        self.start_var = start_var

    def create_unique_var():
        pass



# TODO: delete print statements once program is finished
# Print statements have been included to allow us to see the change
# from our conversions without opening the input and output files
def main(current_path):
    """"
    Main function will convert all CFL files within the input_CFLs directory
    Then store the output into the output_CFLs directory with the same file
    name as the input CFL file
    """
    input_dir = "input_CFLs"
    output_dir = "output_CFLs"

    curr_input_dir = os.path.join(current_path, input_dir)
    curr_output_dir = os.path.join(current_path, output_dir)

    curr_input_dir = os.path.join(current_path, input_dir)
    curr_output_dir = os.path.join(current_path, output_dir)

    # loop through all the input files in the input_CFLs directory
    for filename in os.listdir(curr_input_dir):
        output_file_path = os.path.join(curr_output_dir, filename)
        input_file_path = os.path.join(curr_input_dir, filename)

        if not os.path.isfile(input_file_path):
            print("file at " + input_file_path + " is not of JSON file format")
        else:
            os.chmod(input_file_path, 0o777)
            cfl = import_JSON(input_file_path)

            print("input_CFL: ")
            print(cfl.vars)
            print(cfl.terminals)
            print(cfl.rules)
            print(cfl.start_var)

            convert_cfl(cfl)

            print("output_CFL: ")
            print(cfl.vars)
            print(cfl.terminals)
            print(cfl.rules)
            print(cfl.start_var)

            export_JSON(cfl, output_file_path)



def convert_cfl(cfl):
    """
    Helper function for main()
    Convert the CFL obj into Chomsky Normal Form
    """
    try:

        # NOTE: it's unconventional to have integers as terminals/non-terminals, but it's still possible.
        # in addition, uppercase terminals and lowercase variables are possible aswell.

        test_for_errors(cfl)

        add_new_start_rule(cfl)

        # TODO: call remove_useless_rules(cfl)

        remove_epsilons(cfl)

        # TODO: call remove_unit_products(cfl)

        # TODO: call isolate_terminals(cfl)

        # TODO: call remove_nonterminal_groups(cfl)

    # TODO: instead of exiting, send an invalid input report with the input_file_path
    # then continue to the next file in the input-CFLs directory.
    except TypeError as e:
        print("Mismatch type detected: " + e)
        sys.exit()

    except AttributeError as e:
        print("Invalid key in data: " + e)
        sys.exit()



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
    if os.path.exists(output_file_path):
        print("Warning: Output file at: " + output_file_path + " already existed, and is now overwritten")
    with open(output_file_path, "w") as file:
        json.dump(output_cfl.__dict__, file, indent=4)



def test_for_errors(cfl):
    """
    Helper function that will be used to check if cfl is valid. If it's not valid, don't continue the program. 
    NOTE: only checks if there is multiple start rules for now but may include other functions in future.
    """

    #check to see if start_state contains more than one element and if so, this is incorrect format and terminate program.
    if type(cfl.start_var) is list:
        if len(cfl.start_var) > 1:
            print("Error in CFG input")
            sys.exit()

if __name__ == "__main__":
    main(os.getcwd())
