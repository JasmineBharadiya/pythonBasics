# find howmany characters in string is upper case and lower case

def countUL(str):
    cu=0
    cl=0
    for i in str:
        if i.isupper():
            cu=cu+1
        elif i.islower():
            cl=cl+1
        else :
            pass
    print cu
    print cl
print countUL("HeLLo")
