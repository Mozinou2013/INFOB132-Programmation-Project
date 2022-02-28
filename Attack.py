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
    '''

    
    #bonus = #fct bonus 
    # varible de test/ modifiable 
    order = turn_list(orders)  # prendre la fonction donnant les ordres

    print('order', order)
    for elements in order:
        
        if '*' in elements: # lire l'ordre et voir si * si trouve 
            # voir ce qui se passe sur blessed POUR LA VIE 
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
                

            if player_A [(x_A,y_A)]["life"] == 0 :
                player_A [(x_A,y_A)] == 'humain' # voir sur blessed

            else :
                vie = player_A[(x_A,y_A)]["life"] # quand un loup attaque, perte 1/10 de son énergie
                vie = vie/10
                print(vie)
                player_B [(x_B,y_B)]["life"] -= vie
                

            if player_B [(x_B,y_B)]["life"] == 0 :
                player_B [(x_B,y_B)] == 'humain' # voir sur blessed
        #player_A [(x_A, y_A)["life"]] = (player_A[(x_A,y_A)["life"]]) - attack # énergie loup au debut du cours ATTENTION - bonus
         
    return player_A, player_B

print(attack (player_1,player_2, "2-2:*7-4 10-10:pacify"))
