from random import randint, choice
# x = 3
# y = 7
# op = choice(['+','-','*','/'])
#
# result =-999999
#
# if op =='+':
#     result = x + y
# elif op =='-':
#     result = x - y
# elif op =='*':
#     result = x * y
# elif op =='/':
#     result = x / y
#
# print(result)

def calc(x,y, op):
    if op =='+':
        result = x + y
    elif op =='-':
        result = x - y
    elif op =='*':
        result = x * y
    elif op =='/':
        result = x / y

    return result

# argument, parameter
#
res = calc(3,7,'+')
print(res)
#
# r = calc(1,2,'-')
# print(r)
