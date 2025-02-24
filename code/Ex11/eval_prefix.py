from operator import add, sub, mul

ops = {"+":add, "-":sub, "*":mul}


def read_prefix() -> list[str]:
    return input().split()


def process_prefix(terms: list[str]) -> int:
    stack = []
    for t in reversed(terms):
        if t in ops:
            stack.append(ops[t](stack.pop(), stack.pop()))
        else:
            stack.append(int(t))
    return stack[0]


def main() -> None:
    print(process_prefix(read_prefix()))

