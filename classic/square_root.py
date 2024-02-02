"""
牛顿迭代法
求数a的平方根，等价于求方程y = x2 - a = 0的解，
假设猜想平方根为b，过点 (b, b2 - a)所作的切线与X轴的交点为 (b + a/b)/2,
将该交点作为猜想的平方根继续做切线，就越来越靠近结果
"""


def func(x):
    a = x   # 待求平方根的数
    b = x   # 猜想的平方根
    while True:
        # 根据一个b值计算出一个res
        res = (b + a / b) / 2

        # 判断两个数的整数部分是否相同
        if int(res) == int(b):
            break

        b = res
        # print(res)

    return int(res)


if __name__ == '__main__':
    X = 0.5
    print(func(X))
