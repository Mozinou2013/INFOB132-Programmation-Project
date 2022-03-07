def update_life(player_A, x, y):
    """Print on the map the life of the wolf

    Parameters:
    ------------
    player_A: wolves of a player
    x: coordonate x of a wolf
    y: coordonate y of a wolf

    Versions:
    ----------
    specificaion: Eline Mota (v.1 03/03/2022)
    implementation: Eline Mota (v.1 03/03/2022)
    """
    colore = color(player_A)
    type = type_wolf(player_A, x, y)
    life = player_A[(x,y)]['life']
    x, y = trans_coord(x,y)
    if life > 60 and life < 100:
        print(term.move_xy(x,y) + colore + term.on_darkolivegreen3 + type)
    elif life <= 60 and life > 30:
        print(term.move_xy(x,y) + colore + term.on_yellow + type)
    elif life <= 30 and life > 0:
        print(term.move_xy(x,y) + colore + term.on_orangered + type)
    elif life == 0:
        print(term.move_xy(x, y) + colore + term.on_orangered + 'H')
    else:
        raise ValueError('error')
    print(term.move_xy(20,20))
