def pacification(player_A, player_B, orders):
     """ 
    Pacification of the wolves of the other player 
    Parameters
    ----------
    player_A : the player who wants to pacify (dict)
    player_B : the player who is pacify (dict) 
    orders : orders of the player who attacks (str)
    Returns
    --------
    pacified: pacified wolves of player_B (list) 
    Versions
    --------
    specification : Aline Boulanger (v.1 17/02/2022) 
    implementation : Aline Boulanger (v.1 2/03/2022) 
    """

    coord = case.split("-")
    x_A = int(coord[0])
    y_A = int(coord[1])

    if player_A[(x_A, y_A)]["life"] == 0 :
       player_A[(x_A, y_A)] = "human" 
    else :
       player_A[(x_A, y_A)] = player_A[(x_A, y_A)]

    return player_A[(x_A, y_A)]

