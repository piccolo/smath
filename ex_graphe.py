import numpy

def f(x):
    return x**2-2

for x in numpy.linspace(0,5,num=10):
    print(x,f(x))

