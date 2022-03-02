def check_life(player_A, case):
    """Check if a wolf has zero life
    Parameters:
    ----------
    player_A: wolves of the player playing (dict)
    case: place of the wolf we want to check (tuple)
    Return:
    -------
    player_A : wolves of the player playing (dict)
    Versions:
    ---------
    specification: Eline Mota (v.1 19/02/2022)
    implementation : Aline Boulanger (v.1 2/03/2022)

    """
    x_A = int(case[0])
    y_A = int(case[1])

    if player_A[(x_A, y_A)]["life"] == 0 :
       player_A[(x_A, y_A)]["type"] = "human" 
    else :
       player_A[(x_A, y_A)]["type"] = player_A[(x_A, y_A)]["type"] 
       
    return player_A

#check_life (player_1, (2,2))
