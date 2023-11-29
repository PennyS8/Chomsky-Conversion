from helper import product_to_list
from unit_products import remove_unit_products

def simplify_rules(cfl):
    """
    Remove duplicate rules (rules with the same LHS and RHS) from the CFL.
    Additionally, remove unused variables and, if the start variable points
    only to terminals, simplify the grammar to include only
    that variable's rule.
    
    Args:
        cfl (json dictionary): dictionary of 4 tuple cfl
    """
    used_variables = set(cfl.start_var)

    # Iterate through the rules and add them to the unique_rules set
    # if they are not already present (considering LHS and RHS)
    new_rules = []
    for rule_dict in cfl.rules:
        # Convert RHS to a list to handle individual characters
        rhs_set = frozenset(rule_dict["RHS"])
        new_rules.append({"LHS": rule_dict["LHS"], "RHS": list(rhs_set)})

        # find all vars in RHS of rules
        symbol_list = product_to_list(rhs_set)
        var_list = [char for symbol in symbol_list for char in symbol]

        # Update used_variables set with non-terminal variables
        for symbol in var_list:
            if symbol not in cfl.terminals and symbol not in used_variables:
                used_variables.add(symbol)

    # Remove unused variables
    cfl.vars = [var for var in cfl.vars if var in used_variables]

    # Create a new list to store the rules to keep
    updated_rules = []

    # Filter rules based on the presence of LHS variable in cfl.vars
    for rule_dict in new_rules:
        if rule_dict["LHS"] in cfl.vars:
            updated_rules.append(rule_dict)

    # Update the CFL rules with the unique rules
    cfl.rules = updated_rules
    
    remove_unit_products(cfl)