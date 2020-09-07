def dict(x):
    result = {}
    for i in range(1,10):
        count = 0
        for j in x:
           if j%i== 0 and j!=0:
               count +=1
        result[i] = count;
    return result


print(dict([0,1,2,8,9,12,46,76,82,15,20,30]))