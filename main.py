a = 'emmanuel'
b = '1234'
f = 'marach'
e = 'John'

c = input('Enter your username: ')
print()
d = input('Enter your password: ')
print()
if c == a and d == b:
  print(f'\033[32mDear {a}, You logged in sucessfully!\033[0m')
elif c == e and d == b:
  print(f'\033[32mDear {e}, You logged in sucessfully!\033[0m') 
elif c == f and d == b:
  print(f'\033[32mDear {f}, You logged in sucessfully!\033[0m')
else:
  print('\033[31mInvalid details\033[0m')