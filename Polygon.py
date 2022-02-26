class Polygon(object):
    def __init__(self):
        # this is hard coded but in the future will be loaded truigh the setter function
        self.points = [Point(10, 10), Point(20, 20), Point(30, 30), Point(40, 40), Point(50, 50), Point(60, 60)]
# probably not needed
    def Get_Points(self):

        return self.points
    def set_points(self, array):
        self.points = array
