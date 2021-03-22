#minus, mul, div, mymodel
def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mymodel(a,b):
    return a%b

sum = add(1,5)
min = minus(1,5)
mul = mul(1,5)
div = div(1,5)
mod = mymodel(1,5)

print(sum,min,mul,div,mod)

#멀티
def add_min_mul_div_mod(a,b):
    return a+b,a-b,a*b,a/b,a%b

sum,min,mul,div,mod = add_min_mul_div_mod(1,5)

print(sum,min,mul,div,mod) 