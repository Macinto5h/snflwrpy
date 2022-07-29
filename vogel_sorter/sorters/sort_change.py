class SortChange:
    def __init__(self, index, old_value, new_value):
        self.index = index
        self.old_value = old_value
        self.new_value = new_value

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.index == other.index and self.old_value == other.old_value and self.new_value == other.new_value