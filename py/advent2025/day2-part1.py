# DC1: Format array
# Read the raw_range string and split by ','
# For this split_range and create range with the 2 number
# Send this range to the function responsible to Invalid_id

# DC2: Find invalid IDs


# DC3:Sum all invalid IDs


def format_range(raw_range):
    range_arr = []
    split_range = raw_range.split(",")

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
                find_invalid_ids(range_arr)
            else:
                print("Not valid range numbers")


def find_invalid_ids(range):
    for item in range:
        print(item)


def main() -> None:
    raw_range = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    invalid_ids = []

    # Format range
    format_range(raw_range)

    # Sum invalid numbers


main()
