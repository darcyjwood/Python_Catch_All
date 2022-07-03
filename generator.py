
#def gen_range(stop, start=1, step=1):
    #num = start
    #gen_range(10)
    #generator = gen_range(10)
    #while num <= stop:
        #yield num
        #num += step
        
        
#def gen_fib():
    #a, b = 0, 1
    #while True:
        #a, b = b, a + b
        #yield a
        
        
        
def char_range(start, stop, step=1):
    stop_modifier = 1
    start_code = ord(start)
    stop_code = ord(stop)
    
    
    if start_code > stop_code:
        step *= -1
        stop_modifier *= -1

    
    for value in range(start_code, stop_code + stop_modifier, step):
        yield chr(value)
    
    
    



