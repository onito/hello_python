""" THE LEAST SURPRISE LAW : Don't use weired thing too much.
 - Substitution for docstring, not forced usage, similar to SCALA.
"""


def ohms_law(I: 'Current'=10, R: 'Resistance'=50) -> 'Voltage':
    """ ASSIGN ANNOTATIONS AS DICT.
    {'I': 'Current', 'R': 'Resistance', 'return': 'Voltage'}
    """
    return I * R


_a = ohms_law.__annotations__
print(_a)


_voltage = ohms_law()
print('voltage = %s v' % _voltage)
