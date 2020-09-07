def Odd(x):
    result = []
    for i in range(1, (x)*2):
        if i%2 != 0:
            result.append(i)
    return result
print(Odd(int(input('Enter Your integer:'))))