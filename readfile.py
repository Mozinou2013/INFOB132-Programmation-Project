def read_file(file):
    """ 
    Read the file and turn it into a data structure 
    Parameters
    -----------
    file : file of the game (file)

    Returns
    -------
    food: food on the map (dict)
    player_1: wolves of the player 1 (dict)
    player_2: wolves of the player 2 (dict)
    width: width of the map (int)
    height: height of the map (int)

    Versions
    --------
    specification : Aurélie Genot (v.1 17/02/2022)
    specification: Eline Mota (v.2 24/02/2022)
    Implementation: Eline Mota (v.1 24/02/2022)
    """
    f = open.file(file, 'r')
    i = 0
    player_1 = {}
    player_2 = {}
    height = 0
    width = 0
    food = {}
    for lines in f.readlines():
        i+=1
        if i == 2:
            liste = lines.split(' ')
            height = liste[0]
            width = liste[1]

        elif i >= 4 and i <= 12:
            liste = lines.split(' ')
            coordonate = (liste[1], liste[2])
            y = liste[3] #enlève le retour à la ligne
            y = y[0:-1]
            player_1[coordonate] = {'type': y, 'life': 100}
            
        elif i > 12 and i <= 21:
            liste = lines.split(' ')
            coordonate = (liste[1], liste[2])
            y = liste[3]
            y = y[0:-1]
            player_2[coordonate] = {'type': y, 'life': 100}
            
        elif i > 22:
            liste = lines.split(' ')
            coordonate = (liste[0], liste[1])
            food[coordonate] = {'type': liste[2], 'life': liste[3]}

    return width, height, player_1, player_2, food

