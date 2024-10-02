
#Tuple items are ordered, unchangeable, and allow duplicate values.
#A tuple is a collection which is ordered and unchangeable. 

tuple__ = ("apple", "banana", "cherry", "apple", "cherry")
one_item_tuple = ('mango',)


#access tuple 
print(tuple__[-1])
print(tuple__[1])
print(tuple__[2:5])


#Tuples are unchangeable, or immutable 

tuple__ = ("apple", "banana", "cherry", "apple", "cherry")
list__ = list(tuple__)
list__[1] = "kiwi"
tuple__ = tuple(list__)

print(tuple__)


#unpacking tuples 
var__ = ("22", "33", "44")

(a, b, c) = var__

print(a)
print(b)
print(c)



tuple__ = ("apple", "banana", "cherry", "apple", "cherry")
for x in tuple__:
  print(x)

  