def thousands_separators(number: int or str or float, separator: str=" ") -> str:
    """Convert a number to a string with thousands separators.
    
    :param number: The number that we would like to convert in string with thousands separators
    :type number: int or string or float

    :param separator: Separator used
    :default separator: space
    :type separator: string

    :return: String with separator between groups of thousands
    """
    # Convert the number to int or float if it's string
    if isinstance(number, str):
        if ',' in number or '.' in number: # If number is a float
            exit = number.replace(',', '.') # Replace comma to dot if number is in french format
            exit = float(exit)
        else:
            exit = int(number)
    else:
        exit = number       
            
    return '{0:,}'.format(exit).replace(',', ' ')