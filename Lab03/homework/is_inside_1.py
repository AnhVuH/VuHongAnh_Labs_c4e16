def is_inside(*args):
    if args[1][0] <= args[0][0] <= args[1][0] + args[1][2] \
    and args[1][1] <= args[0][1] <= args[1][1] + args[1][3]:
        return True
    else:
        return False


point_is_inside = is_inside([100, 120], [140, 60, 100, 200])

if not point_is_inside :
    print("Your function is corret")
else:
    print("Oops, there's a bug")