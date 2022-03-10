def move(player_A, orders):
    """
    Move a wolf on the board

    Parameters:
    -----------
    player_A: wolves of the player who is playing (dict)
    orders : order of the player_A (str)

    Returns:
    ---------
    player_A: wolves of the player who is playing after moving (dict)

    Versions:
    --------
    specification: Eline Mota (v.1 19/02/2022)
    implementation : Aurélie Genot (v.1 03/03/2022)
    implementation: Aurélie Genot (v.2 07/03/2022)

    """

    order = turn_list(orders)
    for elements in order:

        # PB FONCTIONNE SI 1 DEPLACEMENT (parce que coords ne retourne pas plusieurs pos) 
        if '@' in elements: # Pour chaque @ dans l'ordre
            coords = elements.split (":@") #Met en liste les éléments entourant @ 

            i = 0
            for coord in coords:
                i += 1

                coord = coord.split ("-") # Pour récupérer les coordonnées X et Y 
                if i == 1:
                    actual_x = int(coord[0])
                    actual_y = int(coord[1])
                elif i == 2 :
                    future_x = int(coord[0])
                    future_y = int(coord[1])
        
            actual_pos = (actual_x, actual_y)
            future_pos = (future_x, future_y)

            # 1ère étape: Regarder si déplacement possible (ckeck_case et in_map) 

            if check_case(future_pos, player_A) == False and in_map(future_pos, width, height) == True:
               

            # 2ème étape: vérifie que c'est un déplacement d'une case maximumu (avec count_case)
                distance = count_cases(actual_pos, future_pos) 
                distance_x = distance[0]
                distance_y = distance[1] 
                if distance_x <=1 and distance_y <=1: 
                    
                   #3ème étape: faire le déplacement 
                    case_deleted = player_A.pop(actual_pos) # Supprimer l'emplacement actuel
                    value_case_deleted = case_deleted
                    player_A[(future_pos)] = value_case_deleted # Créer le nouvel emplacement

    return player_A
                    


move(player_A, orders)
            
