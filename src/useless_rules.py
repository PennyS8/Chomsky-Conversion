import string
from helper import product_to_list

def remove_useless_rules(cfl):
    """
    Removes non-generating and non-reachable rules from the given
    context-free grammar.

    Args:
    - cfl (CFG): The context-free grammar to process.
    """

    for rule_dict in cfl.rules:
        for right_rule in rule_dict["RHS"]:

            # we will assume all variables are of length 1 for now and
            # check if it's upper case as that's what variables are usually.
            if len(right_rule) == 1 and right_rule in string.ascii_uppercase:
                #print(right_rule)
                checkProductionRuleRHS(cfl, rule_dict, right_rule)

    checkProductionRuleLHS(cfl)

    test = createSimpleDict(cfl.rules, cfl.vars)

    visited = [] # List to keep track of visited nodes.
    queue = [] # Initialize a queue

    bfs(visited, test, cfl.start_var, queue)

    checkReachableVariable(cfl, visited)


def bfs(visited, graph, node, queue):
    """
    Breadth-first-search algorithm used to find all reachable states based on input.
    Reference: https://favtutor.com/blogs/breadth-first-search-python to help me create
    BFS algorithm in python.

    Args:
        visited (list): list that contains all visited states from graph
        graph (dictionary): dictionary that contains all production rules.
        node (string): Current state
        queue (list): contains list of states currently in queue
    """
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) 

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    
def createSimpleDict(rules, vars):
    """
    Creates a dictionary object with variables as key values.
    This makes it simpler to perform BFS to detect reachable states.

    Args:
        rules (list): list that contains dictionary of production rules

    Returns:
        dictionary object
    """
    rule_dict = {}
    
    for rule_dicts in rules:
        for left_rule in rule_dicts["LHS"]:
            rule_dict[left_rule] = addAllVar(rule_dicts["RHS"], vars)

    return rule_dict

def checkProductionRuleRHS(cfl, rule_dict, rule_rhs):
    """
    Function that removes index from RHS if the variable is not part of
    variable set.

    Args:
        cfl (json dictionary): dictionary of 4 tuple cfl
        rule_dict (list): list of production rules
        rule_rhs (list): list of all variables from RHS.
    """
    for var in rule_rhs:
        if var not in cfl.vars:
            rule_dict["RHS"].remove(var)

def checkProductionRuleLHS(cfl):
    """
    Function that looks at all the variables from LHS, check if variables are
    part of variable set, and if not
    remove.

    Args:
        cfl (json dictionary): dictionary of 4 tuple cfl
    """
    for rule_dict in cfl.rules:
        for left_rule in rule_dict["LHS"]:
            if left_rule not in cfl.vars:
                cfl.rules.pop(cfl.rules.index(rule_dict))

def checkReachableVariable(cfl, visited):
    """
    Function that checks if LHS of production rule variables are in the list of
    visted (reachable) variables and removes them if unreachable.

    Args:
        cfl (json dictionary): dictionary of 4 tuple cfl
        visited (list): list of all variables that were reachable from the
        starting state
    """
    for rule_dict in cfl.rules:
        for left_rule in rule_dict['LHS']:

            # if LHS can't be reachable, remove from production rule
            if left_rule not in visited:
                cfl.rules.pop(cfl.rules.index(rule_dict))

                # remove from list of variables aswell
                if left_rule in cfl.vars:
                    cfl.vars.pop(cfl.vars.index(left_rule))

            # if RHS of a production rule is empty but it's still a reachable
            # state
            # then modify the production rule to have epsilon transition to
            # prevent possible errors
            # 
            # Ex: if W -> (blank) and it's still a reachable production rule
            # and part of variable list
            # then W -> ""
            if left_rule in visited and len(rule_dict['RHS']) == 0: 
                index = cfl.rules.index(rule_dict)
                cfl.rules[index]["RHS"] = [""]
    
def addAllVar(RHS_elements, vars):
    """
    Function that checks if RHS characters contain a variable
    and appends it to the list of reachable variables
    
    Arg:
        RHS_elements (list): list of strings of elements from RHS of a specific
                            production rule

    Returns:
        list of variables
    """
    reachable_var_list = []

    for element in RHS_elements:

        symbol_list = product_to_list(element)
        for symbol in symbol_list:
            if symbol in vars:
                # we have found a variable
                reachable_var_list.append(symbol)
    
    return reachable_var_list
