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
    implementation: Louise Delpierre, Aline Boulanger (v.1 24/02/2022)
    Eline Mota (v.2, 03/03/2022)
    '''
    order = turn_list(orders)  

    print('order', order)
    for elements in order:
        
        if '*' in elements:
            coords = elements.split (":*")
            
            i = 0
            for coord in coords:
                i += 1

                coord = coord.split ("-")
                if i == 1:
                    x_A = int(coord[0])
                    y_A = int(coord[1])
                elif i == 2 :
                    x_B = int(coord[0])
                    y_B = int(coord[1])
                

            if check_life(player_A, (x_A, y_A)):
                print(term.move_xy(50, 100) + 'your wolf has zero life, you cannot attack')

            else :
                vie = player_A[(x_A,y_A)]["life"]
                vie = vie/10
                player_B [(x_B,y_B)]["life"] -= vie
                update_life(player_B, x_B, y_B)
         
    return player_A, player_B
