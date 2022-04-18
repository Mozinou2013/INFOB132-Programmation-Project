def move_food(pos, food):
    """Search the nearest source of food and make a wolf move toward it
    
    Parameters:
    -----------
    pos: position of the wolf (tuple)
    food: dictionary of food (dict)

    Return:
    -------
    order: the move the wolf is going to make (str)

    Versions:
    ----------
    specification: Louise Delpierre (v.1 31/03/2022)
    implementation: Louise Delpierre, Eline Mota (v.1 31/03/2022)

    """
    i = 0
    z = 0
    for foods in food:
        i += 1
        x, y = localisation(pos, foods)
        distance = x + y
        if i == 1:
            z = distance
        else:
            if distance <= z and food[foods]['life'] > 0:
                z = distance
                distance_x = x
                distance_y = y
                the_food = foods
            else:
                None
        
    order = str(pos[0]) + '-' + str(pos[1]) + ':@' + str(the_food[0]) + '-' + str(the_food[1])
    return order
