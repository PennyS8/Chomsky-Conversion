def remove_duplicate_rules(cfl):
    """
    Remove duplicate rules (rules with the same LHS and RHS) from the CFL.
    """
    unique_rules = set()

    # Iterate through the rules and add them to the unique_rules set
    # if they are not already present (considering LHS and RHS)
    new_rules = []
    for rule_dict in cfl.rules:
        rhs_set = frozenset(rule_dict["RHS"])
        rule_key = (rule_dict["LHS"], rhs_set)
        if rule_key not in unique_rules:
            unique_rules.add(rule_key)
            new_rules.append(rule_dict)

    # Update the CFL rules with the unique rules
    cfl.rules = new_rules