def remove_duplicate_rules(cfl):
    """
    Remove duplicate rules with different LHS but identical RHS and substitute accordingly
    """
    rules_dict = {}  # Dictionary to store rules based on their RHS

    # Iterate through the rules in reverse order to prioritize keeping the first occurrence
    for i in range(len(cfl.rules) - 1, -1, -1):
        rule = cfl.rules[i]
        lhs = rule["LHS"]
        rhs = tuple(rule["RHS"])

        # Check if the RHS is already in the dictionary
        if rhs in rules_dict:
            # If the LHS is different, substitute the rule
            if lhs != rules_dict[rhs]["LHS"]:
                substitute_rule = rules_dict[rhs].copy()
                substitute_rule["LHS"] = lhs
                cfl.rules[i] = substitute_rule
        else:
            # If the RHS is not in the dictionary, add the rule to the dictionary
            rules_dict[rhs] = rule