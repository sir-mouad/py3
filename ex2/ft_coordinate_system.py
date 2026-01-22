import math


def calculate_distanse(position: tuple) -> float:
    px, py, pz = position
    distance = math.sqrt((px-0)**2 + (py-0)**2 + (pz-0)**2)
    return distance


def parsing_check_float(str_p: str) -> tuple:
    str_p = str_p.split(",")
    position = tuple()
    for i in str_p:
        try:
            position += (int(i),)
        except ValueError:
            try:
                position += (float(i),)
            except ValueError:
                position += (int(i),)
    return position


def main() -> None:
    print("=== Game Coordinate System ===")
    position0 = (10, 20, 5)
    print("\nPosition created:", position0)
    distance = calculate_distanse(position0)
    print(f"Distance between (0, 0, 0) and {position0} : {distance:.2f}\n")
    str_p = "3,4,0"
    position1 = parsing_check_float(str_p)
    px1, pz1, py1 = position1
    print(f"Parsing coordinates: \"{px1},{py1},{pz1}\"")
    print("Parsed position:", position1)
    distance = calculate_distanse(position1)
    print(f"Distance between (0, 0, 0) and {position1} : {distance:.2f}\n")
    str_p = "abc,def,ghi"
    try:
        position2 = parsing_check_float(str_p)
        px1, pz1, py1 = position2
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{str_p}\"")
        print("Error parsing coordinates:", e)
        print(f"Error details - Type: ValueError, Args: (\"{e}\",)\n")
    print("Unpacking demonstration:")
    print(f"Player at x={px1}, y={py1}, z={pz1}")
    print(f"Coordinates: X={px1}, Y={py1}, Z={pz1}")


main()
