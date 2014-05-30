# Function 1: local parameter
def func_local(x):
    print 'x is', x
    x = 2
    print 'Changed local x to', x
# Function 2: global parameter
def funcg_lobal():
    global x
    print 'x is', x
    x = 2
    print 'Changed global x to', x
# main body
x = 50
#
func_local(x)
print 'x is still', x
#
funcg_lobal()
print 'Value of x is', x
