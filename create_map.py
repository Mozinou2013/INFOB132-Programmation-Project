def create_map(width, height, player_1, player_2, food): 
    """ 
    Create the map of the board 
    Parameters
    ----------
    width: width of the map (int)
    lenght: lenght of the map (int)
    player_1: wolves of the player 1 (dict)
    player_2: wolves of the player 2 (dict)
    food : food on the map (dict)
    Versions
    --------
    specification : Louise Delpierre (v1 17/02/2022)
    implementation: Eline Mota (v.1 28/02/2022)
    """
    print(term.home + term.clear)
    for x in range(0, width * 3, 3):
        for y in range(0, height, 1):
            if (x+y)%2 ==0:
                print(term.move_xy(x, y) + term.on_lavenderblush3 + '   ')
            else:
                print(term.move_xy(x, y) + term.on_snow2 + '   ')
    for key in player_1:
        if player_1[key]['type'] =='alpha':
            x = key[0]
            y = key[1]
            x, y = trans_coord(x, y)
            print(term.move_xy(x, y) + term.slateblue1 + term.on_darkolivegreen3 + 'A')
        elif player_1[key]['type'] =='omega':
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x, y) + 'O')
        else:
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x, y) + 'L')
    for key in player_2:
        if player_2[key]['type'] =='alpha':
            x = key[0]
            y = key[1]
            x, y = trans_coord(x, y)
            print(term.move_xy(x, y) + term.purple4 +'A')
        elif player_2[key]['type'] =='omega':
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x, y) +'O')
        else:
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x, y) +'L')
    for key in food:
        if food[key]['type'] == 'berries':
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x,y) +'b')
        elif food[key]['type'] == 'apples':
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x,y) + 'a')
        elif food[key]['type'] == 'mice':
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x,y) + 'm')
        elif food[key]['type'] == 'rabbits':
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x,y) + 'r')
        elif food[key]['type'] == 'deers':
            x = key[0]
            y = key[1]
            x, y = trans_coord(x,y)
            print(term.move_xy(x,y) + 'd')
        else:
            raise ValueError('something is wrong with the file')
