def new_func(a,b):
    return a+b

x = map(new_func, (1,2),(2,3))

def lambda_check(n):
    return lambda a : a*n

y = lambda_check(2)

print(y(2))