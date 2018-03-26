from random import *
from f_math import calc
def generate_quiz():
    # Hint: Return [x, y, op, result]
    err = choice([-1,0,0,1])
    ops = ['+','-','*','/','+','-','*']
    op = choice(ops)
    x = randint(0,10)
    if op =='/':
        y = randint(1,10)
    else:
        y = randint(0,10)
    result = calc(x,y,op) + err
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    if user_choice == True:
        if result == calc(x,y,op):
            return True
        else:
            return False
    else:
        if result == calc(x,y,op):
            return False
        else:
            return True
