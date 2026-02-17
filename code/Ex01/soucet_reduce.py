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


def sum_by_digits(a0: list[int], b0: list[int]) -> list[int]:
    """
    Sums two integers given as lists of digits.
    :param a0: list of digits of the first number
    :param b0: list of digits of the second number
    :return: list of digits of the sum
    """
    a = a0.copy()     # to protect from side effects
    b = b0.copy()
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
