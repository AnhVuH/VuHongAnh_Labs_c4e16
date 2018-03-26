from random import *
from inside import is_inside


shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]

def get_shapes():
    return shapes

def generate_quiz():
    meaning = choice(get_shapes())['text']
    color = choice(get_shapes())['color']
    return [
                meaning,
                color,
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    shapes = get_shapes()
    for shape in shapes:
        if is_inside([x,y], shape['rect']):
            if quiz_type == 0:
                if text == shape['text']:
                    return True
                else:
                    return False
            else:
                if color == shape['color']:
                    return True
                else:
                    return False
