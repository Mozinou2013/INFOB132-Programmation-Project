

food = {(2,3) : {"type" : "berries", "life" : 10}, (1, 1) : {"type" : "mice", "life" : 50}}
player_1 = {(2,2): {'type': 'alpha', 'life': 90}, (1,1): {'type': 'omega', 'life': 100}}
orders = "2-2:<2-3 10-10:pacify"

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
    food : food placed on the map (dict)
    Versions:
    ---------
    specifiaction: Aline Boulanger (v.1 19/02/2022)
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
                    coords_wolfs = (x_A, y_A)
                elif i == 2 : 
                    x_food = int(coord[0])
                    y_food = int(coord[1]) 
                    coords_food = (x_food, y_food) 

            if can_eat(player_A, orders) == True :
                for key in food :
                    if coords_food == key :
                        while player_A[(coords_wolfs)]["life"] < 100 and food[coords_food]["life"]  > 0 :
                            player_A[(coords_wolfs)]["life"] += 1
                            food[coords_food]["life"] -= 1
            else :
                None

    return food, player_A 

print(eat(food, player_1, orders))
