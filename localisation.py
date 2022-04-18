def localisation(elem1, elem2):
    """Caclculate the distance (without abs) between two elements
    
    Parameters:
    -----------
    elem1: position of the first element (tuple)
    elem2: position of the second element (tuple)
    
    Return
    -------
    distance_x: distance x between two elements (int)
    distance_y: distance y between two elements (int)
    
    Versions:
    ----------
    specification: Eline Mota (v.1 31/03/2022)
    implementation: Eline Mota, Louise Delapierre (v.1 31/03/2022)"""
    pos_ix = elem1[0]
    pos_iy = elem1[1]
    pos_fx = elem2[0]
    pos_fy = elem2[1]

    distance_x = pos_fx - pos_ix
    distance_y = pos_fy - pos_iy

    return distance_x, distance_y
