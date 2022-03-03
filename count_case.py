def count_cases(e1, e2):
    """
    Count the cases that separes two elements
    
    Parameters:
    ------------
    e1: position of the first element (tuple)
    e2: position of the second element (tuple) 
    
    Returns:
    --------
    distance: the number of cases that separes two things on the board (int)
    
    Versions:
    ----------
    specification: Louise Delpierre (v.1 19/02/2022)
    """
    x_1 = e1[0]
    y_1 = e1[1]
    x_2 = e2[0]
    y_2 = e2[1]

    x = x_2 - x_1
    distance_x = abs(x)
    y = y_2 - y_1
    distance_y = abs(y)

    distance = (distance_x, distance_y)
    return distance 


print(count_cases ((4,4), (1,3)))
