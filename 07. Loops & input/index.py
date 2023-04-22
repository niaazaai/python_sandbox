#
# num = int(input('enter a number please'))
#
# if num % 2 == 0 :
#     print('the number is even')
# elif num % 2 != 0 :
#     print('the number is odd')
# else:
#     print('noting!')


# num = 1 ;
#
# while num < 10 :
#     print(num)
#     num = num + 1
#
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
#
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)


#
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")


name = ['ahmad' , 'safwan' , 'mahmood' , 'khalid' , 'doe']

counter = 0;
name_length = len(name)

while counter < name_length :
    print(f"==> {name[counter]}")
    counter = counter+1



# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'cat' in pets :
#     pets.remove('cat')
# print(pets)
#
#
# pets1 = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets1)
#
# counter1 = 0
# while counter1 < len(pets1):
#     if(pets1[counter1] == 'cat'):
#         pets1.remove(pets1[counter1])
#     counter1 = counter1 + 1
# print(pets1)
#


response = {}
polling_active = True;
while polling_active :
    name = input('What is your name ? ')
    if name == 'quite':
        break
    idea = input(f'Dear {name} What is you Idea about this project? ')
    response[name] = idea

print(response)
