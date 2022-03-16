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



def IA_game(player_A, player_B, food):
    """
    To give a random order of a IA

    Parameters
    ----------
    player_A : wolves of the IA (dict)
    player_B : wolves of the other player (dict)
    food: food of the game (dict)

    Returns
    -------
    orders: orders of the IA (str)

    Versions:
    ---------
    specification: Aurélie Genot (v.1 10/03/2022)
    implementation: Aurélie Genot (v.1 10/03/2022)
    implementation : Aurélie Genot (v.2 15/03/2022)
    """
    orders = ""

    #Si un loup est à côté, il va l'attaquer 
    
    pos_player_A = player_A.keys() # Récupère toutes les clés du dictionnaire 
    pos_player_B = player_B.keys()
    
    for pos_A in pos_player_A:  #Pour chaque position des loups de player_A, regarde les positions des loups de player_B
        for pos_B in pos_player_B:
        
            distance = count_cases(pos_A,pos_B)
            distance_x = distance[0]
            distance_y = distance[1]
            if distance_x <= 1 and distance_y <= 1 : #Si jamais l'attaque est possible 
                attacking_x = pos_A[0]
                attacking_y = pos_A[1]
                attacked_x = pos_B[0]
                attacked_y = pos_B[1]
                action = ":*"

                if action == ":*"
                    orders += attacking_x + "-" + attacking_y + ":*" + attacked_x + "-" + attacked_y



    # Si une nourriture est à côté, va la manger 

    pos_food = food.keys() 

    for pos_A in pos_player_A:  #Pour chaque position des loups de player_A, regarde les positions des nourritures 
        for pos_food in pos_food:
        
            distance = count_cases(pos_A,pos_food)
            distance_x = distance[0]
            distance_y = distance[1]
            if distance_x <= 1 and distance_y <= 1 : #Si jamais le repas est possible 
                eating = pos_A
                eaten = pos_B
                action_2 = 'eating'
                
            # Dit les ordres 
            if action == 'attack'
                order += 

    coords_chosen = x_chosen + "-" + y_chosen

    return coords_chosen 

## Pr l'instant un loup ne pacifie jamais et ne prend pas compte ni des loups à 0 d'énergie, ni des loups pacifiés