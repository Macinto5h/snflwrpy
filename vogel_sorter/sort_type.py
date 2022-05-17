from enum import Enum

class SortType(Enum):
    BUBBLE = 'bubble'
    COCKTAIL = 'cocktail'
    GNOME = 'gnome'
    INSERTION = 'insertion'
    MERGE = 'merge'
    RADIX_LSD = 'radixlsd'
    SELECTION = 'selection'
    SHELL = 'shell'
    STOOGE = 'stooge'

    @classmethod
    def get_values(self):
        return list(map(lambda sortType: sortType.value, self))
