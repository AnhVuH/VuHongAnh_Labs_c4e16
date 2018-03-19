from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

from collections import OrderedDict

mongo_uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

labels = ['events', 'ads', 'wom']

dict_values = OrderedDict()
for label in labels:
    dict_values[label] = 0

sum =0
for customer in db.customers.find():
    sum +=1
    if customer['ref'] in dict_values:
        dict_values[customer['ref']] += 1

for label in dict_values:
	print('The numbers of customer in group {}: {}'.format(label,dict_values[label]))
	dict_values[label] = (dict_values[label]/sum) *100


colors = ['red','green', 'blue']
explode1 =[]
for i in range(len(dict_values)):
    explode1.append(0.1)

pyplot.pie([v for v in dict_values.values()], labels= [k for k in dict_values.keys()],colors=colors, explode = explode1, autopct='%.2f%%', shadow =True)
pyplot.axis('equal')

pyplot.show()
