orders = ''


def IA_game_attack(player_A, life_ennemy, pos_ennemy, orders): 
    """
    To attack the wolf of the player_B
    
    Parameters
    ----------
    player_A : wolves of the IA (dict)
    pos_ennemy: position of the ennemy that we will attack (tuple)
    life_ennemy: life of the ennemy that we will attack (tuple)
    orders: orders of the IA (str)

    Returns
    -------
    orders: orders of the IA (str)

    Versions:
    ---------
    specification: Aurélie Genot et Aline Boulanger (v.1 31/03/2022)
    specification: Aurélie Genot et Aline Boulanger (v.2 21/04/2022)
    implementation : Aurélie Genot et Aline Boulanger (v.1 31/03/2022)
    implementation : Aurélie Genot (v.2 02/04/2022)
    implementation: Aurélie Genot et Aline Boulanger (v.3 21/04/2022)
    """

    for wolves in player_A: 
        distance_wolf = count_cases(wolves, pos_ennemy)
        distance_wolf_x = distance_wolf[0]
        distance_wolf_y = distance_wolf[1]



        if distance_wolf_x <= 1 and distance_wolf_y <= 1 and life_omega > 30:
            # attaquer l'omega adverse si celui-ci a plus que 30 points de vie 
      

def IA_game_attack(wolf, ennemy, orders): 
    """
    To give the order to attack the wolf of the player_B
    
    Parameters
    ----------
    wolf: the wolf which will attack (tuple)
    ennemy: the wolf which will be attacked (tuple)
    orders: orders of the IA (str)

    Returns
    -------
    orders: orders of the IA (str)

    Versions:
    ---------
    specification: Aurélie Genot et Aline Boulanger (v.1 31/03/2022)
    specification: Aurélie Genot et Aline Boulanger (v.2 21/04/2022)
    implementation : Aurélie Genot et Aline Boulanger (v.1 31/03/2022)
    implementation : Aurélie Genot (v.2 02/04/2022)
    implementation: Aurélie Genot et Aline Boulanger (v.3 21/04/2022)
    """

    attack_x = str(wolf[0])
    attack_y = str(wolf[1])
    action = '*'    
    attacked_x = str(ennemy[0])
    attacked_y = str(ennemy[1])
    
    if can_use(orders, int(attack_x), int(attack_y)) == True: 
        orders += orders + attack_x + '-' + attack_y + action + attacked_x + '-' + attacked_y + ' '     
        
    return orders

