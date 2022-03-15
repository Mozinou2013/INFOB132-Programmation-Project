orders = "10-10:pacify 2-2:@2-1 3-3:@5-4 1-1:@1-2"
player_A = {(2,2): {'type': 'alpha', 'life': 90}, (1,1): {'type': 'omega', 'life': 100}}
width = 30
height = 30


def turn_list(orders):
    """Turn an order into a list
    Parameters:
    -----------
    order: the order that a player has given (list)
    Return:
    -------
    order: the order turned into a list (list)
    Version:
    --------
    specification: Aurélie Genot (v.1 19/02/2022)
    implementation: Aurélie Genot (v.1 24/02/2022) 
    """
    order = orders.split(" ")
    return order

def check_case(case, dictionnary_checked):
    """Check if there is an element of the dictionnary on a case 
    
    Parameters:
    -----------
    case: a case of the map (tuple)
    dictionnary_checked: dictionnary in which we check the information(dict)

    Return:
    -------
    Result: True if there is a item on the case, False otherwise (bool)

    Versions:
    ---------
    specification: Louise Delpierre (v.1 19/02/2022)
    specification: Aurélie Genot (v.2 03/03/2022)
    implementation: Aurélie Genot (v.1 03/03/2022)
    """
    for key in dictionnary_checked :
        if case == key :
            return True 
        else:
            return False
                   
def count_cases(e1, e2):

    """
    Count the cases that separes two elements
    
    Parameters:
    ------------
    e1: position of the first element (tuple)
    e2: position of the second element (tuple) 
    
    Returns:
    --------
    distance: the difference of the two positions (with the X and the Y) (tuple)
    
    Versions:
    ----------
    specification: Louise Delpierre (v.1 19/02/2022)
    specification: Aurélie Genot (v.2 07/03/2022)
    implementation : Aline Boulanger (v.1 3/03/2022)
    """
    x_1 = e1[0]
    y_1 = e1[1]
    x_2 = e2[0]
    y_2 = e2[1]

    x = x_2 - x_1
    distance_x = abs(x)
    y = y_2 - y_1
    distance_y = abs(y)
    distance = (distance_x, distance_y)
    return distance

def in_map(case, width, height): 
    """To check if the case where the wolf wants to go is well in the map

    Parameters:
    -----------
    case: the case who has to be checked (tuple)

    Return:
    -------
    Result: True if the case is in the map, False otherwise (bool)

    Versions:
    ----------
    specification: Aurélie Genot (v.1 19/02/2022)
    specification: Aurélie Genot (v.2 03/03/2022)
    implementation: Aurélie Genot (v.1 03/03/2022)
    """
    
    x = case[0]
    y = case[1]

    if x >= 1 and x<= width and y>=1 and y<= height: 
        return True
    else:
        return False 

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
                   
print (move(player_A, orders))



def check_if_good(player_A, dic_B, option): 
    """ 
    To check if the wolf will can eat or attack 

    Parameters:
    ----------
    player_A: the wolves of the player_A (dic) 
    dic_B: the dictionnary that you want to check (dic) 
    option: if the wolf will can eat (1) or attack (2) (int)
    


    Versions:
    ---------
    Specification: Aurélie Genot (v.1 15/03/2022)
    Implementation: Aurélie Genot (v.1 15/03/2022)
    """
    pos_player_A = player_A.keys() # Récupère toutes les clés du dictionnaire 
    pos_dic_B = dic_B.keys()
    
    for pos_A in pos_player_A:  #Pour chaque position des loups de player_A, regarde les positions du dictionnaire 2 
        for pos_B in pos_dic_B:
        
            distance = count_cases(pos_A,pos_B)
            distance_x = distance[0]
            distance_y = distance[1]
            if distance_x <= 1 and distance_y <= 1 : #Si jamais l'attaque ou le repas est possible 
                if option == 1: 
                attacking = pos_A
                attacked = pos_B
                choose = 0 
                if option == 2:
                moving = pos_A
                eating = pos_B
                choose = 1 
    