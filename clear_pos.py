def clear_pos(x,y):
    """Clear a position after moving a wolf
    Parameters:
    -----------
    x: coordonate x of the position
    y: coordonate y of the position
    
    Versions:
    ---------
    specification: Eline Mota (v.1 01/03/2022)
    implementation: Eline Mota (v.1 01/03/2022)
    """
    if (x+y) % 2 ==0:
        print(term.move_xy(x, y) + term.on_snow2 + ' ')
    else:
        print(term.move_xy(x,y) + term.on_lavenderblush3 + ' ')
