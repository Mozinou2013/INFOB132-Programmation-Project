player_1 = {(2,2): {'type': 'alpha', 'life': 100}, (1,1): {'type': 'omega', 'life': 100}}

def count_cases(e1, e2):
    """
    Count the cases that separes two elements
    
    Parameters:
    ------------
    e1: position of the first element (tuple)
    e2: position of the second element (tuple) 
    
    Returns:
    --------
    distance: the number of cases that separes two things on the board (int)
    
    Versions:
    ----------
    specification: Louise Delpierre (v.1 19/02/2022)
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

def bonus(player_A, case):
    '''
    Get a bonus to the wolves of the player who is playing 
    Parameters
    ----------
    player_A : wolves of the player who plays (dict) # peut-être juste utilisé player
    case : the case of the wolf (tuple)  
    Returns
    --------
    power_up_wolves: wolves with their bonus (dict)
    Versions
    --------
    specification : Aurélie Genot (v.1 17/02/2022) 
    '''
    
    
    if count_cases < 2 : #Erreur là aussi car < n'est pas supporté si on met un fct avant et un entier ap
        for key in player_A :
            if player_A [key]['type'] == 'loup': # si le type du loup = loup 
                case1 = 10 # ajoute 10 
    elif count_cases < 4 :
        for key in player_A :
            if player_A [key]['type'] == 'alpha': # si le type du loup = alpha 
                case2 =  30 # il ajoute 30 
    case = case1 + case2   # il faut calculer aussi le nombre d'itération !!  Erreur ici 

loup = bonus (player_1,(2,2))  
# faire disparaitre le bonus   
    
