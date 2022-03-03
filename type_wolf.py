def type_wolf(player_A, x, y):
    """Return the type of a wolf
    
    Parameters:
    ------------
    player_A: wolves of a player
    x: coordonate x of a wolf
    y: coordonate y of a wolf
    
    Return:
    -------
    type: type of the wolf (A, O or L)"""
    type = player_A[(x,y)]['type']
    if type == 'alpha':
        return 'A'
    elif type == 'omega':
        return 'O'
    elif type == 'normal':
        return 'L'
    else:
        raise ValueError('your type does not exist')
