import re

def remove_epsilons(cfl):
    """
    Remove all products that terminate to epsilon, except the start variable
    """
    e_set = set() # set of variables that terminate to epsilon
    
    findEpsilon(cfl, e_set)

    e_list = list(e_set)

    # remove rules where the entire RHS is epsilon

    #cfl.rules = [rule for rule in cfl.rules if rule["RHS"] if len(rule["RHS"]) == 0]
    cfl.rules = nonEpsilonList(cfl)

    print(cfl.rules)

    visited = []
    print("e_list", e_list)

    moveEpsilon(cfl, visited, e_list)

    print(visited)


    for rule in cfl.rules:
        for LHS in rule["LHS"]:
            if LHS not in visited and rule["LHS"] != cfl.start_var:

                loop_e_set = set()
                findEpsilon(cfl, loop_e_set)
    
                loop_e_list = list(loop_e_set)

                cfl.rules = nonEpsilonList(cfl)

                moveEpsilon(cfl, visited, loop_e_list)
    
    finalResults(cfl)
    


def moveEpsilon(cfl, visited, e_list):
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

def findEpsilon(cfl, e_set_list):
    # find variables that terminate to epsilon
    for rule in cfl.rules:
        if rule["LHS"] != cfl.start_var: # start var exception
            for i, product in enumerate(rule["RHS"]):
                if product == "":
                    # append the variable to e_list to substitute it later
                    e_set_list.add(rule["LHS"])
                    rule["RHS"].pop(i) # remove item from the product list

def nonEpsilonList(cfl):
    results = []
    for rule in cfl.rules:
        if len(rule["RHS"]) == 0:
            results.append(rule)
        if rule["RHS"]:
            results.append(rule)
    
    return results

def finalResults(cfl):
    for rule in cfl.rules:
        results = []
        if rule['LHS'] != cfl.start_var:
            for elements in rule["RHS"]:
                if elements != '':
                    results.append(elements)
            index = cfl.rules.index(rule)
            cfl.rules[index]['RHS'] = results