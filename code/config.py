from enum import Enum

class PlaneConfig(Enum):
    ALTITUDE: float = 10
    Y_MULTIPLIER: float = 0.5
    X_MULTIPLIER: float = 0.25
    STEP: int = 1
    FLIGHT_DISTANCE: int = 10
    FLIGHT_PATH: int = 3 # 0 - straight path, 1 - sin path, 2 - cos path, 3 - tan path