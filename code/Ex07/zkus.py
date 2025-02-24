if m == 0:
    print("Division by zero")
else:
    1 / m


try:
    1 / 0
except ZeroDivisionError:
    print("Division by zero")
