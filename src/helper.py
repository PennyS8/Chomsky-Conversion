import string

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

    # append ints if we run out of letters
    n = 0
    while True:
        new_var = f"_{n}"
        if new_var not in vars:
            vars.append(new_var)
            return new_var
        n += 1

def check_proper_form(cfl):
    '''
    Check if the input CFL is in proper CFL form, if not raise an exception.
    '''
    # TODO: update this fn with more checks
    # Check start_state contains no more than one element
    if type(cfl.start_var) is list:
        if len(cfl.start_var) > 1:
            raise ValueError("Input CFL is not in proper form: " +
                            "There is more than one start variable")