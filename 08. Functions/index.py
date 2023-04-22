# def describe_pet1(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet1(animal_type='hamster', pet_name='harry')



# # we have four things to remember 
# """
# def describe_pet(animal_type, pet_name) <- this is parameter
# def describe_pet(animal_type='dog', pet_name) <- this is a default value for parameter if argument value is not provided we can call it like  describe_pet('jaik') 
# describe_pet('dog', 'jaik') <- this is argument or the value of parameter that is passed to function is called arguments 
# describe_pet(animal_type='hamster', pet_name='harry') <- this is called Keyword Arguments 
# describe_pet( 'hamster', 'harry') <- this is called positional Arguments 

# """



# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")


# # A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')

# # A hamster named Harry.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')




# def format_name(name): 
#     return name.title(); 

# print(f"The Formated Name is : {format_name('mahmood khan')}")



# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)



# def format_name(firstname , lastname):
#     fullname = f"{firstname} {lastname}"
#     return fullname.title(); 


# dict = {
#     100144 : {"firstname" : "Ahmad" , "lastname" : "Khan" }, 
#     100145 : {"firstname" : "zakir" , "lastname" : "jalil" },
#     100146 : {"firstname" : "samet" , "lastname" : "suhrab" },
#     100147 : {"firstname" : "Khalil" , "lastname" : "Wadood" },
#     100148 : {"firstname" : "Haris" , "lastname" : "Wadood" },
# }


# for key , value in dict.items(): 
#     print(f"{key} :::::::::::::> { format_name (value['firstname'] , value['lastname'] ) }")





# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)

# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)





# # Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# #  Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)



# def print_models(unprinted_designs, completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)




# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a pizza with the following toppings:")
#     print(type(toppings))
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')



# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')





# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)





# def build_profile(first='' , last='' , **info):
#     info['firstname'] = first
#     info['lastname'] = last 
#     return info 


# info_ = build_profile (location = 'kabul' , degree = 'bachlor' , age=23 )
# print(info_)


# from pizza import build_profile as bp 
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


import pizza as p 
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
 
# print(bp(location = 'kabul' , degree = 'bachlor' , age=23 ))

print('Please explain many to many relationship in laravel ')

