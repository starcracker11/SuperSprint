import GameMob
import Car as carLib
import Track as trackLib


class User(object):
    def __init__(self, name, colour):
        self.name = str(name)
        self.lap_counter = 0
        # self.lives = int(Lives)
        self.car = carLib.Car(8, 18, 10, 4, 10, 10, colour)
        self.current_track_marker = trackLib.TrackMarker(0)
        self.reset_lap_counter()

    def set_track_marker(self, new_track_marker):
        self.current_track_marker = new_track_marker

    def get_track_marker(self):
        return self.current_track_marker

    def get_lap_counter(self):
        return self.lap_counter

    def reset_lap_counter(self):
        self.lap_counter = 0

    def increment_lap_counter(self):
        self.lap_counter += 1
        print("incrementing lap counter for " + self.name + ": " + str(self.lap_counter))

    def update_state(self, track):
        self.car.update_state()
