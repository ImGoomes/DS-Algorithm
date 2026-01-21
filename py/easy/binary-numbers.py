def convert_to_base2(number_base10, binary_array):
    if number_base10 == 0:
        return binary_array

    division_result = number_base10 // 2
    remaing = number_base10 % 2
    binary_array.append(remaing)

    return convert_to_base2(division_result, binary_array)


def find_max_occurence(target, source):
    max_occurence = 0
    temp_occurence = 0
    for item in source:
        if item == target:
            temp_occurence += 1
        else:
            temp_occurence = 0

        if temp_occurence > max_occurence:
            max_occurence = temp_occurence

    return max_occurence


if __name__ == "__main__":
    n = int(input().strip())

    if n > 0:
        binary_array = []
        convert_to_base2(n, binary_array)
        print(find_max_occurence(1, binary_array[::-1]))
