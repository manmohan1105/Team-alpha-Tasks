'''
Q swap two variables in python with and without using temporary variable
'''
def function_without_3rd_variable(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b

def function_with_3rd_variable(a,b):
    temp=a
    a=b
    b=temp
    return a,b    