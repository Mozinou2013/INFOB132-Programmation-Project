from random import randint 


def choose_random_move(wolf): 
    """ 
    To give a ramdom position for a move possible on the map
    
    Parameters
    -----------
    wolf : the wolf who will move (tuple)

    Returns 
    --------
    coords_chosen: the coords chosen randomly (str)
    
    Versions
    ---------
    specification: Aurélie Genot (v.1 10/03/2022)
    implementation: Auréie Genot (v.1 10/03/2022)
    """
    actual_x = wolf[0]
    actual_y = wolf[1]

    #Choisit un déplacement possible
    x_chosen= str(randint(actual_x-1,actual_x+1)) 
    y_chosen= str(randint(actual_y-1,actual_y+1))

    coords_chosen = x_chosen + "-" + y_chosen

    return coords_chosen 


def IA_game(player_A, player_B):
    """
    To give a random order of a IA

    Parameters
    ----------
    player_A : wolves of the IA (dict)
    player_B : wolves of the other player (dict)

    Returns
    -------
    orders: orders of the IA (str)

    Versions:
    ---------
    specification: Aurélie Genot (v.1 10/03/2022)
    implementation: Aurélie Genot (v.1 10/03/2022)
    """
    orders = ""

    for 

    # Regarder pr taper tt ce qui bouge 

    number_orders = randint (0,3) # Nbre d'ordres donnés par l'IA
    for number in numbers_orders: 
        choose = randint(0,4)

    
## Si un loup est tout près, il tape, si il a 0 d'énergie il mange et sinon il move