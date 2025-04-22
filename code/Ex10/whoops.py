def whoops():
    try:
        return True
    finally:
        return False

print(whoops())