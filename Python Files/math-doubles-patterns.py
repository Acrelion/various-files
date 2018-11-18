# This script is to visualize the pattern when 
# combining digits of numbers.

def combine(doubled_str):
    """
    Helper function to recursively combine the digits of a number.
    64 = 6 + 4 = 10 = 1 + 0 = 1
    """
    combined = 0

    for y in doubled_str:
        combined += int(y)

    if combined >= 10:
        recursive_result = combine(str(combined))
        return recursive_result
    else:
        return combined


def regular(original):
    """
    May need different increment methods,
    so this is a plugable incremenention method.
    """
    return original * 2


def print_with_columns(data):
    """
    Helper function to print numbers in proper columns.
    Credit to Shawn Chin at StackOverflow.
    """
    col_width = max(len(word) for row in data for word in row) + 2  # padding

    for row in data:
        print("".join(word.ljust(col_width) for word in row))

    print("\n\n")

def main(start_int, typefunc=regular):
    """
    Iterate a set number of times, calculating the recursive
    adding of numbers.
    """
    result_arr = []
    original = start_int

    for i in range(1, 25):
        doubled = typefunc(original)
        doubled_str = str(doubled)
        combined = combine(doubled_str)

        result_arr.append([str(original), str(doubled), str(combined)])

        original = doubled

    print_with_columns(result_arr)

main(1)
main(3)
main(6)
main(9)

"""
The result is:
1. Gives idea of patterns existing when iterating numbers.
"""
