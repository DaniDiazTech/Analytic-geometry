

class FindInTheLine:
    def __init__(self, x1, y1, y2, x2):
      self.x1 = x1
      self.y1 = y1
      self.x2 = x2
      self.y2 = y2

    def distance(self):
        """
        Calculates the disctance between two coordinates

        """
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5

    def midpoint(self):
        """
        Calculates the midpoint between  two end points
        Returns an array with the midpoint
        The first element is the x axis, and the second the y axis
        """
        return (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2
    
    def slope(self):
        """
        Find the slope of a line.
        """
        return (self.y2 - self.y1) / (self.x2 - self.x1)


if __name__ == "__main__":
    print("In this file are the classes I use in the main.py file")
    pass
