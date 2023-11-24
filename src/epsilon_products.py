import re

def remove_epsilons(cfl):
    """
    Remove all products that terminate to epsilon
    Note: that if the grammar accepts the empty string there must be an epsilon in the
    start state's production rule.
    """
    e_set = set() # set of variables that terminate to epsilon
    
    # find variables that terminate to epsilon
    for rule in cfl.rules:
        if rule["LHS"] != cfl.start_var: # exception is made for the start state
            for i, product in enumerate(rule["RHS"]):
                if "_epsilon_" in product:
                    # append the variable to e_list to substitute it later
                    e_set.add(rule["LHS"])
                    rule["RHS"].pop(i) # remove item from the product list

    e_list = list(e_set)

    # if a rule has a production with a variable in e_list, then duplicate that
    # production excluding the epsilon terminating variable
    for rule in cfl.rules:
        for product in rule["RHS"]:
            # does this product contain a variable that would terminate to epsilon
            for et_var in e_list: # et_var (Epsilon Terminating VARiable)
                if et_var in product:
                    # duplicate the product excluding the var in child_var
                    new_product = re.sub(et_var, "", product, count=1)
                    if len(new_product) != 0 and new_product not in rule["RHS"]:
                        rule["RHS"].append(new_product)