import math
print("=== Game Coordinate System ===")
position0 = ("10", "20", "5")
px, py, pz = position0
position1 = ("3", "4", "0")
px1, py1, pz1 = position1
position2 = ("abc", "def", "ghi")
px2, py2, pz2 = position2
print("\nPosition created:", position0)
distance = math.sqrt((int(px)-0)**2 + (int(py)-0)**2 + (int(pz)-0)**2)
print(f"Distance between (0, 0, 0) and {position0} : {distance:.2f}\n")
print(f"Parsing coordinates: \"{px1},{py1},{pz1}\"")
print("Parsed position:", position1)
distance = math.sqrt((int(px1)-0)**2 + (int(py1)-0)**2 + (int(pz1)-0)**2)
print(f"Distance between (0, 0, 0) and {position1} : {distance:.2f}\n")
print(f"Parsing coordinates: \"{px2},{py2},{pz2}\"")
try:
    distance = math.sqrt((int(px2)-0)**2 + (int(py2)-0)**2 + (int(pz2)-0)**2)
except ValueError as e:
    print(f"Parsing invalid coordinates: \"{px2},{py2},{pz2}\"")
    print("Error parsing coordinates:", e)
    print(f"Error details - Type: ValueError, Args: (\"{e}\",)\n")
print("Unpacking demonstration:")
print(f"Player at x={px1}, y={py1}, z={pz1}")
print(f"Coordinates: X={px1}, Y={py1}, Z={pz1}")
