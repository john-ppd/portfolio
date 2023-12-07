import random

# allowed chars within our generated password
list_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
list_symbols = ["! @ # $ % ^ & * ( ) _ - = + [ ] { } : ; \" ' / ? > < \ | "]
list_numbers = ["0 1 2 3 4 5 6 7 8 9"]
list_symbols = list_symbols[0].split()
list_numbers = list_numbers[0].split()
print(list_symbols)

# Loop while taking user input until the input is valid
while True:
    try:
        password_length = int(input("How long is password?"))
        password_symbols = int(input("How many symbols?"))
        password_upper = int(input("How many upper case?"))
        password_numbers = int(input("How many numbers?"))
        password_string = ""
        password_lower = password_length - password_symbols - password_upper - password_numbers

        if password_lower > 0:
            print()
            break
        else:
            print()
            print('Try again, the password length was exceeded by what you added')
    except:
        print('What you typed was not a valid number')


# generate lower case
password_lower_case = ""
for i in range(0, password_lower):
    # add each random lower case to lower case string
    password_string += list_letters[random.randint(0, len(list_letters) - 1)]
print('lower added:', password_string)

# generate symbols
for i in range(0, password_symbols):
    password_string += list_symbols[random.randint(0, len(list_symbols) - 1)]
print('symbols added:', password_string)

# generate upper case
for i in range(0, password_upper):
    password_string += list_letters[random.randint(0, len(list_letters) - 1)].upper()
print('upper added:', password_string)

# generate numbers
for i in range(0, password_numbers):
    password_string += random.choice(list_numbers)
print('all non scrambled:', password_string)

# randomize index locations
final_string = ''.join(random.sample(password_string, len(password_string)))
print()
print('Your final password is:', final_string)
