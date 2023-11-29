import re

def remove_epsilons(cfl):
    """
    Remove all products that terminate to epsilon, except the start variable
    
    Args:
        cfl (json dictionary): dictionary of 4 tuple cfl
    """
    e_set = set() # set of variables that terminate to epsilon
    
    find_epsilon(cfl, e_set)

    e_list = list(e_set)

    # filters cfl rules to contain non epsilons on RHS.
    # However, if the only value on RHS is epsilon,
    # because we don't want to remove variable that is part of the set.
    cfl.rules = non_epsilon_list(cfl)

    visited = []

    move_epsilon(cfl, visited, e_list)


    # There is a possibility that the LHS of rule may not be accessed
    # yet due to epsilon transition moving to another location,
    # so we track LHS and see if it hasn't been visited yet and cycle
    # through the function calls in a for loop to make sure that all
    # epsilon transitions that are pointing to variables other than
    # starting variable gets removed/moved to different location (and
    # cycle again).
    for rule in cfl.rules:
        for LHS in rule["LHS"]:
            if LHS not in visited and rule["LHS"] != cfl.start_var:

                loop_e_set = set()
                find_epsilon(cfl, loop_e_set)

                loop_e_list = list(loop_e_set)

                cfl.rules = non_epsilon_list(cfl)

                move_epsilon(cfl, visited, loop_e_list)

    # remove rules that contain no products and their variables in other
    # rules' products, and in the variables list
    remove_empty_rules(cfl)

    final_results(cfl)


def remove_empty_rules(cfl):
    """
    Remove rules with no products and remove the LHS
    variable from the vars list
    
    Args:
        cfl (json dictionary): dictionary of 4 tuple cfl
    """
    # this will iterate for the maximum amount possible for there to be a chain
    # of empty rules removed due to epsilon removals and rule simplifications
    for _ in range(len(cfl.vars)):
        # creates a list of the rules that have no products
        empty_rules = [rule for rule in cfl.rules if len(rule["RHS"]) == 0]

        for rule in empty_rules:
            # Remove the LHS variable from the vars list
            if rule["LHS"] in cfl.vars:
                cfl.vars.remove(rule["LHS"])

            # Remove products that contain the LHS variable
            for other_rule in cfl.rules:
                updated_rhs = []
                for product in other_rule["RHS"]:
                    if rule["LHS"] not in product:
                        updated_rhs.append(product)
                other_rule["RHS"] = updated_rhs

            # Remove the empty rule from the cfl rules
            cfl.rules.remove(rule)

def move_epsilon(cfl, visited, e_list):
    """
    Function that checks RHS of rules to see if epsilon exists, and if so
    retrieve the pointer to the Variable to access rules contained
    in that and append it.

    Args:
        cfl (json dictionary): dictionary of 4 tuple cfl
        visited (list): list of all Variables visited so far
        e_list (list): list that contains Variables whose rule includes an
                        epsilon transition 
    """

    # if a rule has a product with a variable in e_list, then duplicate that
    # production excluding the epsilon terminating variable
    for rule in cfl.rules:
        for product in rule["RHS"]:
            # does this product contain a variable that is epsilon terminating
            for et_var in e_list: # et_var (Epsilon Terminating VARiable)
                if et_var in product:
                    # duplicate the product excluding the var in child_var
                    new_product = re.sub(et_var, "", product)
                    if new_product not in rule["RHS"]:
                        rule["RHS"].append(new_product)
                        if et_var not in visited:
                            visited.append(et_var)

def find_epsilon(cfl, e_set_list):
    """
    Function that finds epsilon from rule and stores the Variable that
    has the epsilon into a list to be referenced for other filters.
    Will also pop the epsilon from the rule as per Chomsky Normal Rule requires.

    Args:
        cfl (json dictionary): dictionary of 4 tuple cfl
        e_list (list): list that contains Variables whose rule includes an epsilon transition 
    """
    # find variables that terminate to epsilon
    for rule in cfl.rules:
        if rule["LHS"] != cfl.start_var: # start var exception
            for i, product in enumerate(rule["RHS"]):
                if product == "":
                    # append the variable to e_list to substitute it later
                    e_set_list.add(rule["LHS"])
                    rule["RHS"].pop(i) # remove item from the product list

def non_epsilon_list(cfl):
    """
    Function that creates a list containing rules excluding epsilons.

    Args:
        cfl (json dictionary): dictionary of 4 tuple cfl
    """
    results = []
    for rule in cfl.rules:
        if len(rule["RHS"]) == 0:
            results.append(rule)
        if rule["RHS"]:
            results.append(rule)
    
    return results

def final_results(cfl):
    """
    Filter that removes all epsilon transitions excluding
    starting variable. This should only be called at the very end
    after epsilon transitions have been modified.

    Args:
        cfl (json dictionary): dictionary of 4 tuple cfl
    """
    for rule in cfl.rules:
        results = []
        if rule["LHS"] != cfl.start_var:
            for elements in rule["RHS"]:
                if elements != "":
                    results.append(elements)
            
            #find the index to update with recent data
            index = cfl.rules.index(rule)
            cfl.rules[index]["RHS"] = results