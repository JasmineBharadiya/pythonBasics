i=0
l3=[i for i in range(1,50) if i%3==0]
l5=[i for i in range(1,50) if i%5==0]
l35=[i for i in range(1,50) if i%3==0 and i%5==0]
print l3
print l5
print l35
for index in range(1,50):
    if(index%3==0 and index%5==0):
        index="fizzbuzz"
        print index
    elif(index%5==0):
        index="buzz"
        print index
    elif(index%3==0):
        index="fizz"
        print index
     
    else:
        print index

