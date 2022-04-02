
def IA_game_eat(player_A, food, orders):
    """
    To make the wolves eat

    Parameters
    ----------
    player_A : wolves of the IA (dict)
    food: food of the game (dict)
    orders: orders of the IA (str)

    Returns
    -------
    orders: orders of the IA (str)

    Versions:
    ---------
    specification: Aurélie Genot et Aline Boulanger (v.1 31/03/2022)
    implementation : Aurélie Genot et Aline Boulanger (v.1 31/03/2022)
    """
    for wolves in player_A:
        for foods in food:
    
            distance = count_cases(wolves, foods)
            distance_x = distance[0]
            distance_y = distance[1]
            if distance_x <= 1 and distance_y <=1: 
                #vérifie une série de chose pour que l'action de se nourrir ait un minimum de sens
                if 100 > player_A[wolves]['life'] and food[foods]['life'] > 0 :  
                    eat_x = str(wolves[0])
                    eat_y = str(wolves[1])
                    eaten_x = str(foods[0])
                    eaten_y = str(foods[1])
                    action_2 = ':<'
                    if can_use(orders, eat_x, eat_y): 
                        orders += orders + eat_x + '-' + eat_y + action_2 + eaten_x + '-' + eaten_y + ' '
    return orders
                        