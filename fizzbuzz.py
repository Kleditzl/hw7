def fizz_print():
    a = []
    for i in range(1, 101):

        a.append(i)
    lstToStr = ' '.join([str(elem) for elem in a])
    return lstToStr

if __name__ == "__main__":
    fizz_print()