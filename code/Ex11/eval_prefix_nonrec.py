from collections import deque


def parse(tokens):
    token = tokens.popleft()
    if token == '+':
        return parse(tokens) + parse(tokens)
    elif token == '-':
        return parse(tokens) - parse(tokens)
    elif token == '*':
        return parse(tokens) * parse(tokens)
    else:
        return int(token)


if __name__ == '__main__':
    print(parse(deque(input().split())))
