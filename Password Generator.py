import random

print('''Welcome to your own Password Generator
----------------------------------------------------''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('Amount of Passwords to be generated: ')
number = int(number)

length = input('Enter Your Password length: ')
length = int(length)

print('Here are your Random Passwords right from the oven: ')
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
