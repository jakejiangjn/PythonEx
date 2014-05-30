# Filename: printMax.py
# Function: Output the larger obkect
def printMax(a, b):
    '''Prints the maximum of two numbers.\nThe two values must be integers.\n''' # printMax.__doc__
    a = int(a);  b = int(b);
    if a > b:
        print a, 'is maximum';
        return a;
    else:
        print b, 'is maximum';
        return b;
# main body
printMax(3, 4); # directly give literal values
x = 5;y = 7;
printMax(x, y); # give variables as arguments
print printMax.__doc__;
