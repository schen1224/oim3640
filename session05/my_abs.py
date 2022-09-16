print("exercise 3-5:")
a=4
def my_abs(x):
    "this is our own version of abs. return the abs value of x"
    if isinstance(x,(int,float)):
        if x < 0:
            return -x
        else:
            return x
    else: 
        print('I don\'t know how to solve this' ) 
        raise TypeError('We do not accept this type as argument')  # return immediately ends the function


print(my_abs(a))
if__name__='__main__'
# running as the main program but does not execute if loaded with input

def f2(x):
    x = 10
    return x *2
    
print(f2(2))