import Polygon as polygon
import Point as mathsLib


# Track class contains a description of a single track
# an instance (an object) or many of this will be created in CarGame
# to understand how to make classes go here: https://www.w3schools.com/python/python_classes.asp
class Track(object):
    def __init__(self):
        self.polygons = [polygon.Polygon]
        # for now, we will have to hardcode any polygons
        self.generate_track()

    def generate_track(self):
        # the simplest track consists of two polygons that represent either side of the road
        # in this case one will be 'inside' the other one
        # this concept could be added to created carious obsticles
        # please see documentatioin ??? for how this works
        # this is based on a 1024x768 setup but these values should be normalised
        # so that we can easily scale to any size

        # so first we created the outer part of the track
        tmp_outer_points = [(66,71), (47, 101), (20, 440), (66, 474), (248, 473), (292, 440), (283, 295), (471, 470),
                      (593, 471), (639, 437), (599, 90), (574, 65), (538, 54), (124, 56)]

        tmp_inner_points = [(162, 166), (145, 352), (166, 354), (178, 222), (207, 187), (240, 176), (304, 175), (336, 189),
                     (508, 358), (493, 171)]

        self.polygons = [polygon.Polygon(tmp_outer_points), polygon.Polygon(tmp_inner_points)]
        # the problem we now have is that polygons alone aren't much use
        # we now need to add properties - for now we will consider the 'road' to be anywhere
        # and any collection with any polygon means 'not on road'
        print(" polygons created: " + str(len(self.polygons)))
