##FUNCTION 2: LOG FOR ANY BASE
#Okay so this takes some more explaining. Idk if logs are native to python but numpy and pylab is on page 3 of the instructions, not page 2. In any case, I do know the change of base formula.
def logb(argument, base):
    #simple enough, if you just have log base 10
    return log(argument)/log(base)

##FUNCTION 1: LOG FOR BASE 10
#The fun part
#I used logarithmic and exponential equivalence. logb(a) = r == b^r = a
#It basically solves for r, by granting the expression of 10 to an exponent and comparing it to the argument
#It's not perfect of course, but it seems to be able to work fine with tested numbers, and adding 0's to the acceptable range makes it more accurate
def log(argument):
    #The different between calculated and actual argument can be this small:
    acceptableRange = 0.000000000000001
    #Just a big number to start off with, it should get immediately overwritten
    WorkingDiff = 9999999999
    #This number goes down over time, trying to get closer to the actual argument
    WorkingRange = 1
    #Stores the closest number to the return value
    WorkingExp = 1
    #Buffer number to not always overwrite workingDiff and wind up in an endless loop
    tempDiff = 0;
    #Loops while the difference between argument and calculated argument is greater then the range
    while(WorkingDiff > acceptableRange):
        #Stores possible exponent values: low, medium, and high
        lowExp = WorkingExp-WorkingRange
        highExp = WorkingExp+WorkingRange
        #Stores possible argument calculations: low, medium, and high
        low = 10**(lowExp)
        mid = 10**WorkingExp
        high = 10**(highExp)
        #Stores the differences in absolute value between the calculated and actual argument
        lowDiff = abs(argument-low)
        midDiff = abs(argument-mid)
        highDiff = abs(argument-high)
        #Sets the current diff and working exp based on closest values
        if(lowDiff < midDiff and lowDiff < highDiff):
            tempDiff = lowDiff
            WorkingExp = lowExp
        elif(midDiff < lowDiff and midDiff < highDiff):
            tempDiff = midDiff
        else:
            tempDiff = highDiff
            WorkingExp = highExp
        #If the buffer number is in fact smaller, workingDiff gets overwritten
        if(tempDiff < WorkingDiff):
            WorkingDiff = tempDiff
        else:
            #If it isn't, the calculations overshot the correct number, so just halve the search range
            WorkingRange = WorkingRange/2
        #The exact exponent has been found, and should be returned
        if(WorkingDiff == 0):
            return WorkingExp
        #Decrease the working range to narrow search
        WorkingRange = WorkingRange * 0.9
    #I tried to do this to rid myself of the remainder. I'm not sure if it worked properly, but it seems fine in testing
    return (WorkingExp-(WorkingExp%acceptableRange))


#ASSIGNMENT DIRECTIONS:

#1. Asks the user to enter a number “x”
#2. Asks the user to enter a number “y”
#3. Prints out number “x”, raised to the power “y”.
#4. Prints out the log (base 2) of “x”.


#1. Asks the user to enter a number “x”
#try catch and while loop to continually ask for input if input is not a number.
x = ""
while(type(x) != type(0.0)):
    try:
        temp = float(input("Please input number x. "))
        x = temp
    except ValueError:
        print("Input must be a number.")

        
#2. Asks the user to enter a number “y”  
y = ""
while(type(y) != type(0.0)):
    try:
        temp = float(input("Please input number y. "))
        y = temp
    except ValueError:
        print("Input must be a number.")

#3. Prints out number “x”, raised to the power “y”.
print("x: (" + str(x) + ") raised to the power of y: (" + str(y) + ") is " + str(x**y))

#4. Prints out the log (base 2) of “x”.
print("the log (base 2) of x: (" + str(x) + ") is: " + str(logb(x,2)))


