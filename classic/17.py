KEY = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


def letterCombinations(digits: str):
    if digits == "":
        return []

    res = [""]
    for num in digits:
        res = [x + d for x in res for d in KEY[num]]

    return res


if __name__ == '__main__':
    s = '48'
    print(letterCombinations(s))
