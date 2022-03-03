player_1 = {(2,2): {'type': 'alpha', 'life': 100}, (1,1): {'type': 'omega', 'life': 30}}

def can_pacify(player_A, x_A, y_A):
    """Check if a wolf has enough energy to pacify.
    Parameters:
    -----------
    player_A: wolves of the player playing (dict)
    x_A : the absisse of the wolf's position (int)
    y_A : the ordonate of the wolf's position (int)

    Return:
    -------
    Result: True if it can, False otherwise (bool)

    Versions:
    ---------
    specification: Aline Boulanger (v.1 19/02/2022)
    specification : Aline Boulanger (v.2 03/03/2022)
    implementation : Aline Boulanger (v.1 03/03/2022)
    """

    if player_A[x_A, y_A]["type"] == "omega" :
        if player_A[x_A, y_A]["life"] >= 40 :
            return True
        else :
            return False
    else :
        return False 

print(can_pacify(player_1, 1, 1))