def ConditionalOdd(x):
    result = []
    for i in range(1, x*2):
        if i%2 != 0:
            result.append(i)
    res = ''
    if x%2 == 0:
        res = result[:x-1]
    if res:
        return res
    else:
        return result
print(ConditionalOdd(int(input('Enter Your integer:'))))