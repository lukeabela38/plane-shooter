from enum import Enum

class PlaneConfig(Enum):
    ALTITUDE: float = 100
    Y_ALTITUDE_MULTIPLIER: float = 1
    X_ALTITUDE_MULTIPLIER: float = 0.1
    TIME_INTIAL: int = 0
    TIME_STEP: int = 1
    FLIGHT_DURATION: int = 250
    INITIAL_SPEED: float = 2
    ACCELERATION: float = 0.005
    FLIGHT_PATH: int = 1 # 0 - straight path, 1 - sin path, 2 - cos path, 3 - tan path