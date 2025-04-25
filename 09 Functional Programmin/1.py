#3 functions fun(), disp() and msg().Store them in a list and call them one by one 
# in a loop.

def fun():
    print("This is function fun()")

def disp():
    print("This is function disp()")

def msg():
    print("This is function msg()")

function_list = [fun, disp, msg]

list(map(lambda f: f(), function_list))