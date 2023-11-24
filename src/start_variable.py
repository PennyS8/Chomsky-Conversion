def add_new_start_rule(cfl):
    counter = 0
    if (cfl.start_state[0] + "_" + str(counter)) == cfl.start_state:
        counter += 1

    new_start_string = cfl.start_state[0] + "_" + str(counter)
    cfl.production_rules.insert(0, dict(LHS = new_start_string,
                                        RHS = list(cfl.start_state)))

    cfl.start_state = new_start_string
    cfl.variables.append(new_start_string)

    return cfl