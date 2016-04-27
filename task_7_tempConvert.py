#convert temp in c'to f' vice-versa
resultF=0
resultC=0
a=int(raw_input("press 1. for fahrenhit to celcius and 2. celcius to fahrenhit "))

if(a==1):
    f=int(raw_input("enter fahrenhit: "))
    resultF=int(round(f-32)*5/9)
    print "celcius is ",resultF
elif(a==2):
    c=int(raw_input("enter celcius: "))
    resultC=int(round(c*9)/5+32)
    print "fahrenhit is ",resultC
print "good bye"
