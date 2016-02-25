# http://www.codewars.com/kata/55c0ac142326fdf18d0000af/

class Cube:
    def __init__(self, side=0):
        """Construct the Cube"""
        self._side = abs(side)


    def get_side(self):
        """Return the side of the Cube"""
        return self._side
  
  
    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = abs(new_side)
