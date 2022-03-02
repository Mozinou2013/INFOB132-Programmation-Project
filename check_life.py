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
    implementation : Louise Delpierre (v.1 2/03/2022)

    """

    coord = case.split("-")
    x_A = int(coord[0])
    y_A = int(coord[1])

    if player_A[(x_A, y_A)]["life"] == 0 :
       player_A[(x_A, y_A)] = "human" 
    else :
       player_A[(x_A, y_A)] = player_A[(x_A, y_A)]

    return player_A[(x_A, y_A)]

