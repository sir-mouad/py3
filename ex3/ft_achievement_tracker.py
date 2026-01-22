def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice_a = {'first_kill', 'level_10',
               'treasure_hunter', 'speed_demon'}
    bob_a = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie_a = {'level_10', 'treasure_hunter',
                 'boss_slayer', 'speed_demon', 'perfectionist'}
    print(f"Player alice achievements: {alice_a}")
    print(f"Player bob achievements: {bob_a}")
    print(f"Player charlie achievements: {charlie_a}")
    print("\n=== Achievement Analytics ===")
    unique_a = alice_a.union(bob_a, charlie_a)
    print("All unique achievements:", unique_a)
    print(f"Total unique achievements: {len(unique_a)}\n")
    all_players = alice_a.intersection(bob_a, charlie_a)
    print("Common to all players:", all_players)
    rare_alice = alice_a.difference(bob_a, charlie_a)
    rare_bob = bob_a.difference(alice_a, charlie_a)
    rare_charlie = charlie_a.difference(alice_a, bob_a)
    rare_a = rare_alice.union(rare_bob, rare_charlie)
    print(f"Rare achievements (1 player): {rare_a}\n")
    alice_X_bob = alice_a.intersection(bob_a)
    print("Alice vs Bob common:", alice_X_bob)
    alice_u = alice_a.difference(bob_a)
    print("Alice unique:", alice_u)
    bob_u = bob_a.difference(alice_a)
    print("Bob unique:", bob_u)


main()
