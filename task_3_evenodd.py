#count of odd & even in 1-100
i=0
countE=0
countO=0
for index in range(1,100):
    if (index%2==0):
        countE=countE+1
        
    else:
        countO=countO+1
        
print countE," are even"
print countO," are odd"
