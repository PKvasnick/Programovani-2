from itertools import accumulate, zip_longest


def add_and_carry(accumulator: tuple[int, int], digits: tuple[int, int]) -> tuple[int, int]:
    """
    Přičte součet dvou dalších číslic a přenosu, vrací aktualizovaný součet a přenos.
    :param accumulator: tuple of the running sum and carry
    :param digits: tuple of two new digits to add
    :return: tuple of updated sum and carry
    """
    carry, old_sum = accumulator
    a, b = digits
    new_sum = a + b + carry
    return divmod(new_sum, 10)  # returns (carry, digit_sum)


def sum_by_digits(a: list[int], b: list[int]) -> list[int]:
    """
    Sums two integers given as lists of digits.
    :param a0: list of digits of the first number
    :param b0: list of digits of the second number
    :return: list of digits of the sum
    """
    tuples = list(accumulate(zip_longest(a, b, fillvalue=0), func=add_and_carry, initial=(0,0)))
    tuples.reverse()
    tuples.pop()    # remove initial state
    carry = tuples[0][0]
    result = [carry] if carry != 0 else []
    result += [v for u, v in tuples]
    return result


def main() -> None:
    """
    Demonstrates the sum_by_digits function.
    """
    a = [int(c) for c in input()]
    b = [int(c) for c in input()]
    print("First number: ", *a, sep = "")
    print("Second number: ",*b, sep = "")
    digit_sum = sum_by_digits(a, b)
    print("Sum: ", *digit_sum, sep="")
    print("Check:")
    a_int = int("".join([str(d) for d in a]))
    b_int = int("".join([str(d) for d in b]))
    print("Int addition: ", a_int + b_int)


if __name__ == "__main__":
    main()
