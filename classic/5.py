# 寻找两个数组合并后第k小的数
def get_k(num1, num2, k):
    # 如果一个数组空了，那么只需要在另一个数组中找第k小的数即可
    if len(num1) == 0:
        return num2[k - 1]
    if len(num2) == 0:
        return num1[k - 1]

    # 退出递归的条件，此时已经要找到中位数了
    if k == 1:
        return min(num1[0], num2[0])

    s1 = min(len(num1), k // 2)
    s2 = min(len(num2), k // 2)
    if num1[s1 - 1] > num2[s2 - 1]:
        return get_k(num1, num2[s2:], k - s2)
    else:
        return get_k(num1[s1:], num2, k - s1)


if __name__ == '__main__':
    m = [5]
    n = [2, 6, 8, 12, 14, 15, 27, 30, 32]
    res = (get_k(m, n, (len(m) + len(n) + 1) // 2) + get_k(m, n, (len(m) + len(n) + 2) // 2)) / 2
    print(res)
