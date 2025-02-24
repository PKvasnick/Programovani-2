import re

def is_number(s):
    """
    Determines if a given string represents a number.
    """
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_name(s):
    """
    Determines if a string matches a regular alphanumeric pattern.
    """
    return bool(re.match(r'\w+', s))

def peek(stack):
    """
    Peeks at the top element of a stack without popping it.
    """
    return stack[-1] if stack else None

def apply_operator(operators, values):
    """
    Applies an operator to the two most recent values in the values stack.
    """
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    formula = "{0}{1}{2}".format(left, operator, right)
    values.append(eval(formula))

def greater_precedence(op1, op2):
    """
    Determines if the precedence of op1 is greater than op2.
    """
    precedences = {'+' : 0, '-' : 0, '*' : 1, '/' : 1}
    return precedences[op1] > precedences[op2]

def evaluate(expression):
    """
    Evaluates a mathematical expression using the Shunting Yard Algorithm.
    """
    tokens = re.findall(r'[+/*()-]|\d+', expression)
    values, operators = [], []
    for token in tokens:
        if is_number(token):
            values.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while peek(operators) and peek(operators) != '(':
                apply_operator(operators, values)
            operators.pop() # Discard the '('
        else:
            while peek(operators) and peek(operators) not in "()" and greater_precedence(peek(operators), token):
                apply_operator(operators, values)
            operators.append(token)
    while peek(operators):
        apply_operator(operators, values)
    return values[0]

# Example demonstration:
def main():
    expression = '((20 - 10 ) * (30 - 20) / 10 + 10 ) * 2'
    print("Shunting Yard Algorithm Result:", evaluate(expression))
    print("Native Python Evaluation:", eval(expression))

if __name__ == '__main__':
    main()