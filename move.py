player_1 = {(2,2): {'type': 'alpha', 'life': 100}, (1,1): {'type': 'omega', 'life': 100}}
orders = "10-10:@10-11 12-12:*12-11 9-8:@9-9"

def turn_list(orders):
    """Turn an order into a list
    Parameters:
    -----------
    order: the order that a player has given (list)
    Return:
    -------
    order: the order turned into a list (list)
    Version:
    --------
    specification: Aurélie Genot (v.1 19/02/2022)
    implementation: Aurélie Genot (v.1 24/02/2022) 
    """
    order = orders.split(" ")
    return order


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
            i = 0
            for coord in coords:
                i += 1

                coord = coord.split ("-")
                if i == 1:
                    x_A = int(coord[0])
                    y_A = int(coord[1])
                    coords_wolf = (x_A, y_A)
                elif i == 2 :
                    x_B = int(coord[0])
                    y_B = int(coord[1])
                    coords_deplacement = (x_B, y_B)
        
        return coords_wolf, coords_deplacement
            
print(move(player_1, orders))
            
## 1) Vérifier que le déplacement est possible (in_map)
## utiliser count_case
