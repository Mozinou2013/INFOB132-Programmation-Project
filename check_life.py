def check_food(food, case):
    """Check if there is food on a case
    
    Parameters:
    -----------
    case: a case on the map
    food: food placed on the map
    
    Return:
    -------
    Result: True if there is food on a case, False otherwise
    
    Version:
    --------
    specification: Eline Mota (v.1 19/02/2022)
    """

    coord = case.split("-")
    x_A = int(coord[0])
    y_A = int(coord[1])

    if player_A[(x_A, y_A)]["life"] == 0 :
       player_A[(x_A, y_A)] = "human" 
    else :
       player_A[(x_A, y_A)] = player_A[(x_A, y_A)]

    return player_A[(x_A, y_A)]

