def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)


def main():
    number = int(input("Inform a number:"))
    result = fat(number)
    print("Result: ", result)

main()
