import string

def new_var(vars):
    """
    Create a new unique variable and append it to the variables list.
    Note: new_var does not have a rule be default
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
    # Check if all required keys are present
    required_keys = ["vars", "terminals", "rules", "start_var"]
    for key in required_keys:
        if key not in cfl.__dict__:
            raise ValueError(f"Input CFL is not in proper form: " + 
                        "Missing key '{key}'")

    # Check variable types
    if (not isinstance(cfl.vars, list) or
        not isinstance(cfl.terminals, list) or
        not isinstance(cfl.rules, list) or
        not isinstance(cfl.start_var, str)):
        raise ValueError("Input CFL is not in proper form: " + 
                        "Incorrect variable types")

    # Check rule format
    for rule in cfl.rules:
        if not isinstance(rule, dict) or \
            "LHS" not in rule or \
            "RHS" not in rule or \
            not isinstance(rule["LHS"], str) or \
            not isinstance(rule["RHS"], list):
            raise ValueError("Input CFL is not in proper form: " + 
                            "Incorrect rule format")

    # Check start variable format
    if len(cfl.start_var) != 1:
        raise ValueError("Input CFL is not in proper form: " + 
                        "Start variable should have exactly one element")

    # Check if variables and terminals lists are comprehensive
    used_vars = set()
    used_terminals = set()

    for rule in cfl.rules:
        used_vars.add(rule["LHS"])
        for symbol in rule["RHS"]:
            if symbol.isalpha():
                used_vars.add(symbol)
            else:
                used_terminals.add(symbol)

    if set(cfl.vars) != used_vars:
        raise ValueError("Input CFL is not in proper form: " + 
                        "Variables list is not comprehensive")

    if set(cfl.terminals) != used_terminals:
        raise ValueError("Input CFL is not in proper form: " + 
                        "Terminals list is not comprehensive")

    # Check for duplicate elements in variables and terminals lists
    if len(cfl.vars) != len(set(cfl.vars)):
        raise ValueError("Input CFL is not in proper form: " + 
                        "Duplicate elements in the variables list")

    if len(cfl.terminals) != len(set(cfl.terminals)):
        raise ValueError("Input CFL is not in proper form: " + 
                        "Duplicate elements in the terminals list")

def product_to_list(product):
    '''
    splits up the product by its variables/terminals and returns the list
    '''
    element_list = []
    current_element = ""
    # spilt up by start of each element is a letter
    for char in product:
        if char.isalpha():
            if current_element:
                element_list.append(current_element)
            current_element = char
        else:
            current_element += char
    # append the last element if the string ends with a symbol
    if current_element:
        element_list.append(current_element)

    return element_list