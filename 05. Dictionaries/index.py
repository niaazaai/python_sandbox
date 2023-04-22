
# alien = { 'color': 'green', 'points': 5, 'live' :3 }
# for al in alien:
#     print(al)


# alien = {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
# alien['color'] = 'yellow'
# print(alien['color'])
# print(alien)

# for al in alien:
#     print(al)


# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")
#
# # Move the alien to the right.
# # Determine how far to move the alien based on its current speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be a fast alien.
#     x_increment = 3
#
# # The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")


# alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(alien.get('speed1' , 'there is no element called speed1 in the alien dictionary'))
# # print(alien['speed1'])



# DICTIONARY FORM OFFICE :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# cars = ['bmw' , 'flexo' , 'voxwagon' , 'ford' , 'ferrari']
# for car  in cars:
#     print(f"new cars : {car}") 


# contract = {'id' : 22 , 'name' : 'glucose' , 'Price': 100}

# for k , v in contract.items():
#     print(f"{k} => {v}")


# # working with only keys 
# for k in contract.keys():
#     print(f"the key is :  {k}")

# # working with only keys  - the default behavior is that looping throgh keys  
# for k in contract:
#     print(f"the key is (default) :  {k}")

# # working with values only 
# for v in contract.values():
#     print(f" values are :  {v}")



# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }
# friends = ['phil', 'sarah']

# for name in favorite_languages:
#     if name in friends: 
#         language = favorite_languages[name].title()
#         print(f"Hi I see you liked { language} Language")


# # working with sets , is the the list of unique values 
# for values in set(favorite_languages.values()): 
#     print(values)

#this set will automatically remvoe the duplicate elements 
# languages = {'python', 'rust', 'python', 'c'}
# print(languages)


# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens: 
#     print(alien['color'])



# we have list 
# we have tuples 
# we have dictionaries 
# we have sets 




# students = {'ahmad' , 'mahmood' , 'khalid' , 'ahmad'}
# print(students)

# lists = ['ahmad' , 'mahmood' , 'khalid' , 'ahmad']
# print(lists)

# tuple_ = ('ahmad' , 'mahmood' , 'khalid' , 'ahmad')
# print(tuple_)

# favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}
# print(favorite_languages)
# for key in sorted(favorite_languages.keys()) : 
#     print(key)




# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:4]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")




race = {
    'name' : 'formulla' ,
    'cars' : ['bmw' , 'flexo' , 'voxwagon' , 'ford' , 'ferrari'] , 
}

print(race)



favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}


for key , value  in favorite_languages.items(): 
    for v in value : 
        print(f"{key}'s favorite language is {v}")

# or more optimized way is 

for key , value  in favorite_languages.items(): 
        print(f"\t{key}'s favorite language is {value}")



# dictionary inside dictionary 

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}

for username , information in users.items(): 
    print(f"Username : {username}")
    print(f"\t Fullname {information['first']} {information['last']}")
    print(f"\t Location {information['location']}")










