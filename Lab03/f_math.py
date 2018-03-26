from random import randint, choice
from eval import calc
x = randint(1,10)
y = randint(1,10)

# result_t = x + y
#
# error = [-1, 0, 1]
#
# result = x + y + choice(error)
#
# print("{0} + {1}={2}".format(x,y,result))
# ans = input('(Y/N)?').lower()
#
# if ans == 'y':
#     if result ==result_t:
#         print('Yay')
#     else:
#         print('You are wrong')
# else:
#     if result ==result_t:
#         print('You are wrong')
#     else:
#         print('Yay')

# err = randint(-1,1)
err = choice([-1,0,0,1])    # tang xac suat cua ket qua dung
op = choice(['+','-','*','+','-','*','/'])

# if op =='+':
#     result = x + y
# elif op =='-':
#     result = x-y
# elif op =='*':
#     result = x * y
# elif op =='/':
#     result = x/y

result = calc(x,y,op)

result += err

print("{0} {1} {2}={3}".format(x,op, y,result))

ans = input('(Y/N)?').upper()

if err == 0:
    if ans =='Y':
        print('Yay')
    else:
        print("You're wrong")
else:
    if ans =='Y':
        print("You're wrong")
    else:
        print('Yay')
#
# if (err == 0 and ans == 'Y') or (err != 0 and ans == 'N'):
#     print('Yay')
# else:
#     print('You are wrong')
