
"""
Mission:
Write a “eval” function that returns the result of a given phrase (String) like "5-4*2+12/3". 
In this example it returns 1. 
P.S. please write the full code and do not use external library
"""

def exp_breakdown(expression):
    math_signs = ['+','-','*','/']
    breakdown = []
    index = 0
    index_last_sign = -1
    # Check the prase doesn't start with a sign. If starts with '-', it's ok and shoult be treated as negative number
    if expression[0] in math_signs:
        if expression[0] != '-':
            raise Exception("Incorrect input")
        else:
            expression = '0'+expression

    # Break expression to numbers and signs
    while index<len(expression):
        if expression[index] in math_signs:
            # Check for no two signs one after the other
            if index == index_last_sign+1:
                raise Exception("Incorrect input")
            try:
                val = int(expression[index_last_sign+1:index])
            except:
                raise Exception("Incorrect input")
            # Add the number to the array
            breakdown.append(val)
            # Add the sign to the array
            breakdown.append(expression[index])
            # Remember the last place a sign appeared
            index_last_sign = index
        index += 1
    # Add last number in phrase to the array
    try:
        val = int(expression[index_last_sign+1:len(expression)])
    except:
        raise Exception("Incorrect input")
    breakdown.append(val)
    return breakdown



def calculate(breakdown):

    num1 = 0;
    num2 = 0;

    mult = False
    div = False
    sub = False

    for element in breakdown:
        if element == "+":
            if sub:
                num1 -= num2
            else:
                num1 += num2
            num2 = 0
            sub = False
        elif element == "-":
            if sub:
                num1 -= num2
                num2 = 0
            sub = True
        elif element == "*":
            mult = True
        elif element == "/":
            div = True
        else:
            if mult:
                num2 *= element
                mult = False
            elif div:
                num2 /= element
                div = False
            elif sub:
                num1 += num2
                num2 = element
            else:
                num2 = element
    if sub:
        result = num1-num2
    else:
        result = num1+num2

    return result

# Check stability of code for different cases
def test():

    test_expression = ('5-4*2+12/3',
                        '5 -4*2+12 /3 ',
                        '5-4*2+/3',
                        'a-4*2+12/3',
                        '-4*2+12/3',
                        '*2+12/3',
                        '5-4*2+12/',
                        '5/4*2+12',
                        '3+5-4',
                        '5-4-2*4',
                        '24/2/3',
                        '2*3*4*5*6-4-3-5-6'
                        )

    for expression in test_expression:
        try:
            breakdown = exp_breakdown(expression)
        except:
            print(expression)
            print("Incorrect input")
        else:
            result = calculate(breakdown)
            print(expression,'=',result)


def main():
    
    #test()

    # Ask for a phrase from user
    expression = input("Please enter a math phrase: ")
    
    # Calculate value
    try:
        breakdown = exp_breakdown(expression)
    except:
        print("Incorrect input")
    else:
        result = calculate(breakdown)
        print(expression,'=',result)
        return result

if __name__ == '__main__':
    main()

