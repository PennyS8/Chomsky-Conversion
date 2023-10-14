def main():
    pass
    # define CFL data structure
    # call import_JSON()
    # call new_start_rule()
    # call eliminate_useless_rules)()
    # call eliminate_epsilons()
    # call eliminate_unit_productions)()
    # call eliminate_terminal_non-terminal()
    # call eliminate_non-terminal_groups()
    # call export_JSON()



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
