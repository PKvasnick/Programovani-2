from itertools import zip_longest
from itertools import accumulate


def sum_by_digits(a : list[int], b : list[int]) -> list[int]:
    '''
    Sums two integers given as lists of digits.
    :param a: list of digits of the first number
    :param b: list of digits of the second number
    :return: list of digits of the sum
    '''
    a.reverse()     # this is cheap for lists, but causes side effect
    b.reverse()
    tuples = list(accumulate(zip_longest(a, b, fillvalue=0), func=add_and_carry, initial=(0,0)))
    tuples.reverse()
    tuples.pop()    # remove initial state
    carry = tuples[0][1]
    result = [carry] if carry != 0 else []
    result += [u for u, v in tuples]
    a.reverse()     # correct side effect!
    b.reverse()
    return result


def main() -> None:
    a0 = [int(c) for c in input()]
    b0 = [int(c) for c in input()]
    print("First number: ", *a0, sep = "")
    print("Second number: ",*b0, sep = "")
    digit_sum = sum_by_digits(a0, b0)
    print(*digit_sum, sep="")
    print("Kontrola:")
    a0_int = int("".join([str(d) for d in a0]))
    b0_int = int("".join([str(d) for d in b0]))
    print(a0_int + b0_int)


if __name__ == "__main__":
    main()
