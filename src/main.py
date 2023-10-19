import sys
import os
import json

class CFL:
    """
    Data structure for the input and output context-free-languages
    """
    def __init__(self, variables, terminals, production_rules, start_state):
        self.variables = variables
        self.terminals = terminals
        self.production_rules = production_rules
        self.start_state = start_state

    def create_unique_variable():
        pass



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



# TODO: delete print statements once program is finished
# Print statements have been included to allow us to see the change
# from our conversions without opening the input and output files
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


    # loop through all the input files in the input_CFLs directory
    for filename in os.listdir(current_input_directory):
        output_file_path = os.path.join(current_output_directory, filename)

        input_file_path = os.path.join(current_input_directory, filename)

        if not os.path.isfile(input_file_path):
            print("file at " + input_file_path + " is not of JSON file format")
        else:
            os.chmod(input_file_path, 0o777)
            cfl = import_JSON(input_file_path)

            print("input_CFL: ")
            print(cfl.variables)
            print(cfl.terminals)
            print(cfl.production_rules)
            print(cfl.start_state)

            convert_cfl(cfl)

            print("output_CFL: ")
            print(cfl.variables)
            print(cfl.terminals)
            print(cfl.production_rules)
            print(cfl.start_state)

            export_JSON(cfl, output_file_path)


def newVariable(variables):
    """
    Create a new unique variable and append it to the variables list.
    Note: This function currently finds a variable of the form "Xn" where n
    is an integer greater than or equal to zero.
    TODO: change this function to create a unique single character symbol
    at least up to the whole 26 letter alphabet.
    """
    var = "X"
    i = 0
    while (var + i) in variables:
        i+=1
    variables.append(var + i)

def new_start_rule(cfl):
    print()
    print("new start rule")
    
    counter = 0
    if (cfl.start_state[0] + "_" + str(counter)) == cfl.start_state:
        counter += 1
    
    new_start_string = cfl.start_state[0] + "_" + str(counter)
    cfl.production_rules.insert(0, dict(LHS = new_start_string, RHS = list(cfl.start_state)))

    cfl.start_state = new_start_string
    cfl.variables.append(new_start_string)
    

    print("created start rule")
    print()
    return cfl

def test_for_errors(cfl):
    """
    Helper function that will be used to check if cfl is valid. If it's not valid, don't continue the program. 
    NOTE: only checks if there is multiple start rules for now but may include other functions in future.
    """

    #check to see if start_state contains more than one element and if so, this is incorrect format and terminate program.
    if type(cfl.start_state) is list:
        if len(cfl.start_state) > 1:
            print("Error in CFG input")
            sys.exit()

def convert_cfl(cfl):
    """
    Helper function for main()
    Convert the CFL obj into Chomsky Normal Form
    """
    try:
        
        # NOTE: it's unconventional to have integers as terminals/non-terminals, but it's still possible.
        # in addition, uppercase terminals and lowercase variables are possible aswell.

        test_for_errors(cfl)

        new_start_rule(cfl)
        

        # TODO: call eliminate_useless_rules)()

        # TODO: call eliminate_epsilons()

        # TODO: call eliminate_unit_productions)()

        # TODO: call eliminate_terminal_nonterminal()

        # TODO: call eliminate_nonterminal_groups()

    except TypeError as e:
        print("Mismatch type detected: " + e)
        sys.exit()

    except AttributeError as e:
        print("Invalid key in data: " + e)
        sys.exit()

if __name__ == "__main__":
    main(os.getcwd())
