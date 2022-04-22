def AI_final(player_A, player_B, food, height, lenght):
    """Return an order to play the game

    Parameters:
    ------------
    player_1: wolves of the player_1 (dict)
    player_2: wolves of the player_2 (dict)
    food: food on the map (dict)
    height: height of the map (int)
    lenght: lenght of the map (int)

    Return:
    -------
    orders: order final to play the game (str)

    Versions:
    ---------
    specificaition: Eline Mota et Louise Delpierre (v.1 21/04/2022)
    implementation: Louise Delpierre et Eline Mota (v.1 21/04/2022)
    """
    orders = ''
    for key in player_A :
        if player_A[key]['type'] == 'omega':
            life_omega = player_A[key]['life']
            pos_omega_A = key

        if player_A[key]['type']== 'alpha':
            life_alpha = player_A[key]['life']
            pos_alpha_A = key 
    
    distance_A_O = count_cases(pos_alpha_A, pos_omega_A) #calcule la distance entre alpha et omega
    x_A_O = distance_A_O[0]
    y_A_O = distance_A_O[1]

    if x_A_O > 3 or y_A_O > 3:

        tuple0 =  move_wolf_to_wolf(pos_alpha_A, pos_omega_A, orders)
        orders += tuple0[0]
        pos_alpha_A  = tuple0[1]
        tuple1=  move_wolf_to_wolf(pos_omega_A, pos_alpha_A, orders)
        orders += tuple1[0]
        pos_omega_A  = tuple1[1]

    else:

        for wolves in player_B:

            distance_A_W = count_cases(pos_alpha_A, wolves) #calcule la distance entre alpha et les loups adverses (merci Louise)
            x_A_W = distance_A_W[0]
            y_A_W = distance_A_W[1]

            if x_A_W <= 2 and y_A_W <= 2:
                tuple0 = move_away_from_wolf(pos_alpha_A, pos_omega_A, orders) #alpha se casse loin des méchants
                orders += tuple0[0]
                pos_alpha_A = tuple0[1] 

                if player_A[pos_omega_A['life']] >= 40:
                    orders += str(pos_omega_A[0]) + '-' + str(pos_omega_A[1]) + ':pacify' #omega pacifie
                else:
                    for foods in food:
                        if foods == 'lol': #voir Aline et Aurélie
                            if pos_alpha_A == 'prout':
                                None
                                
                        else:
                            hungry0 = move_food(pos_omega_A, food, orders)
                            orders += hungry0[0]
                            pos_omega_A = hungry0[1]
                            depla = move_wolf_to_wolf(pos_alpha_A, pos_omega_A, orders)
