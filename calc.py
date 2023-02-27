'''
A series of calc functions to be used 
as sample unittest snippets
'''

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y ==0:
        raise ValueError("Can't divide by Zero")
    return x/y

'''
niaive alternative to testing

x=5
y=5
print(add(x,y))
'''

if "__name__" =="__main__":
    main()