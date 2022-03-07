def color (player_A):
    """return the color of each team
    
    Parameters:
    -----------
    player_A: wolf of a player (dict)
    
    Return:
    -------
    term.stateblue1 : color of team 1
    term.purple4 : color of team 2
    
    Version:
    ---------
    specification: Eline Mota (v.1 03/03/2022)
    implementation: Eline Mota (v.1 03/03/2022)"""
    if player_A == player_1:
        return term.slateblue1
    elif player_A == player_2:
        return term.purple4
    else:
        raise ValueError('error')
