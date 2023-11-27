from helper import new_var

def add_new_start_rule(cfl):
    '''
    Create a new unique variable. Set it as the new start variable and create
    a rule product to the previous start variable
    '''
    # create a new unique variable
    new_start_var = new_var(cfl.vars)

    # create start variable rule to point to previous start variable
    cfl.rules.insert(0, dict(LHS = new_start_var, RHS = list(cfl.start_var)))

    # update the cfl's start variable
    cfl.start_var = new_start_var