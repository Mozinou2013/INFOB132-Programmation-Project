orders = "2-2:<2-3 10-10:pacify"
food = {(4,4) : 10, (1, 1) : 50}
player_1 = {(2,2): {'type': 'alpha', 'life': 90}, (1,1): {'type': 'omega', 'life': 100}}
player_2 = {(1,2): {'type': 'alpha', 'life': 30}, (2,1): {'type': 'omega', 'life': 100}}


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

def count_cases(e1, e2):
    """
    Count the cases that separes two elements
    
    Parameters:
    ------------
    e1: position of the first element (tuple)
    e2: position of the second element (tuple) 
    
    Returns:
    --------
    distance: the difference of the two positions (with the X and the Y) (tuple)
    
    Versions:
    ----------
    specification: Louise Delpierre (v.1 19/02/2022)
    specification: Aurélie Genot (v.2 07/03/2022)
    implementation : Aline Boulanger (v.1 3/03/2022)
    """
    x_1 = e1[0]
    y_1 = e1[1]
    x_2 = e2[0]
    y_2 = e2[1]

    x = x_2 - x_1
    distance_x = abs(x)
    y = y_2 - y_1
    distance_y = abs(y)
    distance = (distance_x, distance_y)
    return distance

def can_pacify(player_A, x_A, y_A):
    """Check if a wolf has enough energy to pacify.
    Parameters:
    -----------
    player_A: wolves of the player playing (dict)
    x_A : the absisse of the wolf's position (int)
    y_A : the ordonate of the wolf's position (int)
    Return:
    -------
    Result: True if it can, False otherwise (bool)
    Versions:
    ---------
    specification: Aline Boulanger (v.1 19/02/2022)
    specification : Aline Boulanger (v.2 03/03/2022)
    implementation : Aline Boulanger (v.1 03/03/2022)
    """

    if player_A[x_A, y_A]["type"] == "omega" :
        if player_A[x_A, y_A]["life"] >= 40 :
            return True
        else :
            return False
    else :
        return False 

def pacification(player_A, player_B, orders):
    """ 
    Pacification of the wolves of the other player 
    Parameters
    ----------
    player_A : the player who wants to pacify (dict)
    player_B : the player who is pacify (dict) 
    orders : orders of the player who attacks (str)
    Returns
    --------
    player_A : the player with the type modification (dict)
    player_B : the player with the type modification (dict) 

    Versions
    --------
    specification : Aline Boulanger (v.1 17/02/2022) 
    implementation : Louise Delpierre (v.1 5/03/2022)
    """
    order = turn_list(orders) 
    for elements in order :                 # recherche pacify dans order 
        if 'pacify' in elements:
            coords = elements.split (":pacify")
            i = 0
            for coord in coords:
                i += 1
                coord = coord.split ("-")
                if i == 1:
                    x_A = int(coord[0])
                    y_A = int(coord[1])
                    coords_omega = (x_A, y_A)

        for key in player_A :               # vérifie si player_A est un omega 
            if can_pacify(player_A[key], x_A, y_A)== True : 
                distance = count_cases (player_A[key],coords_omega)
                distance_x = distance[0]
                distance_y = distance[1]
                if distance_x <= 6 and distance_y <= 6 : # la distance pour pacifier 
                    player_A[key]['type']== 'dog'
                    player_A[key]['life'] -= 40 
                    player_B[key]['type']== 'dog'
                else :
                    None 
            else : 
                None 
        
    return player_A, player_B
