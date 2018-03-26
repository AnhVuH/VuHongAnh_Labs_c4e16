
def is_inside(point =[],rect =[]):
    if rect[0] <= point[0] <= rect[0] + rect[2] \
    and rect[1] <= point[1] <= rect[1] + rect[3]:
        return True
    else:
        return False

point_is_inside = is_inside([200, 120], [140, 60, 100, 200])

if point_is_inside :
    print("Your function is corret")
else:
    print("Oops, there's a bug")