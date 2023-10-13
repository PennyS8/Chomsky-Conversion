variables = [];

def newVariable(variables):
    var = "X"
    i = 0
    while (var + i) in variables:
        i+=1
    variables.append(var + i)




