def trans_coord(x, y):
    """Adapt and return the coordonates of an element for the map
    Parameters:
    -----------
    x: coordonate x (int)
    y: coordonate y (int)
    
    Return:
    -------
    x: coordonate x (int)
    y: coordonate y (int)
    Version:
    --------
    specification: Eline Mota (v.1 1/03/2022)
    implementation: Eline Mota (v.1 1/03/2022) """

    x = (x-1)*3 + 1
    y = y-1
    return x, y
