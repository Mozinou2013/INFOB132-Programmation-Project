def check_life(player_A, case):
    """Check if a wolf has zero life

    Parameters:
    ----------
    player_A: wolves of the player playing (dict)
    case: place of the wolf we want to check (tuple)

    Return:
    -------
    Result: True if the wolf has zero life, False otherwise (bool)

    Versions:
    ---------
    specification: Eline Mota (v.1 19/02/2022)
    implementation: Aline Boulanger, Louise Delpierre (v.1 02/03/2022
    Eline Mota (v.2 03/03/2022)

    """
    if player_A[case]['life'] == 0:
        return True
    else:
        return False
