import traceback

def fat(x):
    print(f"\nCurrent call stack: fat({x})")
    traceback.print_stack(limit=20)
 
    if x == 1:
        return 1
    else:
        return x * fat(x-1)


def main():
    number = int(input("Inform a number:"))
    result = fat(number)
    print("Result: ", result)

main()
