import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this script square a number")

    parser.add_argument("number", type=int, help="the number of square")

    args = parser.parse_args()

    squared_number = args.number ** 2
    print(f"the square number is {squared_number}")

    