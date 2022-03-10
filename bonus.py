player_1 = {(2,2): {'type': 'alpha', 'life': 100}, (1,1): {'type': 'normal', 'life': 100}}

def count_cases(e1, e2):
    """
    Count the cases that separes two elements
    
    Parameters:
    ------------
    e1: position of the first element (tuple)
    e2: position of the second element (tuple) 
    
    Returns:
    --------
    distance_x: the number of cases X that separes two things on the board (int)
    distance_y : the number of cases Y that separes two things on the board (int)
    
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
        print(distance)
        distance_x = distance[0]
        distance_y = distance[1]
        print(distance_x, distance_y)
        if distance_x + distance_y != 0:#Empêche le bonus de s'activer sur la case du loup même
            if player_A [key]['type'] == 'normal':         
                if distance_x <= 2 and distance_y <= 2: 
                    bonusL += 10 # ajoute 10 
            if player_A [key]['type'] == 'alpha': 
                if distance_x <= 4 and distance_y <= 4 :
                    bonusA +=  30 # il ajoute 30 
    bonusTotal = bonusL + bonusA   # il faut calculer aussi le nombre d'itération !!  Erreur ici 

    return bonusTotal

 
print(bonus(player_1,(2,2)))
    

# faire disparaitre le bonus  
