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
        
        # ne fonctionne que si un déplacement (parce que coords ne retourne pas plusieurs pos) 
        if '@' in elements: # Pour chaque @ dans l'ordre
            coords = elements.split (":@") #Met en liste les éléments entourant @ 
            actual_pos = coords[0]
            future_pos = coords[1]
        
        return coords
            
move(player_A, orders)
            
## 1) Vérifier que le déplacement est possible (in_map)
## utiliser count_case
