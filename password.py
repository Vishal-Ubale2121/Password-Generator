import random
import string

print('Welcome to Password Generator!')

print("==============================")
num_of_alphabet = int(input('\nNumber of alphabets: '))
num_of_digit = int(input('Number of Digits: '))
special_characters = int(input('Number of Special characters: '))

if num_of_alphabet+num_of_digit+special_characters >= 8:
  random_alphabet = random_digit = random_character=''

  for i in range(num_of_alphabet):
    random_alphabet = random_alphabet+(random.choice(string.ascii_letters))
  for i in range(num_of_digit):
    random_digit = random_digit+(random.choice(string.digits))
  for i in range(special_characters):
    random_character = random_character+(random.choice('!@$%^&*?'))

  password=random_alphabet+random_digit+random_character

  password=list(password)
  random.shuffle(password)
  password=''.join(password)

  print(f'\nThe generated password: {password}')
else:
  print("The password should be minimum 8 characters long.")
