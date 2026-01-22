import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) == 1:
        print("python3 ft_inventoru_system.py <key1> : <value1>  ...")
        return
    inventory = dict()
    i = 1
    while i < len(sys.argv):
        try:
            inventory[sys.argv[i]] = int(sys.argv[i+2])
        except ValueError as e:
            print(e)
            return
        i += 3
    values = inventory.values()
    total_items = 0
    for value in values:
        total_items += value
    print("Total items in inventory:", total_items)
    print("Unique item types:", len(inventory))
    print("\n=== Current Inventory ===")
    keys = inventory.keys()
    tmp = dict()
    while len(tmp) < len(inventory):
        max_value = -1
        max_key = ""
        for key in keys:
            if key not in tmp and inventory[key] > max_value:
                max_value = inventory[key]
                max_key = key
        tmp[max_key] = max_value
        percent = (max_value / total_items) * 100
        if max_value > 1:
            print(f"{max_key}: {max_value} units ({percent:.2f}%)")
        else:
            print(f"{max_key}: {max_value} unit ({percent:.2f}%)")
    print("\n=== Inventory Statistics ===")
    max_key = ""
    max_value = -1
    for key in keys:
        if inventory[key] > max_value:
            max_value = inventory.get(key)
            max_key = key
    print(f"Most abundant: {max_key} ({max_value} units)")
    min_value = max_value
    min_key = ""
    for key in keys:
        if inventory[key] < min_value:
            min_value = inventory.get(key)
            min_key = key
    print(f"Least abundant: {min_key} ({min_value} unit)")
    print("\n=== Item Categories ===")
    tmp = {max_key: max_value}
    if max_value >= 10:
        print("abundant", tmp)
    print("Moderate:", tmp)
    tmp = dict()
    for key in keys:
        if key != max_key:
            tmp[key] = inventory[key]
    if tmp == {}:
        print("Scarce: Nothing")
    else:
        print("Scarce:", tmp)
    print("\n=== Management Suggestions ===")
    tmp = dict()
    for key in keys:
        if inventory[key] == 1:
            tmp[key] = 1
    res = list(tmp.keys())
    print(f"Restock needed: {res}")
    print("\n=== Dictionary Properties Demo ===")
    lst = []
    for key in keys:
        lst += [key]
    print("Dictionary keys:", lst)
    lst = []
    for value in values:
        lst += [value]
    print("Dictionary values:", lst)
    print("Sample lookup - 'sword' in inventory:", 'sword' in inventory)


main()
