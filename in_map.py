def in_map(case, width, height): 
    """To check if the case is well in the map

    Parameters:
    -----------
    case: the case who has to be checked (tuple)

    Return:
    -------
    Result: True if the case is in the map, False otherwise (bool)

    Versions:
    ----------
    specification: Aurélie Genot (v.1 19/02/2022)
    implementation : Aurélie Genot (v.1 03/02/2022)
    """
    ## Regarder si la case sur laquelle veut aller le loup est sur la map 
    ## Booléen, retourner true si la case est sur le plateau 
    
    x = case[0]
    y = case[1]

    if x >= 1 and x<= width and y>=1 and y<= height: 
        return True