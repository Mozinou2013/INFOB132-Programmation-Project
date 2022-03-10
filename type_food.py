def type_food(type):
    '''
    Indentify the type of the food 
    parameters
    ----------
    type : the type of the food (str)

    return
    -------
    type : the type of the food (str)

    Version 
    -------
    specification: Louise Delpierre (v.1 03/03/2022)
    implementation: Eline Mota (v.1 03/03/2022)  
    '''

    if type == 'berries':
        types = 'b'
    elif type == 'apples':
        types = 'a'
    elif type == 'mice':
        types = 'm'
    elif type == 'rabbits':
        types = 'r'
    elif type == 'deers':
        types = 'd'
    return types
