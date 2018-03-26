x= float(input('x = '))
op = input('Operations(+,-,*,/): ')
y= float(input('y = '))

# if op =='+':
#     print(x, op, y ,'=', x+y)
# elif op =='-':
#     print(x, op, y ,'=', x-y)
# elif op =='*':
#     print(x, op, y ,'=', x*y)
# elif op =='/':
#     print(x, op, y ,'=', x/y)
result = -9999999

if op =='+':
    # print("{0} {1} {2}= {3}".format(x, op, y, x+y))
    result = x + y
elif op =='-':
    # print("{0} {1} {2}= {3}".format(x, op, y, x-y))
    result = x-y
elif op =='*':
    # print("{0} {1} {2}= {3}".format(x, op, y, x*y))
    result = x * y
elif op =='/':
    # print("{0} {1} {2}= {3}".format(x, op, y, x/y))
    result = x/y
print("*"* 20)
print("{0} {1} {2}= {3}".format(x, op, y, result))
