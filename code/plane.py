import math
import enum
import numpy as np
import matplotlib.pyplot as plt 

class Plane:
    def __init__(self, PlaneConfig: enum.EnumMeta):
        
        self.altitude: float = PlaneConfig.ALTITUDE.value
        self.y_multiplier: float = PlaneConfig.Y_MULTIPLIER.value
        self.x_multiplier: float = PlaneConfig.X_MULTIPLIER.value
        self.flight_path: int = PlaneConfig.FLIGHT_PATH.value
        self.step: int = PlaneConfig.STEP.value
        self.flight_distance: int = PlaneConfig.FLIGHT_DISTANCE.value
        
        self.flight_paths: dict = {
            0: self.straight_location,
            1: self.sin_location,
            2: self.cos_location,
            3: self.tan_location
        }
 
    def straight_location(self, x: float) -> [float, float]:
        return (x, self.altitude)
    
    def sin_location(self, x: float) -> [float, float]:
        return (x, self.altitude + self.y_multiplier*math.sin(x * self.x_multiplier))

    def cos_location(self, x: float) -> [float, float]:
        return (x, self.altitude + self.y_multiplier*math.cos(x * self.x_multiplier))

    def tan_location(self, x: float) -> [float, float]:
        return (x, self.altitude + self.y_multiplier*math.tan(x * self.x_multiplier))
    
    def change_altitude(self, dy: float) -> None:
        self.altitude += dy
        
    def find_flight_location(self, x: float) -> [float, float]:
        return self.flight_paths[self.flight_path](x)
    
    def chart_flight_path(self) -> np.array:
        
        coordinates = []
        for x in range(0, self.flight_distance, self.step):
            coordinates.append(self.find_flight_location(x))
        
        return np.array(coordinates)
            
    def plot_flight_path(self) -> None:

        coordinates = self.chart_flight_path()
        
        x = coordinates[:,0]
        y = coordinates[:,1]
        
        plt.title("Line graph") 
        plt.xlabel("Distance (m)") 
        plt.ylabel("Altitude (m)") 
        plt.plot(x, y, color ="red") 
        plt.show()
                