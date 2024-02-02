# 有效的括号
def isValid(s: str) -> bool:
    Map = {
        "]": "[",
        ")": "(",
        "}": "{"
    }
    stack = []
    for x in s:
        if x in Map.values():
            stack.append(x)
        else:
            if stack == [] or stack.pop(-1) != Map[x]:
                return False
    return stack == []
