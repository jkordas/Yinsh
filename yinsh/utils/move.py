"""
Game moves implementations
"""


class PlacementMove(object):
    """
    Represents position where ring should be placed at placement phase
    """

    def __init__(self, x_field, y_field):
        self.x_field = x_field
        self.y_field = y_field

    def __getitem__(self, item):
        if item == 'x':
            return self.x_field
        if item == 'y':
            return self.y_field

    def fake_method_for_pylint(self):
        """
        fake method
        """
        pass

    def fake_method_for_pylint_2(self):
        """
        fake method
        """
        pass


class RingMove(object):
    """
    Represents start position where marker should be added and end position where
    ring should be finally placed
    """

    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

    def __getitem__(self, item):
        if item == 'start_x':
            return self.start_x
        elif item == 'start_y':
            return self.start_y
        elif item == 'end_x':
            return self.end_x
        elif item == 'end_y':
            return self.end_y

    def fake_method_for_pylint(self):
        """
        fake method
        """
        pass

    def fake_method_for_pylint_2(self):
        """
        fake method
        """
        pass
