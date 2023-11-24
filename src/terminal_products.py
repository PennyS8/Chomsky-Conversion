from helper import new_var

def isolate_terminals(cfl):
    '''
    
    '''
    for rule in cfl.rules:
        for product in rule["RHS"]:
            if product :
                new_var(cfl.vars)