
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

def update_life(player_A, x, y):
    """Print on the map the life of the wolf

    Parameters:
    ------------
    player_A: wolves of a player
    x: coordonate x of a wolf
    y: coordonate y of a wolf

    Versions:
    ----------
    specificaion: Eline Mota (v.1 03/03/2022)
    implementation: Eline Mota (v.1 03/03/2022)
    """
    colore = color(player_A)
    type = type_wolf(player_A, x, y)
    life = player_A[(x,y)]['life']
    x, y = trans_coord(x,y)
    if life > 60 and life < 100:
        print(term.move_xy(x,y) + colore + term.on_darkolivegreen3 + type)
    elif life <= 60 and life > 30:
        print(term.move_xy(x,y) + colore + term.on_yellow + type)
    elif life <= 30 and life > 0:
        print(term.move_xy(x,y) + colore + term.on_orangered + type)
    elif life == 0:
        print(term.move_xy(x, y) + colore + term.on_orangered + 'H')
    else:
        raise ValueError('error')
    print(term.move_xy(20,20))

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
    implementation: Aline Boulanger, Louise Delpierre (v.1 02/03/2022)
    
    """
    if player_A[case]['life'] == 0:
        return True
    else:
        return False


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
    implementation : Eline Mota (v.2, 03/03/2022)
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
                lifew = player_A[(x_A,y_A)]["life"]
                lifew = lifew/10
                player_B [(x_B,y_B)]["life"] -= lifew
                update_life(player_B, x_B, y_B)
         
    return player_A, player_B
