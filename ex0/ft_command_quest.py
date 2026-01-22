import sys


def main() -> None:
    print("=== Command Quest ===")
    len_arg = len(sys.argv)
    if len_arg == 1:
        print("No arguments provided!")
        print("Program name:", sys.argv[0])
        print("Total arguments:", len_arg)
    else:
        print("Program name:", sys.argv[0])
        print("Arguments received:", len_arg - 1)
        i = 1
        while i < len_arg:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print("Total arguments:", len_arg)


if __name__ == "__main__":
    main()
