def move(player_A, orders):
    """
    Move a wolf on the board

    Parameters:
    -----------
    player_A: wolves of the player who is playing (dict)
    orders : order of the player_A (str)

    Returns:
    ---------
    player_A: wolves of the player who is playing after moving (dict)

    Versions:
    --------
    specification: Eline Mota (v.1 19/02/2022)
    implementation : Aurélie Genot (v.1 03/03/2022)

    """
    order = turn_list(orders)

    for elements in order:
        
        if '@' in elements: # Pour chaque @ dans l'ordre  
            coords = elements.split (":*")
            
            
            i = 0
            for coord in coords:
                i += 1

                coord = coord.split ("-")
                if i == 1:
                    x_A = int(coord[0])
                    y_A = int(coord[1])
                elif i == 2 :
                    x_B = int(coord[0])
                    y_B = int(coord[1])

## 1) Vérifier que le déplacement est possible (sur le plateau + )