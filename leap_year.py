def ly(a):
    if a % 100 != 0:
        if a % 4 == 0:
            return True
    else:
        return False

if __name__ == '__main__':
    a = 4
    ly(a)