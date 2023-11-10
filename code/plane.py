import math
import enum
import numpy as np
import matplotlib.pyplot as plt 

class Plane:
    def __init__(self, PlaneConfig: enum.EnumMeta):
        
        self.altitude: float = PlaneConfig.ALTITUDE.value
        self.y_altitude_multiplier: float = PlaneConfig.Y_ALTITUDE_MULTIPLIER.value
        self.x_altitude_multiplier: float = PlaneConfig.X_ALTITUDE_MULTIPLIER.value
        self.flight_path: int = PlaneConfig.FLIGHT_PATH.value
        self.time_initial: int = PlaneConfig.TIME_INTIAL.value
        self.flight_duration: int = PlaneConfig.FLIGHT_DURATION.value + self.time_initial
        self.time_step: int = PlaneConfig.TIME_STEP.value
        self.initial_speed: float = PlaneConfig.INITIAL_SPEED.value
        self.acceleration: float = PlaneConfig.ACCELERATION.value

        self.flight_paths: dict = {
            0: self.straight_location,
            1: self.sin_location,
            2: self.cos_location,
            3: self.tan_location
        }

    def get_speed(self, t: int) -> float:
        return self.initial_speed + self.acceleration * t
    
    @staticmethod
    def get_displacement(speed: float, t: int) -> float:
        return speed * t
    
    def straight_location(self, x: float) -> float:
        return self.altitude
    
    def sin_location(self, x: float) -> float:
        return self.altitude + self.y_altitude_multiplier*math.sin(x * self.x_altitude_multiplier)

    def cos_location(self, x: float) -> float:
        return self.altitude + self.y_altitude_multiplier*math.cos(x * self.x_altitude_multiplier)

    def tan_location(self, x: float) -> float:
        return self.altitude + self.y_altitude_multiplier*math.tan(x * self.x_altitude_multiplier)
    
    def change_altitude(self, dy: float) -> None:
        self.altitude += dy
        
    def find_flight_location(self, x: float) -> [float, float]:
        return self.flight_paths[self.flight_path](x)
    
    def chart_flight_path(self) -> np.array:
        
        coordinates = []
        for t in range(self.time_initial, self.flight_duration, self.time_step):

            acceleration: float = self.acceleration
            speed: float = self.get_speed(t)
            displacement: float = self.get_displacement(speed, t)
            altitude: float = self.find_flight_location(displacement)

            coordinates.append((t, acceleration, speed, displacement, altitude))
        
        return np.array(coordinates)
            
    def plot_flight_path(self) -> None:

        coordinates = self.chart_flight_path()
        
        t = coordinates[:,0]
        a = coordinates[:,1]
        s = coordinates[:,2]
        x = coordinates[:,3]
        y = coordinates[:,4]
        
        plt.figure(1, figsize=(10, 5))

        plt.title("Time v Acceleration")
        plt.xlabel("Time (s)")
        plt.ylabel("Accleration (m/s/s)")
        plt.plot(t, a, color="green")
        plt.savefig("artifacts/TimeAcceleration.png", bbox_inches="tight")
        plt.close()

        plt.figure(2, figsize=(10, 5))

        plt.title("Time v Speed")
        plt.xlabel("Time (s)")
        plt.ylabel("Speed (m/s)")
        plt.plot(t, s, color="green")
        plt.savefig("artifacts/TimeSpeed.png", bbox_inches="tight")
        plt.close()

        plt.figure(3, figsize=(10, 5))

        plt.title("Time v Distance")
        plt.xlabel("Time (m)")
        plt.ylabel("Distance (m)")
        plt.plot(t, x, color="green")
        plt.savefig("artifacts/TimeDistance.png", bbox_inches="tight")
        plt.close()

        plt.figure(4, figsize=(10, 5))

        plt.title("Time v Altitude")
        plt.xlabel("Time (s)")
        plt.ylabel("Altitude (m)")
        plt.plot(t, y, color="green")
        plt.savefig("artifacts/TimeAltitude.png", bbox_inches="tight")
        plt.close()




                