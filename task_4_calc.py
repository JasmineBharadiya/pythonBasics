i=0
s=0
avg=0
pro=1
for index in range(0,10):
    n=float(input("enter float: "))
    s+=n
    pro=pro*n
    index=index+1
print "sum is ",s
avg=s/10
print "average is ",avg
print "product is ",pro
