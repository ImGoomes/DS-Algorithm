# Problem Advent of Code 2025
# https://adventofcode.com/2025/day/2


import numpy as np


# format_range(raw_range:str): [[int]]
# This function will recive the raw input range of number in
# string format and convert it into a matrix of integer
# return a matrix of integer
def format_range(raw_range: str) -> list[list[int]]:
    range_matrix = []
    split_range = raw_range.split(",")

    for item in split_range:
        range_array = []
        range_numbers = item.split("-")

        # Verify if is a valid range (two or higher)
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
def find_invalid_ids(range_matrix: list[list[int]]) -> list[int]:
    invalid_ids_range = []

    for range_array in range_matrix:
        for item in range_array:
            # Split it number of the range in an array of integer
            item_array = list(map(int, str(item)))

            # Verify if the number is divisible by 2
            # Req: The number must be repeted at least twice
            print(item_array)
            if len(item_array) % 2 == 0:
                slice_index = len(item_array) // 2

                first_slice = int("".join(map(str, item_array[:slice_index])))
                second_slice = int("".join(map(str, item_array[slice_index:])))

                if first_slice == second_slice:
                    invalid_ids_range.append(item)
            else:
                index = find_next_equal_number(item_array)

                if index > 0 and len(item_array) % index == 0:
                    slice_index = len(item_array) // index
                    is_repeted_numbers = True
                    print(item_array)
                    print(f"SLICE {slice_index}")
                    slice_matrix = np.array_split(item_array, slice_index)
                    last_array = slice_matrix[0]
                    for array in slice_matrix:
                        print(last_array)
                        print(array)
                        if not np.array_equal(array, last_array, equal_nan=False):
                            is_repeted_numbers = False

                    if is_repeted_numbers:
                        invalid_ids_range.append(item)

    return invalid_ids_range


# sum_invalid_ids(invalid_ids: [int]): int
# This function is responsible to sum all invalid_ids
# return the total amount
def sum_invalid_ids(invalid_ids: list[int]) -> int:
    return sum(invalid_ids)


def find_next_equal_number(item_array: list[int]) -> int:
    first_number = item_array[0]
    array_without_first_item = item_array[1:]
    array_index = 1
    for number in array_without_first_item:
        if first_number == number:
            break
        else:
            array_index += 1

    if array_index >= len(item_array):
        array_index = 0

    return array_index


def main() -> None:
    # raw_range = "269194394-269335492,62371645-62509655,958929250-958994165,1336-3155,723925-849457,4416182-4470506,1775759815-1775887457,44422705-44477011,7612653647-7612728309,235784-396818,751-1236,20-36,4-14,9971242-10046246,8796089-8943190,34266-99164,2931385381-2931511480,277-640,894249-1083306,648255-713763,19167863-19202443,62-92,534463-598755,93-196,2276873-2559254,123712-212673,31261442-31408224,421375-503954,8383763979-8383947043,17194-32288,941928989-941964298,3416-9716"
    raw_range = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    ranges = format_range(raw_range)
    invalid_ids = find_invalid_ids(ranges)
    print(invalid_ids)
    total_sum = sum_invalid_ids(invalid_ids)
    print(total_sum)


main()
