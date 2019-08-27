import math


def angle_to_sexigesimal(angle_in_degrees, decimals=3):
    """
    Convert the given RA angle from degree to a sexigesimal string of hours:minutes:seconds.

    Parameters
    ----------
    angle_in_degrees : float
        A scalar angle of RA, expressed in degrees

    Returns
    -------
    hms_str : str
        The sexigesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`

    """
    #if math.floor(decimals) != decimals:
    #    raise OSError('decimals should be an integer!')
    if type(decimals) != int:
        print('Warning : Decimals should be an integer! Converting it now (if possible)')
        decimals = int(decimals)

    hours_num = angle_in_degrees/15.0
    hours = math.floor(hours_num)

    min_num = (hours_num - hours)*60.0
    minutes = math.floor(min_num)

    seconds = (min_num - minutes)*60.0

    format_string = '{}:{}:{:.' + str(decimals) + 'f}'
    return format_string.format(hours, minutes, seconds)
