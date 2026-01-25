# Problem LeetCode 3090. Maximum Length Substring With Two Occurrences


def max_substring(array):
    right, left = 0, 0
    _max_repetion = 1
    dic_char = {}

    dic_char[array[0]] = 1
    while right < len(array) - 1:
        right += 1
        if dic_char.get(array[right]):
            dic_char[array[right]] += 1
        else:
            dic_char[array[right]] = 1
        while dic_char[array[right]] == 3:
            dic_char[array[left]] -= 1
            left += 1
        _max_repetion = max(_max_repetion, right - left + 1)

    return _max_repetion


if __name__ == "__main__":
    char_array = ["b", "c", "b", "b", "b", "c", "b", "a"]

    print(max_substring(char_array))
