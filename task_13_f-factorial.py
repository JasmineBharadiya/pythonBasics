# calculate factorial of number with function

def fact(n):
    if n==0:
        return 1
    else :
        return n*fact(n-1)
n=int(raw_input("enter a number : "))
print fact(n)
