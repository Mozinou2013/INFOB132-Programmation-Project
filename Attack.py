
def attack(player_A, player_B, orders): 
    '''
    Attacks the wolves of the other player 
    Parameters
    ----------
    player_A : wolves of the player who attacks (dict)
    player_B : wolves of the player who is attacked (dict)
    orders : orders of the player who attacks (str)
    Returns
    --------
    player_1: wolves of the player 1 (dict)
    player_2: wolves of the player 2 (dict)
    Versions
    --------
    specification : Eline Mota (v.1 17/02/2022) 
    '''
    # varible de test/ modifiable 
    order = turn_list(orders)  # prensdre la fonction donnant les ordres
    player_A [(x,y)["life"]] = (player_A [(x,y)["life"]] - #bonus ) - attack # énergie loup au debut du cours 
    if '*' in order: # lire l'ordre et voir si * si trouve 
        # voir ce qui se passe sur blessed 
        player_A[(x,y)] = int(player_B [(x,y)["life"]] / 0.1) # quand un loup attaque, perte 1/10 de son énergie 

    if player_A [(x,y)["life"]] == 0  or player_B [(x,y)["life"]] == 0
        player_A [(x,y)] == 'humain'
        player_B [(x,y)]== 'humain' # voir sur blessed 



    
