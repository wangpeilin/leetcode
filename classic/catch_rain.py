"""每根柱子能够接到的雨水量取决于左边最大值和右边最大值中较小的那个值"""


def func(height):
    res = 0
    left_high = height[0]
    for i in range(1, len(height)):
        cur = height[i]
        # 寻找右边的最高值
        right_high = 0
        for j in range(i + 1, len(height)):
            if height[j] > right_high:
                right_high = height[j]

        # 当前柱子能够接的雨水
        print(f"left {left_high}, right {right_high}")
        cur_rain = max(0, min(left_high, right_high) - cur)
        res += cur_rain

        # 更新左边的最高值
        if cur > left_high:
            left_high = cur

    return res


if __name__ == '__main__':
    h = [4,2,0,3,2,5]
    print(func(h))
