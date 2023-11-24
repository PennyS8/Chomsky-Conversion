from helper import new_var

def add_new_start_rule(cfl):
    '''
    Create a new unique variable. Set it as the new start variable and create
    a rule product to the previous start variable
    '''
    new_start_var = new_var(cfl.vars)
    cfl.rules.insert(0, dict(LHS = new_start_var, RHS = list(cfl.start_var)))

    cfl.start_var = new_start_var

    return cfl