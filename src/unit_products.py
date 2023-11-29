def remove_unit_products(cfl):
    """
    Removes all products that are a single variable and replaces them with
    the productions of the replaced variable
    
    Args:
        cfl (json dictionary): dictionary of 4 tuple cfl
    """

    # create two lists, rules of unit products and rules of unit-free products
    uf_rules = [] # uf_rules = unit-product free rules
    unit_rules = [] # unit_rules = unit-product rules

    # unit product conuter to calculate maximum unit product chain possible
    num_unit_products = 0

    # loop through each product and populate the two rule lists
    for rule in cfl.rules:
        uf_products = [] # list of unit-free-products
        unit_products = [] # list of unit-products

        for product in rule["RHS"]:
            if product in cfl.vars: # checks if it's a unit product
                unit_products.append(product)
                num_unit_products += 1
            else:
                uf_products.append(product)

        # create lists of rules for uf_products and unit_products
        uf_rules.append({"LHS": rule["LHS"], "RHS": uf_products})
        unit_rules.append({"LHS": rule["LHS"], "RHS": unit_products})

    # Perform iterations up to max_unit_chain
    for _ in range(num_unit_products):

        # loop through unit_rules' products & substitute vars from uf_rules list
        new_sub_rules = []
        for unit_rule in unit_rules:
            uf_products = []
            for unit_product in unit_rule["RHS"]:

                # for each unit-product substitute from the uf_rules var's products
                for uf_rule in uf_rules:
                    if unit_product == uf_rule["LHS"]:
                        uf_products.extend(uf_rule["RHS"])

            new_sub_rules.append({"LHS": unit_rule["LHS"], "RHS": uf_products})

        # Merge ufs_rules and new_sub_rules to update unit-free rules
        updated_ufs_rules = []
        for uf_rule in uf_rules:
            matching_sub_rule = next((sub_rule for sub_rule in new_sub_rules if sub_rule["LHS"] == uf_rule["LHS"]), None)
            if matching_sub_rule:
                merged_rhs = list(set(uf_rule["RHS"] + matching_sub_rule["RHS"]))
                updated_ufs_rules.append({"LHS": uf_rule["LHS"], "RHS": merged_rhs})
            else:
                updated_ufs_rules.append({"LHS": uf_rule["LHS"], "RHS": uf_rule["RHS"]})

        uf_rules = updated_ufs_rules

    cfl.rules = uf_rules