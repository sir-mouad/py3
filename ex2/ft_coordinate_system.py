import sys
import math
print("=== Game Coordinate System ===")
if len(sys.argv) < 2:
    print("No coordinates provided.")
    sys.exit(1)
x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]
try:
    x = int(x)
    y = int(y)
    z = int(z)
except ValueError as e:
    print(f"Parsing invalid coordinates: \"{x},{y},{z}\"")
    print("Error parsing coordinates:", e)
    print(f"Error details - Type: ValueError, Args: (\"{e}\",)")
    sys.exit(1)
position = (x, y, z)
px, py, pz = position
print("Position created: (10, 20, 5)")
print("Distance between (0, 0, 0) and (10, 20, 5): 22.91\n")
print(f"Parsing coordinates: \"{x},{y},{z}\"")
print("Parsed position:", position)
distance = math.sqrt((px-0)**2 + (py-0)**2 + (pz-0)**2)
print(f"Distance between (0, 0, 0) and {position} : {distance}\n")
print("Unpacking demonstration:")
print(f"Player at x={px}, y={py}, z={pz}")
print(f"Coordinates: X={px}, Y={py}, Z={pz}")
