# PofP srpn basic coursework


# creating our primary stack
srpnstack = []

# random list current position
randpos = 0
# hashfilter for parsing comments
hashfilter = False

numbers = ['1','2','3','4','5','6','7','8','9','0']
operators = ['+','-','^', '*', '/', '%', 'd', '=']


# random number list 
randlist = [1804289383, 846930886, 1681692777, 1714636915, 957747793, 424238335, 719885386, 1649760492, 596516649, 1189641421,
1025202362, 1350490027, 783368690, 1102520059, 2044897763, 1967513926, 1365180540, 1540383426, 304089172, 1303455736, 35005211, 521595368]

# function to parse the input in the appropriate way, taking into account spaces and negatives
def inputparser(inputstring):
    global hashfilter
    blankspace = True
    negativenumber = False
    lastinteger = False
    splitstring = []
    finallist = []
    # splits each string character into a list
    for char in inputstring[0 : len(inputstring) : 1]:
        splitstring.append(char)
    # loop to correctly parse inputs with regards to spacing and order
    for x in range(0,len(splitstring)):
        # deals with hashes
        if splitstring[x] == '#':
            hashfilter = not hashfilter
        elif hashfilter is False:
            # deals with spaces
            if splitstring[x] == ' ':
                blankspace = True
                lastinteger = False
            # deals with negative numbers
            elif splitstring[x] == '-' and blankspace == True:
                finallist.append(splitstring[x])
                negativenumber = True
                lastinteger, blankspace = (False,False)
            # deals with operators
            elif splitstring[x] in ['+','-','^', '*', '/', '%', 'r', 'd', '=']:
                finallist.append(splitstring[x])
                lastinteger, negativenumber = (False,False)
            # deals with numbers 
            elif splitstring[x] in numbers:
                if negativenumber == True or lastinteger ==True:
                    finallist[-1]+=str(splitstring[x])
                else:
                    finallist.append(splitstring[x])
                    lastinteger = True
            # deals with irregular inputs
            elif splitstring[x] not in numbers:
                finallist.append('0')
                negativenumber = False
                lastinteger = False
    return finallist

# defining the r function
def r():
    global randpos
    randnum = randlist[randpos]
    randpos = (randpos+1) % 22
    return randnum


# takes the parsed inputs and separates them for stack calculation
def srpncalculator(unparsedinputs):
    parsedinputs = inputparser(unparsedinputs)
    for item in parsedinputs:
        if item in ['+','-','^', '*', '/', '%', 'd', '=']:
            srpnoperator(item)
        else:
            srpnoperands(item)

# defines what to do with the operators for x
def srpnoperator(operator):
    # return whole stack
    if operator =='d':
        if len(srpnstack) == 0:
            print(-2147483648)
        else:
            # displays only integer values
            for operand in srpnstack:
                print(int(operand))
    # stack peek
    elif operator == '=':
        if len(srpnstack) == 0:
            print('Stack empty.')
        else:
            print(int(srpnstack[-1]))
    else:
        # if there are not 2 operands on the stack, return stack underflow
        if len(srpnstack) >= 2:
            operand2 = srpnstack.pop()
            operand1 = srpnstack.pop()
            # basic calculations
            operatorCheck(operand1, operand2, operator)
        else:
            print('Stack underflow.')



def operatorCheck(operand1, operand2, operator):
    if operator == '+':
        finaloperand = operand1 + operand2
    elif operator == '-':
        finaloperand = operand1 - operand2
    elif operator == '*':
        finaloperand = operand1 * operand2
    elif operator == '^':
        if operand2 >= 0:
            finaloperand = operand1**operand2
        else:
            print('Negative power.')
            srpnstack.append(operand1)
            srpnstack.append(operand2)
            return
    elif operator == '/':
        try:
            finaloperand = operand1 / operand2 
        except ZeroDivisionError:
            print('Divide by 0.')
            srpnstack.append(operand1)
            srpnstack.append(operand2)
            return
    elif operator == '%':
        try:
            finaloperand = operand1 % operand2 > 2147483647
        except:
            print('Divide by 0.')
            srpnstack.append(operand1)
            srpnstack.append(operand2)
            return
    boundcheck(finaloperand)

# check the bounds of every number
def boundcheck(finaloperand):
    if finaloperand > 2147483647:
        srpnstack.append(2147483647)
    elif finaloperand < -2147483648:
        srpnstack.append(-2147483648)
    else:
        srpnstack.append(finaloperand)


    



        
# defines what to do for the numbers, stored as floats for computations
def srpnoperands(operand):
    # checks for stack overflow
    if len(srpnstack) + 1 > 23:
        print('Stack overflow.')
    else:
        # checks for random number function
        if operand == 'r':
            srpnstack.append(float(r()))
        else:
            # pushes latest operand onto the stack
            if float(operand) > 2147483647:
                srpnstack.append(float(2147483647))
            elif float(operand) < -2147483648:
                srpnstack.append(float(-2147483648))
            else:
                srpnstack.append(float(operand))

def process_command(command):
    return srpncalculator(command)
        



if __name__ == "__main__": 
    while True:
        try:
            cmd = input()
            pc = process_command(cmd)
            if pc != None:
                print(str(pc))
        except:
            exit()

