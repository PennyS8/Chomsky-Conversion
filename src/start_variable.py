from helper import new_var

def add_new_start_rule(cfl):
    counter = 0
    if (cfl.start_var[0] + "_" + str(counter)) == cfl.start_var:
        counter += 1

    new_start_var = new_var(cfl.vars)
    cfl.rules.insert(0, dict(LHS = new_start_var, RHS = list(cfl.start_var)))

    cfl.start_var = new_start_var

    return cfl