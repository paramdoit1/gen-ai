# Try block will generate an exception, because x is not defined

try:
    print(tree)
except NameError:
    print('X not defined')
except:
    print('Exception Occured')

# X not defined

# We can use else keyword to define block of code to be executed if no error occurs.


try:
    print('Hello world')
except:
    print('Exception occured')
else:
    print('Execution complete')

'''
Hello world
Execution complete
'''
