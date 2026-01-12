# Problem Advent of Code 2025
# https://adventofcode.com/2025/day/2

# format_range(raw_range:str): [[int]]
# This function will recive the raw input range of number in
# string format and convert it into a matrix of integer
# return a matrix of integer
def format_range(raw_range):
    range_matrix = []
    split_range = raw_range.split(",")

    for item in split_range:
        range_array = []
        range_numbers = item.split("-")

        # Verify if is a valid range (only two numbers)
        if len(range_numbers) <= 2:
            start = int(range_numbers[0])
            end = int(range_numbers[1])

            # Verify if is a valid range (start is lower than end number)
            if start < end:
                # end + 1: range does not consider last index
                range_array += range(start, end + 1)

                # Append in the full array
                range_matrix.append(range_array)
            else:
                print("Not valid range numbers")

    return range_matrix


# find_invalid_ids(range_matrix: [[int]]): [int]
# This function is find the invalid IDs existing int the range
# return a integer array of all invalid IDs
def find_invalid_ids(range_matrix):
    invalid_ids_range = []

    for range_array in range_matrix:
        for item in range_array:
            # Split it number of the range in an array of integer
            item_array = list(map(int, str(item)))

            # Verify if the number is divisible by 2
            # Req: The number must be repeted twice only
            if len(item_array) % 2 == 0:
                slice_index = int(len(item_array) / 2)

                first_slice = int("".join(map(str, item_array[:slice_index])))
                second_slice = int("".join(map(str, item_array[slice_index:])))

                if first_slice == second_slice:
                    invalid_ids_range.append(item)

    return invalid_ids_range


# sum_invalid_ids(invalid_ids: [int]): int
# This function is responsible to sum all invalid_ids
# return the total amount
def sum_invalid_ids(invalid_ids):
    total = 0
    for item in invalid_ids:
        total += item

    return total


def main() -> None:
    raw_range = "269194394-269335492,62371645-62509655,958929250-958994165,1336-3155,723925-849457,4416182-4470506,1775759815-1775887457,44422705-44477011,7612653647-7612728309,235784-396818,751-1236,20-36,4-14,9971242-10046246,8796089-8943190,34266-99164,2931385381-2931511480,277-640,894249-1083306,648255-713763,19167863-19202443,62-92,534463-598755,93-196,2276873-2559254,123712-212673,31261442-31408224,421375-503954,8383763979-8383947043,17194-32288,941928989-941964298,3416-9716"
    invalid_ids = []
    ranges = []

    ranges = format_range(raw_range)
    invalid_ids = find_invalid_ids(ranges)
    total_sum = sum_invalid_ids(invalid_ids)
    print(total_sum)


main()
