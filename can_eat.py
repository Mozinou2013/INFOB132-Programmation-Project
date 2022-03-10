from count_cases import count_cases
from turn_list import turn_list

orders = "2-2:<6-2 10-10:pacify"
player_1 = {(6,2): {'type': 'alpha', 'life': 90}, (1,1): {'type': 'omega', 'life': 100}}


def can_eat (player_A, orders) :
    """
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
print(can_eat(player_1, orders)) 
                