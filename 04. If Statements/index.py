

# cars = ['toyota' , 'bmw' , 'ford' , 'ferarri' , 'lamborgani']
#
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())



# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# x =  'mushrooms' in requested_toppings
# print(x)
#
# if 'onions' not in requested_toppings :
#     print('Please bring some onines with you')
# elif 'tomato' not in requested_toppings :
#     print('Please bring some tomatos with you also')
# else :
#     print('Please remember the shoping list I gave you !')
#
# # print('onions' not in requested_toppings)
#
# print('------------------------------------')
#
#
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')


user_list  = ['mahmood' , 'ahmad' , 'khalid' , 'samim' , 'doe' , 'ezikul' , 'tony']
username = input('What is your name?');

if username in user_list:
     print(f"Hi,  {username}")
else :
     print("sorry your are not in the list !")

# for user in user_list:
#     if username == user :
#         print(f"Welcome {username}")
#     else:
#         print("Access denied!")

age =  12;

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
