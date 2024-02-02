def func(digits):
    div = 1
    for i in range(len(digits) - 1, -1, -1):
        cur = digits[i] + div
        div, mod = cur // 10, cur % 10
        print(div, mod)
        digits[i] = mod

        if div == 0:
            break

    if div == 1:
        digits = [1] + digits

    return digits


if __name__ == '__main__':
    s = [9, 9, 9]
    print(func(s))
