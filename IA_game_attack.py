orders = ''


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
        if player_B[key]['type'] == 'omega':
            life_omega = player_B[key]['life']
            pos_omega = key

        if player_B[key]['type']== 'alpha':
            life_alpha = player_B[key]['life']
            pos_alpha = key 

    for wolves in player_A: 
        distance_omega = count_cases(wolves, pos_omega)
        distance_o_x = distance_omega[0]
        distance_o_y = distance_omega[1]

        distance_alpha = count_cases (wolves, pos_alpha)
        distance_a_x = distance_alpha[0] 
        distance_a_y = distance_alpha[1]

        if distance_o_x <= 1 and distance_o_y <= 1 and life_omega > 30:
            # attaquer l'omega adverse si celui-ci a plus que 30 points de vie 
                attack_x = str(wolves[0])
                attack_y = str(wolves[1])
                action = '*'
  
                attacked_x = str(pos_omega[0])
                attacked_y = str(pos_omega[1])
            
                if can_use(orders, attack_x, attack_y) == True: 
                    orders += orders + attack_x + '-' + attack_y + action + attacked_x + '-' + attacked_y + ' ' 
        
        elif distance_a_x <=1 and distance_a_x <=1: 
            attack_x = str(wolves[0])
            attack_y = str(wolves[1])
            action = '*'
                    
            attacked_x = str(pos_alpha[0])
            attacked_y = str(pos_alpha[1])
            
            if can_use(orders, attack_x, attack_y) == True: 
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
