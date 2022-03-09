def in_map(case, width, height): 
    """To check if the case where the wolf wants to go is well in the map

    Parameters:
    -----------
    case: the case who has to be checked (tuple)

    Return:
    -------
    Result: True if the case is in the map, False otherwise (bool)

    Versions:
    ----------
    specification: Aurélie Genot (v.1 19/02/2022)
    specification: Aurélie Genot (v.2 03/03/2022)
    implementation: Aurélie Genot (v.1 03/03/2022)
    """
    
    x = case[0]
    y = case[1]

    if x >= 1 and x<= width and y>=1 and y<= height: 
        return True
    else:
        return False 