import string
import sys

def new_var(vars):
    """
    Create a new unique variable and append it to the variables list.
    """
    # generate a list of all capitol letters
    all_letters = list(string.ascii_uppercase)

    # find the first letter not in vars
    for letter in all_letters:
        if letter not in vars:
            vars.append(letter)
            return letter

    # append ints after the letter to ensure there will be a valid var to return
    n = 0
    while True:
        new_var = f"_{n}"
        if new_var not in vars:
            vars.append(new_var)
            return new_var
        n += 1

def check_proper_form(cfl):
    """
    Helper function that will be used to check if cfl is valid. If it's not valid, don't
    continue the program. 
    NOTE: only checks if there is multiple start rules for now but may include other
    functions in future.
    """

    #check to see if start_state contains more than one element and if so, this is
    # incorrect format and terminate program.
    if type(cfl.start_var) is list:
        if len(cfl.start_var) > 1:
            print("Error in CFG input")
            # TODO: instead of exiting, send an invalid input report with the input_file_path
            # then continue to the next file in the input-CFLs directory.
            sys.exit()