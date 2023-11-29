import os

# conversion operation files:
from start_variable import new_start_rule
from epsilon_products import remove_epsilons
from useless_rules import remove_useless_rules
from unit_products import remove_unit_products
from terminal_products import isolate_terminals
from variable_groups import remove_variable_groups
from duplicate_rules import remove_duplicate_rules

# helper functions:
from JSON_dictionary import import_JSON
from JSON_dictionary import export_JSON
from helper import check_proper_form

def main(current_path):
    """
    Main function will convert all CFL files within the input_CFLs directory
    Then store the output into the output_CFLs directory with the same file
    name as the input CFL file

    Args:
        current_path (string): filepath where program is running from. Important
                                when trying to access other files in folder and needing
                                to reference a location.
    """
    input_dir = "input_CFLs"
    output_dir = "output_CFLs"

    current_input_dir = os.path.join(current_path, input_dir)
    current_output_dir = os.path.join(current_path, output_dir)

    current_input_dir = os.path.join(current_path, input_dir)
    current_output_dir = os.path.join(current_path, output_dir)

    # loop through input_CFLs directory and convert the CFG's to CNF
    for filename in os.listdir(current_input_dir):
        output_file_path = os.path.join(current_output_dir, filename)
        input_file_path = os.path.join(current_input_dir, filename)

        if not os.path.isfile(input_file_path):
            print("File at " + input_file_path + " is not of JSON file format")
        else:
            os.chmod(input_file_path, 0o777)

            # import JSON file as a python dictionary
            cfl = import_JSON(input_file_path)

            try:
                check_proper_form(cfl) # not whole encompasing
            except ValueError as e:
                print(f"Error in file {filename}: {e}")
                continue

            # the primary conversion steps to CNF as functions:
            new_start_rule(cfl)
            remove_useless_rules(cfl)
            remove_epsilons(cfl)
            remove_unit_products(cfl)
            isolate_terminals(cfl)
            remove_variable_groups(cfl)
            
            # additional operation to simplify output
            remove_duplicate_rules(cfl)

            # export python dictionary as a JSON file
            export_JSON(cfl, output_file_path)

if __name__ == "__main__":
    main(os.getcwd())