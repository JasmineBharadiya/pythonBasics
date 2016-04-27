import random
a=int(raw_input("guess a no. between 1-10: "))

rA=random.randint(1,10)

if(rA==a):
    print "well guessed"
else :
    print "try again"
