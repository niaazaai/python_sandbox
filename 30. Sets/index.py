
#SETS - A set is a collection which is unordered, unchangeable*, and unindexed.

 
 
set__ = {"apple", "banana", "cherry", "apple"}
set2 = {'abc' , 'eft'}

set__.update(set2)

set__.remove('abc')
#access items 
for item in set__:
  print(item)

# Once a set is created, you cannot change its items, but you can add new items.
# however you can change it to list and manipulate it. 

set__.add('grapes')


# add new set to old one
new_set__ = {'mango' , 'watermilon'}
set__.update(new_set__)
print(set__)

# remove items 
set__.remove('grapes')
set__.remove('banana')
print(set__)