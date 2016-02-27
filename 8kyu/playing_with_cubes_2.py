# http://www.codewars.com/kata/55c0ac142326fdf18d0000af/

class Cube(object):
    def __init__(self, side=0):
        """Construct the Cube"""
        self._side = abs(side)

    @property
    def side(self):
        """Return the side of the Cube"""
        return self._side

    @side.setter
    def side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = abs(new_side)
