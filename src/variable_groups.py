from helper import new_var
from helper import product_to_list

def remove_variable_groups(cfl):
    '''
    Find products that are length greater than 2 and cut then substitute each
    half for a new variable & production rule until they are length 2 or less.
    NOTE: that we are appending to the list we are iterating over, this is
        effectively recursively breaking down the size of each production by 2
        each time unntil the length of the production is too small (len() <= 2)
        and is caught by the edge case

        Args:
            cfl (json dictionary): dictionary of 4 tuple cfl
    '''
    # find each instance of variable groups in rule productions
    for rule in cfl.rules:
        for i, product in enumerate(rule["RHS"]):
            # splits up the product into a list by its variable/terminals
            product_list = product_to_list(product)

            if len(product_list) <= 2: # edge case checker
                continue # skip this product, no modifications needed

            # split product into chunks and subtitute a variable for each chunk
            chunk_one = "".join(product_list[:int(len(product_list)/2)])
            chunk_two = "".join(product_list[int(len(product_list)/2):])

            # create substitution variables for each chunk
            chunk_one_sub = new_var(cfl.vars)
            chunk_two_sub = new_var(cfl.vars)

            # create new production rules for each chunk
            cfl.rules.append({"LHS": chunk_one_sub, "RHS": [str(chunk_one)]})
            cfl.rules.append({"LHS": chunk_two_sub, "RHS": [chunk_two]})

            # finalize the substitutions made
            rule["RHS"][i] = chunk_one_sub + chunk_two_sub