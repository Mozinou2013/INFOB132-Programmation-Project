def check_case(case, dictionnary_checked):
    """Check if there is an element of the dictionnary on a case 
    
    Parameters:
    -----------
    case: a case of the map (tuple)
    dictionnary_checked: dictionnary in which we check the information(dict)

    Return:
    -------
    Result: True if there is a item on the case, False otherwise (bool)

    Versions:
    ---------
    specification: Louise Delpierre (v.1 19/02/2022)
    specification: Aurélie Genot (v.2 03/03/2022)
    implementation: Aurélie Genot (v.1 03/03/2022)
    """
    for key in dictionnary_checked :
        if case == key :
            return True 
        else:
            return False
                   
