# DC1: Format array
# Read the raw_range string and split by ','
# For this split_range and create range with the 2 number
# Send this range to the function responsible to Invalid_id

# DC2: Find invalid IDs
# Verify if it divisible by 2
# Verify if first array is equal second array
# Add the invalid IDs into array

# DC3:Sum all invalid IDs
# Sum all invalid IDs


def format_range(raw_range):
    range_arr = []
    split_range = raw_range.split(",")
    invalid_ids = []

    for item in split_range:
        range_numbers = item.split("-")

        # Verify if is a valid range (only two numbers)
        if len(range_numbers) <= 2:
            start = int(range_numbers[0])
            end = int(range_numbers[1])

            # Verify if is a valid range (start is lower than end number)
            if start < end:
                # end + 1: range does not consider last index
                range_arr = range(start, end + 1)

                # Verify invalid number
                invalid_ids += find_invalid_ids(range_arr)
            else:
                print("Not valid range numbers")

    return invalid_ids


def find_invalid_ids(range):
    invalid_ids_range = []
    for item in range:
        item_arr = list(map(int, str(item)))

        if len(item_arr) % 2 == 0:
            slice_index = int(len(item_arr) / 2)

            first_slice = int("".join(map(str, item_arr[:slice_index])))
            second_slice = int("".join(map(str, item_arr[slice_index:])))

            if first_slice == second_slice:
                invalid_ids_range.append(item)

            # print(f"FIRST: {first_slice}")
            # print(f"SECOND: {second_slice}")

            # else:
            # print(f"Not divisible by 2 - Length {len(item_arr)}")

    return invalid_ids_range


def sum_invalid_ids(invalid_ids):
    result = 0
    for item in invalid_ids:
        result += item

    return result


def main() -> None:
    # raw_range = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    raw_range = "269194394-269335492,62371645-62509655,958929250-958994165,1336-3155,723925-849457,4416182-4470506,1775759815-1775887457,44422705-44477011,7612653647-7612728309,235784-396818,751-1236,20-36,4-14,9971242-10046246,8796089-8943190,34266-99164,2931385381-2931511480,277-640,894249-1083306,648255-713763,19167863-19202443,62-92,534463-598755,93-196,2276873-2559254,123712-212673,31261442-31408224,421375-503954,8383763979-8383947043,17194-32288,941928989-941964298,3416-9716"
    invalid_ids = []

    # Format range
    invalid_ids += format_range(raw_range)

    # Sum invalid numbers
    print(sum_invalid_ids(invalid_ids))


main()
