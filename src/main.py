import sys
import os
import json

class CFL:
    '''
    Data structure for the input and output context-free-languages
    '''
    def __init__(self, variables, terminals, production_rules, start_state):
        self.variables = variables
        self.terminals = terminals
        self.production_rules = production_rules
        self.start_state = start_state

    def create_unique_variable():
        pass



def import_JSON(input_file_path):
    '''
    Creates a CFL object from a JSON file
    '''
    try:
        file = open(input_file_path, 'r')
    except OSError:
        print ('Could not open/read file: ' + input_file_path)
        sys.exit()

    try:
        dict = json.load(file)
    except json.JSONDecodeError as e:
        print("Invalid JSON syntax or file is not of type JSON: ", e)
        sys.exit()

    try:
        input_cfl = CFL(dict['variables'],
                        dict['terminals'],
                        dict['production_rules'],
                        dict['start_state'])
    except KeyError as e:
        print('Missing key in file: ' + input_file_path + ': ' + e)
        sys.exit()

    return input_cfl



def export_JSON(output_cfl, output_file_path):
    '''
    Creates a JSON file from CFL object
    Note: it will not create a file if the file already exists,
    but instead will overwrite existing file with that file name.
    '''
    if os.path.exists(output_file_path):
        print('Warning: Output file at: ' + output_file_path + ' already existed, and is now overwritten')
    with open(output_file_path, 'w') as file:
        json.dump(output_cfl.__dict__, file, indent=4)



# TODO: delete print statements once program is finished
# Print statements have been included to allow us to see the change
# from our conversions without opening the input and output files
def main():
    '''
    Main function will convert all CFL files within the input_CFLs directory
    Then store the output into the output_CFLs directory with the same file
    name as the input CFL file
    '''
    input_directory = 'input_CFLs'
    output_directory = 'output_CFLs'

    # loop through all the input files in the input_CFLs directory
    for filename in os.listdir(input_directory):

        output_file_path = os.path.join(output_directory, filename)

        input_file_path = os.path.join(input_directory, filename)
        if not os.path.isfile(input_file_path):
            print('file at ' + input_file_path + ' is not of JSON file format')
        else:
            cfl = import_JSON(input_file_path)

            print('input_CFL: ')
            print(cfl.variables)
            print(cfl.terminals)
            print(cfl.production_rules)
            print(cfl.start_state)

            convert_cfl(cfl)

            print('output_CFL: ')
            print(cfl.variables)
            print(cfl.terminals)
            print(cfl.production_rules)
            print(cfl.start_state)

            export_JSON(cfl, output_file_path)



def convert_cfl(cfl):
    '''
    Helper function for main()
    Convert the CFL obj into Chomsky Normal Form
    '''
    try: pass
        # TODO: call new_start_rule()

        # TODO: call eliminate_useless_rules)()

        # TODO: call eliminate_epsilons()

        # TODO: call eliminate_unit_productions)()

        # TODO: call eliminate_terminal_non-terminal()

        # TODO: call eliminate_non-terminal_groups()

    except TypeError as e:
        print("Mismatch type detected: " + e)
        sys.exit()

    except AttributeError as e:
        print("Invalid key in data: " + e)
        sys.exit()



if __name__ == '__main__':
    main()