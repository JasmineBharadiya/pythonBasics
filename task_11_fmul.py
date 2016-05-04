#multiplication of numbers using function

def multi(numbers):
    result=1
    for x in numbers:
        result*=x
        x=x+1
    return result
print multi([1,2,3,4,5,6,7,8,9])
print multi([2,2])
