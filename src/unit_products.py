def remove_unit_products(cfl):
    '''
    Removes all products that are a single variable and replaces them with
    the productions of the replaced variable
    '''
    # create two lists, rules of unit products and rules of unit-free products
    uf_rules = [] # uf_rules = unit-product free rules
    unit_rules = [] # unit_rules = unit-product rules

    # loop through each product and populate the two rule lists
    for rule in cfl.rules:
        uf_products = [] # list of unit-free-products
        unit_products = [] # list of unit-products

        for product in rule["RHS"]:
            if product in cfl.vars: # checks if it's a unit product
                unit_products.append(product)
            else:
                uf_products.append(product)

        # create lists of rules for uf_products and unit_products
        uf_rules.append({"LHS": rule["LHS"], "RHS": uf_products})
        unit_rules.append({"LHS": rule["LHS"], "RHS": unit_products})

    sub_rules = [] # substituted rules
    # loop through unit_rules' products & substitute vars from uf_rules list
    for unit_rule in unit_rules:
        uf_products = []
        for unit_product in unit_rule["RHS"]:
            # for each unit-product substitute from the uf_rules var's products
            for uf_rule in uf_rules:
                if unit_product == uf_rule["LHS"]:
                    uf_products.extend(uf_rule["RHS"])

        sub_rules.append({"LHS": unit_rule["LHS"], "RHS": uf_products})

    # merge ufs_rules and uf_rules to finalize this conversion step
    ufs_rules = []  # unit free rules appended with the substituted rules
    for uf_rule in uf_rules:
        for sub_rule in sub_rules:
            if sub_rule["LHS"] == uf_rule["LHS"]:
                # Merge the RHS of both rules without duplicates
                merged_rhs = list(set(uf_rule["RHS"] + sub_rule["RHS"]))
                ufs_rules.append({"LHS": uf_rule["LHS"], "RHS": merged_rhs})

    cfl.rules = ufs_rules