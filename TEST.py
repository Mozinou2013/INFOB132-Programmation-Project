orders = ''

def IA_game_eat(player_A, food, orders):
    """
    To make the wolves eat

    Parameters
    ----------
    player_A : wolves of the IA (dict)
    food: food of the game (dict)
    orders: orders of the IA (str)

    Returns
    -------
    orders: orders of the IA (str)

    Versions:
    ---------
    specification: Aurélie Genot et Aline Boulanger (v.1 31/03/2022)
    implementation : Aurélie Genot et Aline Boulanger (v.1 31/03/2022)
    """
    for wolves in player_A:
        for foods in food:
    
            distance = count_cases(wolves, foods)
            distance_x = distance[0]
            distance_y = distance[1]
            if distance_x <= 1 and distance_y <=1: 
                #vérifie une série de chose pour que l'action de se nourrir ait un minimum de sens
                if 100 > player_A[wolves]['life'] and food[foods]['life'] > 0 :  
                    eat_x = str(wolves[0])
                    eat_y = str(wolves[1])
                    eaten_x = str(foods[0])
                    eaten_y = str(foods[1])
                    action_2 = ':<'
                    if can_use(orders, eat_x, eat_y): 
                        orders += orders + eat_x + '-' + eat_y + action_2 + eaten_x + '-' + eaten_y + ' '
    return orders
                        

def IA_game_attack(player_A, player_B, orders): 
    """
    To attack the wolves of the player_B
    
    Parameters
    ----------
    player_A : wolves of the IA (dict)
    player_B : wolves of the player_B (dict)
    orders: orders of the IA (str)

    Returns
    -------
    orders: orders of the IA (str)

    Versions:
    ---------
    specification: Aurélie Genot et Aline Boulanger (v.1 31/03/2022)
    implementation : Aurélie Genot et Aline Boulanger (v.1 31/03/2022)
    implementation : Aurélie Genot (v.2 02/04/2022)
    """
    
     # Récupérer la position de l'omega adverse 
    for key in player_B : 
        if player_B[key]["type"] == 'omega':
            life_omega = player_B[key]["life"]
            pos_omega = key

        if player_B[key]["type"]= 'alpha':
            life_alpha = player_B[key]['life']
            pos_alpha = key 

    for wolves in player_A: 
        distance_omega = count_cases(wolves, pos_omega)
        distance_o_x = distance_omega[0]
        distance_o_y = distance_omega[1]

        distance_alpha = count_cases (wolves, pos_alpha)
        distance_a_x = distance_alpha[0] 
        distance_a_y = distance_alpha[1]

        if distance_o_x <= 1 and distance_o_y <= 1 or distance_a_x <=1 and distance_a_x <=1: 
            # attaquer l'omega adverse si celui-ci a plus que 30 points de vie 
                attack_x = str(wolves[0])
                attack_y = str(wolves[1])
                action = '*'

                if 30 < life_omega :  
                    attacked_x = str(pos_omega[0])
                    attacked_y = str(pos_omega[1])
                    
                if 30> life_omega and 0 < life_alpha: 
                    attacked_x = str(pos_alpha[0])
                    attacked_y = str(pos_alpha[1])
                    
                if can_use(orders, attack_x, attack_y): 
                orders += orders + attack_x + '-' + attack_y + action + attacked_x + '-' + attacked_y + ' '     
                    
    return orders


def IA_game_move(player_A, player_B, food, orders):
    """
    To make the wolves move

    Parameters
    ----------
    player_A : wolves of the IA (dict)
    player_B : wolves of the other player (dict)
    food: food of the game (dict)
    orders: orders of the IA (str)

    Returns
    -------
    orders: orders of the IA (str)

    Versions:
    ---------
    specification: Aurélie Genot et Aline Boulanger (v.1 31/03/2022)
    implementation : Aurélie Genot et Aline Boulanger (v.1 31/03/2022)
    """
    ##ATTENTION SI LOUP ADVERSAIRE PEUT PAS BOUGER 
    for wolves in player_A:
        for wolves in player_B: 

            #si vie omega >30: on move sinon on va attack mais faut être a cote sinon faut move 
            #Si omega dead -> move vers alpha pr attack alpha 