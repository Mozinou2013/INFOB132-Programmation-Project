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
            coords = elements.split (":<") #['2-2', '2-3']
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
                    coords_food = (x_food, y_food) #(2,3)
            for key in food :
                if coords_food == key :
                    while player_A[(x_A, y_A)]["life"] < 100 and food[x_food, y_food]["life"]  > 0 :
                        player_A[(x_A, y_A)]["life"] += 1
                        food[x_food, y_food]["life"] -= 1

    return food, player_A 

print(eat(food, player_1, orders))
