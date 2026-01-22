import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    len_arg = len(sys.argv)
    if len_arg == 1:
        print("No scores provided. Usage: ", end="")
        print("python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        i = 1
        scorses = []
        while i < len_arg:
            try:
                num = int(sys.argv[i])
            except ValueError as e:
                print(e)
                return
            scorses = scorses + [num]
            i += 1
        print("scores processed:", scorses)
        print("Total players:", len_arg - 1)
        print("Total score:", sum(scorses))
        average = sum(scorses) / (len_arg - 1)
        print("Average score:", average)
        print("High score:", max(scorses))
        print("Low score:", min(scorses))
        score_range = max(scorses) - min(scorses)
        print("Score range:", score_range)


main()
