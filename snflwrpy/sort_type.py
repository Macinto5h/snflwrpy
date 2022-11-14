"""
Module provides SortType, an Enum used to provide the available
sorting algorithms by name.
"""
from enum import Enum

class SortType(Enum):
    """Enum representing all available sorting algorithms."""

    BOGO = 'bogo'
    BUBBLE = 'bubble'
    COCKTAIL = 'cocktail'
    GNOME = 'gnome'
    INSERTION = 'insertion'
    RADIX_LSD = 'radixlsd'
    SELECTION = 'selection'
    STOOGE = 'stooge'

    @classmethod
    def get_values(cls):
        """Returns a full list of the SortType values"""

        return list(map(lambda sortType: sortType.value, cls))
