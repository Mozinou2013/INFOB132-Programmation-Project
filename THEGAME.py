import blessed 
term = blessed.Terminal()

def read_file(file):
    """ 
    Read the file and turn it into a data structure 
    Parameters
    -----------
    file : file of the game (file)

    Returns
    -------
    food: food on the map (dict)
    player_1: wolves of the player 1 (dict)
    player_2: wolves of the player 2 (dict)
    width: width of the map (int)
    height: height of the map (int)

    Versions
    --------
    specification : Aurélie Genot (v.1 17/02/2022)
    specification: Eline Mota (v.2 24/02/2022)
    Implementation: Eline Mote (v.1 24/02/2022)
    """
    f = open(file, 'r')
    i = 0
    player_1 = {}
    player_2 = {}
    height = 0
    width = 0
    food = {}
    for lines in f.readlines():
        i+=1
        if i == 2:
            liste = lines.split(' ')
            height = int(liste[0])
            width = int(liste[1])

        elif i >= 4 and i <= 12:
            liste = lines.split(' ')
            coordonate = (int(liste[1]), int(liste[2]))
            y = liste[3] #enlève le retour à la ligne
            y = y[0:-1]
            player_1[coordonate] = {'type': y, 'life': 100, 'pacifie': 'non'}
            
        elif i > 12 and i <= 21:
            liste = lines.split(' ')
            coordonate = (int(liste[1]), int(liste[2]))
            y = liste[3]
            y = y[0:-1]
            player_2[coordonate] = {'type': y, 'life': 100, 'pacifie': 'non'}
            
        elif i > 22:
            liste = lines.split(' ')
            coordonate = (int(liste[0]), int(liste[1]))
            food[coordonate] = {'type': liste[2], 'life': int(liste[3])}

    return width, height, player_1, player_2, food 

def trans_coord(x, y):
    """Adapt and return the coordonates of an element for the map
    Parameters:
    -----------
    x: coordonate x (int)
    y: coordonate y (int)
    
    Return:
    -------
    x: coordonate x (int)
    y: coordonate y (int)
    Version:
    --------
    specification: Eline Mota (v.1 1/03/2022)
    implementation: Eline Mota (v.1 1/03/2022) """


    x = (x-1)*3 + 1
    y = y-1
    return x, y

def can_eat (player_A, orders) :
    """
    Check if a wolf can eat 
    Parametres :
    ------------
    player_A: wolves of the player eating (dict)
    orders: orders of player_A (str)
    Returns :
    ---------
    maybe : The fact that the wolf can eat or not (bool)
    Versions :
    ----------
    specification : Aline Boulanger (v.1 10/03/2022)
    implementation : Louise Delpierre (v.1 10/03/2022)
    
    """
    order = turn_list(orders)
    
    for elements in order :
        if "<" in elements :
            coords = elements.split (":<") 
            i = 0
            for coord in coords : 
                i += 1
                coord = coord.split ("-")
                if i == 1 :
                    x_A = int(coord[0])
                    y_A = int(coord[1])
                    coords_wolfs = (x_A, y_A)
                elif i == 2 : 
                    x_food = int(coord[0])
                    y_food = int(coord[1]) 
                    coords_food = (x_food, y_food) 

    distance = count_cases(coords_food, coords_wolfs)
    distance_x = distance[0]
    distance_y = distance[1]
    if distance_x <= 1 and distance_y <= 1 :
        return True
    else : 
        return False
def check_life(player_A, case):
    """Check if a wolf has zero life

    Parameters:
    ----------
    player_A: wolves of the player playing (dict)
    case: place of the wolf we want to check (tuple)

    Return:
    -------
    Result: True if the wolf has zero life, False otherwise (bool)

    Versions:
    ---------
    specification: Eline Mota (v.1 19/02/2022)
    implementation: Eline Mota (v.1 03/03/2022)

    """
    for wolves in player_A:
        if wolves == case:
            if player_A[wolves]['life'] == 0:
                return True
    return False
def can_pacify(player_A, x_A, y_A):
    """Check if a wolf has enough energy to pacify and if he is an omega.
    Parameters:
    -----------
    player_A: wolves of the player playing (dict)
    x_A : the absisse of the wolf's position (int)
    y_A : the ordonate of the wolf's position (int)
    Return:
    -------
    Result: True if it can, False otherwise (bool)
    Versions:
    ---------
    specification: Aline Boulanger (v.1 19/02/2022)
    specification : Aline Boulanger (v.2 03/03/2022)
    implementation : Aline Boulanger (v.1 03/03/2022)
    """
    #vérifie d'abord si le loup en x_A, y_A fait bien partie des loups du joueur_A
    for key in player_A:
        if key != (x_A, y_A):
            return False
    #Vérifie si le loup du joueur_A est bien un omega et si il a au moins 40 de vie
    if player_A[x_A, y_A]["type"] == "omega" :
        if player_A[x_A, y_A]["life"] >= 40 :
            return True
        else :
            return False
    else :
        return False
print(term.move_xy(20,20))

#utiliser cette fonction après avoir adapter les coordonnées.
def clear_pos(x,y):
    """Clear a position after moving a wolf
    Parameters:
    -----------
    x: coordonate x of the position (int)
    y: coordonate y of the position (int)
    
    Versions:
    ---------
    specification: Eline Mota (v.1 01/03/2022)
    implementation: Eline Mota (v.1 01/03/2022)
    """
    if (x+y) % 2 ==0:
        print(term.move_xy(x, y) + term.on_snow2 + ' ')
    else:
        print(term.move_xy(x,y) + term.on_lavenderblush3 + ' ')


print(term.move_xy(20,20))

def color (team):
    """
    Return the color of each team
    
    Parameters:
    -----------
    player_A: wolf of a player (dict)
    
    Return:
    -------
    term.stateblue1 : color of team 1 (var)
    term.purple4 : color of team 2 (var)
    
    Version:
    ---------
    specification: Eline Mota (v.1 03/03/2022)
    implementation: Eline Mota (v.1 03/03/2022)"""
    
    if team == 1:
        return term.slateblue1
    elif team == 2:
        return term.purple4
    else:
        return ''

def type_wolf(player_A, x, y):
    """Return the type of a wolf
    
    Parameters:
    ------------
    player_A: wolves of a player (dict)
    x: coordonate x of a wolf (int)
    y: coordonate y of a wolf (int)
    
    Return:
    -------
    type: type of the wolf (A, O or L)

    Versions:
    ---------
    specification: Eline Mota (03/03/2022)
    implementation: Eline Mota (03/03/2022)
    """
    type = player_A[(x,y)]['type']
    if type == 'alpha':
        return 'A'
    elif type == 'omega':
        return 'O'
    elif type == 'normal':
        return 'L'
    else:
        None


def update_life(player_A, number, x, y):
    """Print on the map the life of the wolf

    Parameters:
    ------------
    player_A: wolves of a player (dict)
    number: number of the team playing (int)
    x: coordonate x of a wolf (int)
    y: coordonate y of a wolf (int)

    Versions:
    ----------
    specificaion: Eline Mota (v.1 03/03/2022)
    Eline Mota (v.2 18/03/2022)
    implementation: Eline Mota (v.1 03/03/2022)
    """
    colore = color(number) #la couleur de la team
    type = type_wolf(player_A, x, y) #le type du loup
    life = player_A[(x,y)]['life']
    pacifie = player_A[(x,y)]['pacifie']
    x, y = trans_coord(x,y) #adapte les coordonnées avec le plateau
    if life > 60 and life <= 100:
        print(term.move_xy(x,y) + colore + term.on_darkolivegreen3 + type)
    elif life <= 60 and life > 30:
        print(term.move_xy(x,y) + colore + term.on_yellow + type)
    elif life <= 30 and life > 0:
        print(term.move_xy(x,y) + colore + term.on_orangered + type)
    elif life == 0:
        print(term.move_xy(x, y) + colore + term.on_orangered + 'H')
    else:
        None
    if pacifie == 'oui':
        print(term.move_xy(x, y) + colore + 'P')
    else:
        None
    print(term.move_xy(20,20))


def turn_list(order):
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
    order = order.split(" ")
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
    return False


def can_use(order, x, y):
    """Check if a wolf can play, check if it hasn't already been used

    Parameters:
    ------------
    order: order for the wolves (str)
    x: coordonate x of the wolf (str)
    y: coordonate y of the wolf (str)
    
    Return:
    -------
    result: True if he can play, False otherwise 

    Versions:
    ---------
    specification: Eline Mota (11/03/2022)
    implementation: Eline Mota (11/03/2022)
    """
    order = turn_list(order)
    i = 0
    for element in order:
        element = element.split(':')
        element = element[0]
        element = element.split('-')
        if int(element[0]) == x and int(element[1]) == y:
            i += 1
    if i >= 2:
        return False
    elif i <= 1:
        return True

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
    

def type_food(type):
    """Identify the type of the food

    Parameters:
    -----------
    type: type of the food (str)

    Return:
    -------
    types: type of the food (str)

    Version:
    --------
    specification: Louise Delpierre (v.1 03/03/2022)
    implementation: Eline Mota (v.1 03/03/2022)
    """


    if type == 'berries':
        types = 'b'
    elif type == 'apples':
        types = 'a'
    elif type == 'mice':
        types = 'm'
    elif type == 'rabbits':
        types = 'r'
    elif type == 'deers':
        types = 'd'
    return types


def update_food(food):
    """Print the food on the map

    Parameters:
    -----------
    food: food on the map (dict)

    Versions:
    ---------
    specification: Eline Mota (v.1 03/03/2022)
    implementation: Eline Mota (v.1 03/03/2022)
    """
    for coord in food:
        type = type_food(food[coord]['type'])
        x = coord[0]
        y = coord[1]
        x, y = trans_coord(x,y)
        life = food[coord]['life']
        if life > 60:
            print(term.move_xy(x, y) + term.black + term.on_darkolivegreen3 + type)
        elif life <= 60 and life > 30:
            print(term.move_xy(x, y) + term.black + term.on_yellow + type)
        elif life <= 30 and life > 0:
            print(term.move_xy(x, y) + term.black + term.on_orangered + type)
        elif life == 0:
            print(term.move_xy(x,y) + term.black + term.on_orangered + '0')
        else:
            raise ValueError('you cannot have a negative life')

def create_map(width, height, player_1, player_2, food): 
    """ 
    Create the map of the board 
    Parameters
    ----------
    width: width of the map (int)
    height: height of the map (int)
    player_1: wolves of the player 1 (dict)
    player_2: wolves of the player 2 (dict)
    food : food on the map (dict)
    Versions
    --------
    specification : Louise Delpierre (v1 17/02/2022)
    implementation: Eline Mota (v.1 28/02/2022)
    Eline Mota (v.2 10/03/2022)
    """
    print(term.home + term.clear)
    #crée le plateau
    for x in range(0, width * 3, 3):
        for y in range(0, height, 1):
            if (x+y)%2 ==0:
                print(term.move_xy(x, y) + term.on_lavenderblush3 + '   ')
            else:
                print(term.move_xy(x, y) + term.on_snow2 + '   ')
    #positionne les loups des deux joueurs et la nourriture
    for key in player_1:
        x = key[0]
        y = key[1]
        update_life(player_1, 1, x, y)
    for key in player_2:
        x = key[0]
        y = key[1]
        update_life(player_2, 2, x, y)

    for key in food:
        x = key[0]
        y = key[1]
        update_food(food)




def bonus(player_A, case):
    '''
    Get a bonus to the wolves of the player who is playing 
    Parameters
    ----------
    player_A : wolves of the player who plays (dict) # peut-être juste utilisé player
    case : the case of the wolf who wants to have a bonus (tuple)  
    Returns
    --------
    power_up_wolves: wolves with their bonus (dict)
    Versions
    --------
    specification : Aurélie Genot (v.1 17/02/2022) 
    implementation : Louise Delpierre (v.1 9/03/2022)
    '''
    bonusL = 0
    bonusA = 0

    for key in player_A :
        distance = count_cases (case, key)
        distance_x = distance[0]
        distance_y = distance[1]
        if distance_x + distance_y != 0 :#Empêche le bonus de s'activer sur la case du loup même
            if player_A [key]['type'] == 'normal':         
                if distance_x <= 2 and distance_y <= 2: 
                    bonusL += 10
            if player_A [key]['type'] == 'alpha': 
                if distance_x <= 4 and distance_y <= 4 :
                    bonusA +=  30
    bonusTotal = bonusL + bonusA  

    return bonusTotal

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
    implementation: Eline Mota (v.2, 03/03/2022)
    '''
    bonuss = 0
    order = turn_list(orders)  

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
            #vérifie une série de choses avant que le loup puisse attaquer afin d'éviter les erreurs  
            if check_case((x_B, y_B), player_B) == True and check_life(player_A, (x_A, y_A)) == False and player_A[(x_A, y_A)]['pacifie'] == 'non' and can_use(orders, x_A, y_A) == True:
                vie = player_A[(x_A,y_A)]["life"]
                bonuss = bonus(player_A, (x_A, y_A))
                vie += bonuss
                attaque = vie/10
                #boucle pour éviter de tomber dans les négatifs
                while player_B [(x_B,y_B)]["life"] >= 0 and attaque >= 0:
                    player_B [(x_B,y_B)]["life"] -= 1  
                    attaque -= 1   
            else:
                None

    return player_A, player_B


def eat(food, player_A, orders, team):
    """
    Add energy point to a wolf depending on what he eats
    
    Parameters:
    -----------
    food: food placed on the map (dict)
    player_A: wolves of the player eating (dict)
    orders: orders of player_A (str)
    team: team of the player eating (int)
    Return:
    -------
    player_A: wolves of the player who has eaten (dict)
    food : food placed on the map (dict)
    Versions:
    ---------
    specifiaction: Aline Boulanger (v.1 19/02/2022)
    Eline Mota (v.2 18/03/2022)
    implementation : Aline Boulanger (v.1 02/03/2022)
    """
    
    order = turn_list(orders)

    for elements in order :
        if "<" in elements :
            coords = elements.split (":<")
            i = 0
            for coord in coords : 
                i += 1
                coord = coord.split ("-")
                if i == 1 :
                    x_A = int(coord[0])
                    y_A = int(coord[1])
                elif i == 2 : 
                    x_food = int(coord[0])
                    y_food = int(coord[1]) 
                    coords_food = (x_food, y_food)
            for key in food :
                if coords_food == key and can_use(orders, x_A, y_A) and can_eat(player_A, orders):
                    #boucle pour éviter de dépasser 100 ou pour éviter que la vie de la nourriture soit négative
                    while player_A[(x_A, y_A)]["life"] < 100 and food[x_food, y_food]["life"]  > 0 :
                        player_A[(x_A, y_A)]["life"] += 1
                        food[x_food, y_food]["life"] -= 1
                    update_food(food)
                    update_life(player_A, team, x_A, y_A)
                else:
                    None

    return food, player_A 

    
def in_map(case, width, height): 
    """To check if the case where the wolf wants to go is well in the map
    Parameters:
    -----------
    case: the case who has to be checked (tuple)
    width: width of the map (int)
    height: height of the map (int)
    Return:
    -------
    Result: True if the case is in the map, False otherwise (bool)
    Versions:
    ----------
    specification: Aurélie Genot (v.1 19/02/2022)
    specification: Aurélie Genot (v.2 03/03/2022)
    specification: Eline Mota (v.3 18/03/2022)
    implementation: Aurélie Genot (v.1 03/03/2022)
    """
    
    x = case[0]
    y = case[1]

    if x >= 1 and x<= width and y>=1 and y<= height: 
        return True
    else:
        return False


def move(player_A, player_B, orders, width, height, team, food):
    """
    Move a wolf on the board
    Parameters:
    -----------
    player_A: wolves of the player who is playing (dict)
    player_B: wolves of the other player (dict)
    orders : order of the player_A (str)
    width: width of the map (int)
    height: height of the map (int)
    team: team of the player moving (int)
    food: food on the map (dict)
    Returns:
    ---------
    player_A: wolves of the player who is playing after moving (dict)
    Versions:
    --------
    specification: Eline Mota (v.1 19/02/2022)
    specification: Eline Mota (v.2 18/03/2022)
    implementation : Aurélie Genot (v.1 03/03/2022)
    implementation: Aurélie Genot (v.2 07/03/2022)
    implementation: Eline Mota (v.3 18/03/2022)
    """

    order = turn_list(orders) 
    for elements in order:
        

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

            # 1ère étape: Regarder si déplacement possible (ckeck_case, can_use et in_map) 

            if check_case(actual_pos, player_A) == True and check_case(future_pos, player_A) == False and check_case(future_pos, player_B) == False and in_map(future_pos, width, height) == True and can_use(orders, actual_x, actual_y) == True:
               

            # 2ème étape: vérifie que c'est un déplacement d'une case maximumum (avec count_case)
                distance = count_cases(actual_pos, future_pos) 
                distance_x = distance[0]
                distance_y = distance[1] 
                if distance_x <=1 and distance_y <=1: 
                    
                   #3ème étape: faire le déplacement 
                    case_deleted = player_A.pop(actual_pos) # Supprimer l'emplacement actuel
                    value_case_deleted = case_deleted
                    player_A[(future_pos)] = value_case_deleted # Créer le nouvel emplacement
                    #change sur le plateau
                    x, y = trans_coord(actual_x, actual_y)
                    clear_pos(x, y)
                    if team == 1:
                        update_food(food)
                        update_life(player_A, 1, future_x, future_y)
                    elif team == 2:
                        update_food(food)
                        update_life(player_A, 2, future_x, future_y)
            else:
                None




    return player_A


def pacification(player_A, player_B, orders):
    """ 
    Pacification of the wolves of the other player 
    Parameters
    ----------
    player_A : the player who wants to pacify (dict)
    player_B : the player who is pacify (dict) 
    orders : orders of the player who attacks (str)
    Returns
    --------
    player_A : the player with the type modification (dict)
    player_B : the player with the type modification (dict) 
    Versions
    --------
    specification : Aline Boulanger (v.1 17/02/2022) 
    implementation : Louise Delpierre (v.1 5/03/2022)
    """
    order = turn_list(orders) 
    for elements in order :                
        if 'pacify' in elements: # recherche pacify dans order 
            coords = elements.split (":pacify")
            i = 0
            for coord in coords:
                i += 1
                coord = coord.split ("-")
                if i == 1:
                    x_A = int(coord[0])
                    y_A = int(coord[1])
                    coords_omega = (x_A, y_A)
       
                if can_pacify(player_A, x_A, y_A) == True and can_use(orders, x_A, y_A):  # vérifie si player_A est un omega 
                    for key in player_A:
                        distance = count_cases (key,coords_omega)
                        distance_x = distance[0]
                        distance_y = distance[1]
                        if distance_x <= 6 and distance_y <= 6 and key != coords_omega: # la distance pour pacifier 
                            player_A[key]['pacifie'] = 'oui'
                        else:
                            None
                    for key in player_B:
                        distance = count_cases (key,coords_omega)
                        distance_x = distance[0]
                        distance_y = distance[1]
                        if distance_x <= 6 and distance_y <= 6 and key != coords_omega: # la distance pour pacifier 
                            player_B[key]['pacifie']= 'oui'

                        else :
                             None 
                    player_A[coords_omega]['life'] -= 40
                else : 
                    None 
    return player_A, player_B

def play_game(map_path, group_1, type_1, group_2, type_2):
    """Play a game.
    
    Parameters
    ----------
    map_path: path of map file (str)
    group_1: group of player 1 (int)
    type_1: type of player 1 (str)
    group_2: group of player 2 (int)
    type_2: type of player 2 (str)
    
    Notes
    -----
    Player type is either 'human', 'AI' or 'remote'.
    
    If there is an external referee, set group id to 0 for remote player.
    
    """

    width, height, player_1, player_2, food = read_file(map_path)

    for key in player_1:
        if player_1[key]['type'] == 'alpha':
            alpha1 = key
        else:
            None
    for key in player_2:
        if player_2[key]['type'] == 'alpha':
            alpha2 = key
        else:
            None
    
    create_map(width, height, player_1, player_2, food)

    i = 0
    while player_1[alpha1]['life'] > 0 and player_2[alpha2]['life'] > 0 and i <= 200:
        i += 1
        #évite d'avoir les ordres sur le plateau
        print(term.move_xy(25,25))

        #définit le type de "personne qui va jouer"

        if type_1 == 'human':
            orders1 = input('choose an order')
        elif type_2 == 'IA':
            None
        if type_2 == 'human':
            orders2 = input('choose an order')
        elif type_2 == 'IA': 
            None
        

        player_1, player_2 = pacification(player_1, player_2, orders1)
        player_2, player_1 = pacification(player_2, player_1, orders2)

        food, player_1 = eat(food, player_1, orders1, 1)
        food, player_2 = eat(food, player_2, orders2, 2)
        

        player_1 = move(player_1, player_2, orders1, width, height, 1, food)
        player_2 = move(player_2, player_1, orders2, width, height, 2, food)


        player_2b = player_2 #ne donne pas un désavantage pour attaquer à l'équipe deux 

        player_1, player_2b = attack(player_1, player_2b, orders1)
        player_2, player_1 = attack(player_2, player_1, orders2)

        player_2 = player_2b
        #rénitialise le pacifie et effectue les changements après l'attaque
        for wolves in player_1:
            x = wolves[0]
            y = wolves[1]
            player_1[wolves]['pacifie'] = 'non'
            update_life(player_1, 1, x, y )
        for wolves in player_2:
            x = wolves[0]
            y = wolves[1]
            player_2[wolves]['pacifie'] = 'non'
            update_life(player_2, 2, x, y )
        
        for wolves in player_1:
            if player_1[wolves]['type'] == 'alpha':
                alpha1 = wolves
        for wolves in player_2:
            if player_2[wolves]['type'] == 'alpha':
                alpha2 = wolves
    if player_1[alpha1]['life'] > 0:
        print('PLAYER 1 HAS WON')
    elif player_2[alpha2]['life'] > 0:
        print('PLAYER 2 HAS WON')
    else:
        print('EQULITY')


print(play_game('testfichier.txt', 1, 'human', 2, 'human'))


















