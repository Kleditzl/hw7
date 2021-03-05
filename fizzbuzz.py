def fizz_print():
    a = []
    for i in range(1, 101):
        if i % 3 == 0:
            a.append("fizz")
        if i % 5 == 0:
            a.append("buzz")
        else:
            a.append(i)
    lstToStr = ' '.join([str(elem) for elem in a])
    return lstToStr


if __name__ == "__main__":
    fizz_print()