def double_score(lst: list) -> list:
    i = 0
    while i < len(lst):
        lst[i] = lst[i] * 2
        i += 1
    return lst


def main() -> None:
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    player = []
    score = []
    active = []
    player = ["alice"], ["bob"], ["charlie"], ["diana"]
    score = [2300, 1800, 2150, 2050]
    active = [True, True, True, False]
    height_s = []
    active_player = []
    i = 0
    for s in score:
        if s > 2000:
            height_s += player[i]
        if active[i]:
            active_player += player[i]
        i += 1
    print("High scorers (>2000):", height_s)
    score = double_score(score)
    print("Scores doubled:", score)
    print("Active players:", active_player)
    print("\n=== Dict Comprehension Examples ===")
    player_score = {"alice": 2300, "bob": 1800, "charlie": 2150}
    score_ca = {"height": 3, "medium": 2, "low": 1}
    achivements = {
        "alice": {"slayer", "level_up", "demon", "colector", "level_10"},
        "bob": {"level_up", "level 6", "sniper"},
        "charlie": {"boss_slayer", "first_kill", "level_up", "level_14",
                    "clector", "head_shot", "sniper"}
    }
    print("Player scores:", player_score)
    count_ach = dict()
    print("Score categories:", score_ca)
    for name in achivements:
        count_ach[name] = len(achivements[name])
    print("Achievement counts:", count_ach)
    print("\n=== Set Comprehension Examples ===")
    player_u = {'alice', 'bob', 'charlie'}
    alice_a = {'first_kill', 'level_10',
               'treasure_hunter', 'speed_demon'}
    bob_a = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie_a = {'level_10', 'treasure_hunter',
                 'boss_slayer', 'speed_demon', 'perfectionist'}
    active_re = {'north', 'east', 'central'}
    unique_a = alice_a.union(bob_a, charlie_a)
    print("Unique players:", player_u)
    print("Unique achievements:", unique_a)
    print("Active regions:", active_re)
    print("\n=== Combined Analysis ===")
    print("Total players:", len(player))
    print("Total unique achievements:", len(unique_a))
    total = 0
    for name in player_score:
        total += player_score[name]
    avrage = total / len(player_score)
    print(f"Average score: {avrage:.1f}")
    top = 0
    for name in player_score:
        if player_score[name] > top:
            top = player_score[name]
            top_name = name
    print(
        f"Top performer: {top_name} ({player_score[top_name]} points", end=",")
    print(f" {len(achivements[top_name])} achivements)")


if __name__ == "__main__":
    main()
