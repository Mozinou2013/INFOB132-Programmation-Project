orders = "2-2:<7-4 10-10:pacify"
food = {(4,4) : 10, (1, 1) : 50}
player_1 = {(2,2): {'type': 'alpha', 'life': 90}, (1,1): {'type': 'omega', 'life': 100}}

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
def eat(food, player_A, orders):
    """
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
                    if coords_food == key :
                        while player_A[(x_A, y_A)]["life"] < 100 and food[key] > 0 :
                            player_A[(x_A, y_A)]["life"] += 1
                            food[key] -= 1

    return food, player_A 

print(eat(food, player_1, orders))