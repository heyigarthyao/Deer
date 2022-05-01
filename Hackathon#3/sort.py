# This python file is designed to sort the result of number guessing game based on name, date, # of steps.


def sort_by_steps() -> int:
    """
    This function takes argument "boolean" which is bool indicates '
    whether this function should sort ascending order(True) or descending order(False)

    """
    lst = []
    with open("ranking.txt", "r") as f:
        num = len(f.readlines())
        for i in range(num):
            lst.extend(f.readline().split(","))
    return lst

if __name__ == "__main__":
    print(sort_by_steps())


# num = f.readline().split(",")
# print(num[0])
# print(len(f.readlines()))