from helper import new_var
from helper import product_to_list

def isolate_terminals(cfl):
    """
    Function that sub out terminals for a new variable that terminates only to that terminal

    Args:
        cfl (json dictionary): dictionary of 4 tuple cfl
    """

    # creates dict of terminals w/ a var that terminates only to that terminal
    tt_dict = {} # the terminal terminating dictionary (python hashmap)

    new_rules = [] # List to store the rules to add at the end

    # add dictionary entries for all unaccounted for terminals
    for term in cfl.terminals:
        if term not in tt_dict:
            tt_dict[term] = new_var(cfl.vars)
            new_rules.append({"LHS": tt_dict[term], "RHS": [term]})

    # substitute every terminal in rule["RHS"] for its tt_dict variable
    for rule in cfl.rules:
        for i, product in enumerate(rule["RHS"]):
            
            # splits up the product into a list by its variable/terminals
            product_list = product_to_list(product)

            if len(product_list) == 1: # edge case checker
                continue # skip this product, no modifications needed

            # substitute the terminals with the respective tt_var
            for j, item in enumerate(product_list):
                if item in cfl.terminals: # verify item is a terminal
                    product_list[j] = tt_dict[item] # perform the substitution
            
            # finalize substitutions made
            rule["RHS"][i] = "".join(product_list)

    # append the substitution rules to the set of rules in our cfl
    cfl.rules.extend(new_rules)
