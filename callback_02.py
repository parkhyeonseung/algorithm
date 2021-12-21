def func_callback(input):
    print('func_callback sum : ',input)
    return

def func_call(a,b,f_callback):
    f_callback(a+b)
    return 

first = 10
second = 20

func_call(first,second,func_callback)