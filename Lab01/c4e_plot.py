import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot

#1. Prepare data
labels1 = ['Web', 'iOs', 'Android', 'React Native']
values1 = [40,20,25,15]
colors1 = ['red', 'green', 'gold', 'purple']
explode1 = [0, 0.2, 0, 0]


#2. Plot
pyplot.pie(values1, labels=labels1, colors= colors1, explode =explode1, shadow = True)
pyplot.axis('equal')



#3. Show
pyplot.show()
