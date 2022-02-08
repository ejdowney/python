print('What\'s your name?')
userName = input()

print('What\'s your age?')
userAge = input()

if userName == 'Alice':
    print('Hi Alice')
elif int(userAge) < 12:
    print('You are not Alice! and you are too young!!!')
elif int(userAge) > 2000:
    print('Alice is much younger than you!')
