import string

def new_var(vars):
    """
    Create a new unique variable and append it to the variables list.
    Note: new_var does not have a rule be default
    
    Args:
        vars (list): list of unique variables in cfl
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
    """
    Check if the input CFL is in proper CFL form, if not raise an exception.

    Args:
        cfl (json dictionary): dictionary of 4 tuple cfl
    """

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
        if ("LHS" not in rule or
            "RHS" not in rule or
            not isinstance(rule, dict) or
            not isinstance(rule["LHS"], str) or
            not isinstance(rule["RHS"], list)):
            raise ValueError("Input CFL is not in proper form: " + 
                            "Incorrect rule format")

    # Check start variable format
    if len(cfl.start_var) != 1:
        raise ValueError("Input CFL is not in proper form: " + 
                        "Start variable should have exactly one element")

    # Check if vars, terminals, and rules are not empty
    if not cfl.vars or not cfl.terminals or not cfl.rules:
        raise ValueError("Input CFL is not in proper form: Empty lists")

    # Check if variables and terminals lists are comprehensive
    used_vars = set()
    used_terminals = set()

    for rule in cfl.rules:
        used_vars.add(rule["LHS"])
        for product in rule["RHS"]:
            symbol_list = product_to_list(product)
            for symbol in symbol_list:
                if symbol in cfl.vars:
                    used_vars.add(symbol)
                else:
                    used_terminals.add(symbol)

    # if not set(used_vars).issubset(set(cfl.vars)):
    #     raise ValueError("Input CFL is not in proper form: " + 
    #                     "Variables list is not comprehensive")

    if not set(used_terminals).issubset(set(cfl.terminals)):
        raise ValueError("Input CFL is not in proper form: " + 
                        "Terminals list is not comprehensive")

    # Check for duplicate elements in variables and terminals lists
    if len(cfl.vars) != len(set(cfl.vars)):
        raise ValueError("Input CFL is not in proper form: " + 
                        "Duplicate elements in the variables list")

    if len(cfl.terminals) != len(set(cfl.terminals)):
        raise ValueError("Input CFL is not in proper form: " + 
                        "Duplicate elements in the terminals list")
        
    used_vars = set()

def product_to_list(product):
    """
    splits up the product by its variables/terminals and returns the list

    Args:
        product (string): string of an element contained in RHS of particular rule
    """

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

def printCFL(cfl, name):
    """
    Prints out the contents inside cfl. Useful to call to check
    what cfl looks like before function calls vs what it looks like after.

    Args:
        cfl (json dictionary): dictionary of 4 tuple cfl
        name (string): Custom name that is used to identify cfl in its various stages.
                       Usefull when there are many print statements.

    """
    print("\n", name)
    print("  Variables: " + ", ".join(cfl.vars))
    print("  Terminals: " + ", ".join(cfl.terminals))
    print("  Production Rules: ")
    for rule in cfl.rules:
        print("    " + rule["LHS"] + " -> " + ", ".join(rule["RHS"]))
    print("  Start Variable: " + cfl.start_var)