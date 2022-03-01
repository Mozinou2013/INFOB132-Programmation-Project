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

    Versions
    --------
    specification : Aurélie Genot (v.1 17/02/2022)

    """

def create_map(width, height, player_1, player_2, food): 
    """ 
    Create the map of the board 
    Parameters
    ----------
    height: height of the map (int)
    width: lenght of the map (int)
    player_1: wolves of the player 1 (dict)
    player_2: wolves of the player 2 (dict)
    food : food on the map (dict)
    Versions
    --------
    specification : Louise Delpierre (v1 17/02/2022)
    implementation: Eline Mota (v.1 28/02/2022)
    """
    print(term.home + term.clear)
    for x in range(0, width * 3, 3):
        for y in range(0, height, 1):
            if (x+y)%2 ==0:
                print(term.move_xy(x, y) + term.on_lavenderblush3 + '   ')
            else:
                print(term.move_xy(x, y) + term.on_snow2 + '   ')
    for key in player_1:
        if player_1[key]['type'] =='alpha':
            x = key[0]
            y = key[1]
            x, y = trans_coord(x, y)
            print(term.move_xy(x, y) + term.red + term.on_limegreen + 'A')
        elif player_1[key]['type'] =='omega':
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x, y) + 'O')
        else:
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x, y) + 'L')
    for key in player_2:
        if player_2[key]['type'] =='alpha':
            x = key[0]
            y = key[1]
            x, y = trans_coord(x, y)
            print(term.move_xy(x, y) + term.black +'A')
        elif player_2[key]['type'] =='omega':
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x, y) + term.black + 'O')
        else:
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x, y) +'L')
    for key in food:
        if food[key] == 10:
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x,y) +'b')
        elif food[key] == 30:
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x,y) + 'a')
        elif food[key] == 50:
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x,y) + 'm')
        elif food[key] == 100:
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x,y) + 'r')
        else:
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x,y) + 'd')


def attack(player_A, player_B, orders): 
    """ 
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
    """

def pacification(player_A, player_B, orders):
     """ 
    Pacification of the wolves of the other player 

    Parameters
    ----------
    orders : orders of the player who attacks (str)

    Returns
    --------
    pacified: pacified wolves of player_B (list) 


    Versions
    --------
    specification : Aline Boulanger (v.1 17/02/2022) 
    """

def bonus(player_A):
     """ 
    Get a bonus to the wolves of the player who is playing 

    Parameters
    ----------
    player_A : wolves of the player who plays (dict) # peut-être juste utilisé player 

    Returns
    --------
    power_up_wolves: wolves with their bonus (dict)

    Versions
    --------
    specification : Aurélie Genot (v.1 17/02/2022) 
    """
def move(player_A, order):
    """
    Move a wolf on the board

    Parameters:
    -----------
    player_A: wolves of the player who is playing (dict)
    order : order of the player_A (str)

    Returns:
    ---------
    player_A: wolves of the player who is playing after moving (dict)

    Versions:
    --------
    specification: Eline Mota (v.1 19/02/2022)

    """
    
def count_cases(e1, e2):
    """
    Count the cases that separes two elements
    
    Parameters:
    ------------
    e1: position of the first element (tuple)
    e2: position of the second element (tuple) 
    
    Returns:
    --------
    case: the number of cases that separes two things on the board (int)
    
    Versions:
    ----------
    specification: Louise Delpierre (v.1 19/02/2022)"""
    
def eat(food, player_A, orders):
    """
    Add energy point to a wolf depending on what he eats
    
    Parameters:
    -----------
    food: food placed on the map (dict)
    player_A: wolves of the player eating (dict)
    orders: orders of player_A (str)

    Return:
    -------
    player_A: wolves of the player who has eaten (dict)

    Versions:
    ---------
    specifiaction: Aline Boulanger (v.1 19/02/2022)

    """
def in_map(case):
    """Check if the case is well in the map
    Parameters:
    -----------
    case: the case who has to be checked (tuple)

    Return:
    -------
    Result: True if the case is in the map, False otherwise (bool)

    Versions:
    ----------
    specification: Aurélie Genot (v.1 19/02/2022)
    """
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

    """
def can_pacify(player_A):
    """Check if a wolf has enough energy to pacify

    Parameters:
    -----------
    player_A: wolves of the player playing (dict)

    Return:
    -------
    Result: True if it can, False otherwise (bool)

    Versions:
    ---------
    specification: Aline Boulanger (v.1 19/02/2022)
    """

def check_case(case, player_A):
    """Check if there is a wolf on a case
    
    Parameters:
    -----------
    case: a case of the map (tuple)
    player_A: wolves of a player (dict)

    Return:
    -------
    Result: True if there is a wolf on the case, False otherwise (bool)

    Versions:
    ---------
    specification: Louise Delpierre (v.1 19/02/2022)
    """

def check_food(food, case):
    """Check if there is food on a case
    
    Parameters:
    -----------
    case: a case on the map
    food: food placed on the map
    
    Return:
    -------
    Result: True if there is food on a case, False otherwise
    
    Version:
    --------
    specification: Eline Mota (v.1 19/02/2022)"""


def turn_list(order):
    """Turn an order into a list

    Parameters:
    -----------
    order: the order that a player has given (list)

    Return:
    -------
    case: the order turned into a list (list)

    Version:
    --------
    specification: Aurélie Genot (v.1 19/02/2022)
    """
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
def clear_pos(x,y):
    """Clear a position after moving a wolf
    Parameters:
    -----------
    x: coordonate x of the position
    y: coordonate y of the position
    
    Versions:
    ---------
    specification: Eline Mota (v.1 01/03/2022)
    implementation: Eline Mota (v.1 01/03/2022)
    """
    if (x+y) % 2 ==0:
        print(term.move_xy(x, y) + term.on_snow2 + ' ')
    else:
        print(term.move_xy(x,y) + term.on_lavenderblush3 + ' ')
    
