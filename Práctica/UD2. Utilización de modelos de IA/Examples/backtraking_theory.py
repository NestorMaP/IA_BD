def pre_backtraking(elements:list[int],
partial_solution: list[bool],objective:int)->list[bool]:
    print (partial_solution)
    
    # base case
    if (len(partial_solution) == len(elements)):
        return None
    
    """
    Define the domain, all vars have the same so it can
    be defined in as global
    """
    domain=[True,False]

    # Arrived to the end, so this is not the solution
    for option in [0, 1]:
        next_state = next_solution(partial_solution, option)
        pre_backtraking(elements, next_state, objective)
    return None