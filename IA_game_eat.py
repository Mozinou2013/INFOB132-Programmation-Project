pos_alpha_omega = {pos_alpha : 'alpha', pos_omega : 'omega'}

## PARTIE OMEGA ET ALPHA MANGENT 
def IA_food_eaten(wolves, food)


## PARTIE LES LOUPS MANGENT 
for wolves in player_A:
        for foods in food:
    
            distance = count_cases(wolves, foods)
            distance_x = distance[0]
            distance_y = distance[1]
            food_eaten = foods[key]
            if distance_x <= 1 and distance_y <=1: 
                #vérifie que l'action de se nourrir ait un minimum de sens
                if 100 > player_A[wolves]['life'] and food[foods]['life'] > 0 :
                    IA_game_eat(wolf, food_eaten, orders)  


## POUR CREER L'ORDRE FOOD 
def IA_game_eat(wolf, food_eaten, orders):
    """
    To make the wolves eat

    Parameters
    ----------
    wolf: wolf which will eat (tuple)
    food_eaten: food eaten by the wolf (tuple)
    orders: orders of the IA (str)

    Returns
    -------
    orders: orders of the IA (str)

    Versions:
    ---------
    specification: Aurélie Genot et Aline Boulanger (v.1 31/03/2022)
    specification : Aurélie Genot et Aline Boulanger (v.2 20/04/2022)
    implementation : Aurélie Genot et Aline Boulanger (v.1 31/03/2022)
    implementation : Aurélie Genot et Aline Boulanger (v.2 21/04/2022)
    """
    eat_x = str(wolf[0])
    eat_y = str(wolf[1])
    eaten_x = str(food_eaten[0])
    eaten_y = str(food_eaten[1])

    action = ':<'
    if can_use(orders, int(eat_x), int(eat_y)) == True: 
        orders += orders + eat_x + '-' + eat_y + action + eaten_x + '-' + eaten_y + ' '
    return orders
                        
