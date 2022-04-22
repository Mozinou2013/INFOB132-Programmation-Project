def move_wolf_to_wolf(wolf1, wolf2, order):
    """Make a wolf move toward another wolf

    Parameters:
    -----------
    wolf1: coordonates of the first wolf who is going to move (tuple)
    wolf2: coordonate of the second wolf where the first wolf is going to go (tuple)
    order: orders (str)

    Return:
    -------
    order: orders (str)
    pos_wolf1: update of the position of the wolf 1
    
    Versions:
    ----------
    implementation: Eline Mota et Louise Delpierre (v.1 21/04/2022)
    specification: Eline Mota et Louise Delpierre (v.1 21/04/2022)
    """
    distance_x, distance_y = localisation(wolf1, wolf2) #calcule la distance (sans abs) entre les deux loups

    #en fonction de la distance, bouge le loup un (recule ou avance pour chaque x et y)

    if distance_x > 1:
        move_x = wolf1[0] + 1
    elif distance_x < 1:
        move_x = wolf1[0] - 1
    else:
        move_x = wolf1[0]

    if distance_y > 1:
        move_y = wolf1[1] + 1
    elif distance_y < 1:
        move_y = wolf1[1] - 1
    else:
        move_y = wolf1[1]
    
    if can_use(order, wolf1[0], wolf1[1]): #regarde si loup a déjà une action avant

        order += str(wolf1[0]) + '-' + str(wolf1[1]) + ':@' + str(move_x) + '-' + str(move_y) #move_x et move_y: position vers laquelle le loup va
   
    pos_wolf1 = (move_x, move_y)
    tuple = (order, pos_wolf1)

    return tuple
