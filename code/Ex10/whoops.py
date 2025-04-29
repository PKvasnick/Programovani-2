def divide(x, y):
    print('entering divide')
    try:
        print(x/y)
    except ZeroDivisionError:
        print('error')
    else:
        print('no error')
    finally:
        print('exit')

divide(1, 1)
divide(1, 0)