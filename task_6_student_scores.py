stdno=int(raw_input("enter student id. "))
tScore=float(raw_input("enter tutorial scores. "))
testScore=float(raw_input("enter test scores. "))
avg=0
avg=tScore+testScore/2
if (avg<40):
    print "Grade F"
else:
    finalScore=float(raw_input("enter final exam scores. "))
    finalScore=finalScore/2
    tScore=tScore/4
    testScore=testScore/4
    totalScore=finalScore+tScore+testScore
if(totalScore<50):
    print "Grade E"
elif(totalScore<=60):
    print "Grade D"
elif(totalScore<=70):
    print "Grade c"
elif(totalScore<=80):
    print "Grade B"
else: 
    print "Grade A"
    
