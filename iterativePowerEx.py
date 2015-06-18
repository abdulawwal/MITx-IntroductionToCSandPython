# Procedural approach to calculating power of a number using Iteration

def iterativeProcedure(x,po):
    result = 1
    for turn in range(po):
        result = result * x
        print('Iteration number : ' + str(turn+1) + ' Current result : ' + str(result))
    return result
    