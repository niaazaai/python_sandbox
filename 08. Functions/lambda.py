
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression

lamb__ = lambda a, b,c : (a * b) + c
print(lamb__(5, 6, 2))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))


