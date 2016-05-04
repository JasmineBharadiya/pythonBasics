# find unique numbers in list using function

def unique(numbers):
    x=[]
    for a in numbers:
        if a not in x:
            x.append(a)
    return x
print unique([1,2,3,3,4,5])
