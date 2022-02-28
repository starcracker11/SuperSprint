import Line
import Point
import Polygon
import Polygon as polygon
import Point as pointLib
import Line as lineLib
import json


# this class define a location on the track where a player
# has to cross in order to make progress around the track
# they must be gone through in order, so each track marker
# has an index/number associated (we could use the actual index
# into the array it will eventually be stored in but this makes it cleaer)
class TrackMarker:
    def __init__(self, index, line=lineLib.Line):
        self.index = index
        self.line = line

    def get_index(self):
        return self.index


# Track class contains a description of a single track
# an instance (an object) or many of this will be created in CarGame
# to understand how to make classes go here: https://www.w3schools.com/python/python_classes.asp
class Track(object):
    def __init__(self):
        # the two main data elements
        self.polygons = [polygon.Polygon]
        self.track_markers = [TrackMarker]

        # the following are just methods to easily get to first and last marker
        self.starting_line_track_marker = lineLib.Line
        self.ending_line_track_marker = lineLib.Line

        # TODO: again this would need to be loaded in along with track data
        self.max_laps = 3
        # ...if it was a line, we could also workout the starting direction by calculating the perpendicular
        self.starting_direction = 270

        # for now, we will have to hardcode any polygons
        self.generate_track()
        # self.load("test_track_file.json")
        # really this should be a polygon - a 'starting line'
        # and treated separately to the parts of the track

    def generate_track(self):
        # the simplest track consists of two polygons that represent either side of the road
        # in this case one will be 'inside' the other one
        # this concept could be added to created carious obsticles
        # please see documentation ??? for how this works
        # this is based on a 1024x768 setup but these values should be normalised
        # so that we can easily scale to any size

        self.max_laps = 3

        # so first we created the outer part of the track
        tmp_outer_points = [(66, 71), (47, 101), (20, 440), (66, 474), (248, 473), (292, 440), (283, 295), (471, 470),
                            (593, 471), (639, 437), (599, 90), (574, 65), (538, 54), (124, 56)]

        tmp_inner_points = [(162, 166), (145, 352), (166, 354), (178, 222), (207, 187), (240, 176), (304, 175),
                            (336, 189),
                            (508, 358), (493, 171)]

        self.polygons = [polygon.Polygon(tmp_outer_points, (125, 125, 125)),
                         polygon.Polygon(tmp_inner_points, (0, 100, 0))]
        # the problem we now have is that polygons alone aren't much use
        # we now need to add properties - for now we will consider the 'road' to be anywhere
        # and any collection with any polygon means 'not on road'
        print(" polygons created: " + str(len(self.polygons)))

        # self.starting_line = pointLib.Point(328, 78)

        # now create the circuit markers
        # the are lines that must be crossed _in order_
        # so we can determine if car has completed a circuit
        # we need a minimum of 3 markers
        # these will not be visible (unless debugging) to the players
        self.starting_line_track_marker = TrackMarker(0,
                                                      lineLib.Line(pointLib.Point(329, 54), pointLib.Point(328, 162)))
        self.ending_line_track_marker = TrackMarker(2, lineLib.Line(pointLib.Point(508, 360), pointLib.Point(518, 456)))
        self.track_markers = [self.starting_line_track_marker,
                              TrackMarker(1, lineLib.Line(pointLib.Point(158, 364), pointLib.Point(156, 458))),
                              self.ending_line_track_marker]

    def get_starting_line(self):
        return self.track_markers[0]

    def get_ending_line(self):
        return self.track_markers[2]

    def save(self, file_name):
        print('saving track data to file')
        # ANY CHANGE HERE MUST BE REFLECTED IN THE LOAD FUNCTION
        with open(file_name, 'w') as json_file:
            # write out all the track polygons
            tmp_tuples = []

            tmp_poly_tuples = []
            for poly in self.polygons:
                tmp_poly_tuples.append((poly.get_points_as_tuples(), poly.colour))
            tmp_tuples.append(tmp_poly_tuples)

            tmp_tm_tuples = []
            for track_marker in self.track_markers:
                tmp_tm_tuples.append((track_marker.index, track_marker.line.get_points_as_tuples()))
            tmp_tuples.append(tmp_tm_tuples)

            json.dump(tmp_tuples, json_file)

    def load(self, file_name):
        print('Loading track data from file')
        # ANY CHANGE HERE MUST BE REFLECTED IN THE SAVE FUNCTION
        # clear arrays:
        self.polygons = []
        self.track_markers = []
        with open(file_name, 'r') as json_file:
            # write out all the track polygons
            # for poly in self.track.polygons:
            main_data_structure = json.load(json_file)
            for poly_raw in main_data_structure[0]:
                tmp_poly = Polygon.Polygon(poly_raw[0], poly_raw[1])
                self.polygons.append(tmp_poly)

            for track_marker_raw in main_data_structure[1]:
                tmp_p1 = Point.Point(track_marker_raw[1][0][0], track_marker_raw[1][0][1])
                tmp_p2 = Point.Point(track_marker_raw[1][1][0], track_marker_raw[1][1][1])
                tmp_line = Line.Line(tmp_p1, tmp_p2)
                tmp_track_marker = TrackMarker(track_marker_raw[0], tmp_line)
                self.track_markers.append(tmp_track_marker)
