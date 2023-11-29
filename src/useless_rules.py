import string
from helper import product_to_list

def remove_useless_rules(cfl):
    """
    Remove variables that don't generate anything. Then remove variables that
    are unreachable from start symbol.
    """
    # remove products with vars/terminals that are not in var/terminal list
    for rule_dict in cfl.rules:
        for right_rule in rule_dict["RHS"]:
            # splits up the product into a list by its variable/terminals
            product_list = product_to_list(right_rule)

            if len(product_list) == 0: # check for epsilon edge case
                right_rule == ""

            # remove product if it contains invalid var or terminal
            for symbol in product_list:
                if symbol not in cfl.vars and symbol not in cfl.terminals:
                    rule_dict.remove(right_rule)

    # Function that looks at all the variables from LHS, check if variable
    # are part of variable set, and if not remove.
    for rule_dict in cfl.rules:
        for left_rule in rule_dict["LHS"]:
            if left_rule not in cfl.vars:
                cfl.rules.remove(rule_dict)


    # Remove variables that don't generate anything. Then remove variables that
    # are unreachable from the start symbol.
    reachable_vars = set([cfl.start_var])  # Initialize with the start variable

    # Iterate until no new reachable variables are found
    while True:
        num_reachable_vars = len(reachable_vars)

        for rule_dict in cfl.rules:
            lhs = rule_dict["LHS"]

            # If the LHS is reachable or it appears in the product of a
            # reachable variable's rule, mark it as reachable
            if lhs in reachable_vars:
                reachable_vars.add(lhs)
            else:
                # Check each product in the RHS for the LHS variable
                for product in rule_dict["RHS"]:
                    if lhs in product_to_list(product):
                        reachable_vars.add(lhs)
                        # we've found a reachable symbol in the RHS, break
                        break 

        # Break the loop if no new reachable variables are found
        if len(reachable_vars) == num_reachable_vars:
            break

    # Remove rules with unreachable LHS using a for loop
    new_rules = []
    for rule_dict in cfl.rules:
        if rule_dict["LHS"] in reachable_vars:
            new_rules.append(rule_dict)

    cfl.rules = new_rules

    # Remove variables that don't generate anything using a for loop
    new_vars = []
    for var in cfl.vars:
        if var in reachable_vars:
            new_vars.append(var)

    cfl.vars = new_vars