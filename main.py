from code.config import PlaneConfig
from code.plane import Plane

def main() -> int:
    
    plane = Plane(PlaneConfig=PlaneConfig)
    plane.plot_flight_path()
    return 0

if __name__ == "__main__":
    main()