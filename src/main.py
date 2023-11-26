import os

# conversion operation files:
from start_variable import add_new_start_rule
from epsilon_products import remove_epsilons
from useless_rules import remove_useless_rules
from unit_products import remove_unit_products
from terminal_products import isolate_terminals
from nonterminal_groups import remove_nonterminal_groups

# helper functions:
from JSON_dictionary import import_JSON
from JSON_dictionary import export_JSON
from helper import check_proper_form

def main(current_path):
    """"
    Main function will convert all CFL files within the input_CFLs directory
    Then store the output into the output_CFLs directory with the same file
    name as the input CFL file
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
                check_proper_form(cfl)
            except ValueError as e:
                print(f"Error: {e}")
                break

            # TODO: remove print()'s once program is finished
            print("\ninput_CFL: ")
            print("  Variables: " + ", ".join(cfl.vars))
            print("  Terminals: " + ", ".join(cfl.terminals))
            print("  Production Rules: ")
            for rule in cfl.rules:
                print("    " + rule["LHS"] + " -> " + ", ".join(rule["RHS"]))
            print("  Start Variable: " + cfl.start_var)

            #add_new_start_rule(cfl)
            #remove_useless_rules(cfl)
            #remove_epsilons(cfl)
            #remove_unit_products(cfl)
            isolate_terminals(cfl)
            #remove_nonterminal_groups(cfl)

            # TODO: remove print()'s once program is finished
            print("\noutput_CFL: ")
            print("  Variables: " + ", ".join(cfl.vars))
            print("  Terminals: " + ", ".join(cfl.terminals))
            print("  Production Rules: ")
            for rule in cfl.rules:
                print("    " + rule["LHS"] + " -> " + ", ".join(rule["RHS"]))
            print("  Start Variable: " + cfl.start_var)

            # export python dictionary as a JSON file
            export_JSON(cfl, output_file_path)

if __name__ == "__main__":
    main(os.getcwd())