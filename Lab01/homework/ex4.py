from pymongo import MongoClient
import matplotlib

matplotlib.use("TkAgg")

from matplotlib import pyplot

mongo_uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

labels = ['events', 'advertisements', 'word of mouth']

values =[0,0,0]
sum =0
for customer in db.customers.find():
	sum +=1
	if customer['ref'] == 'events':
		values[0] +=1
	elif customer ['ref'] =='ads':
		values[1] +=1
	elif customer ['ref'] == 'wom':
		values[2] +=1


for i in range(len(values)):
	print('The numbers of customer in group {}: {}'.format(labels[i],values[i]))
	values[i] = (values[i]/sum) *100

colors = ['red','green', 'blue']
explode = [0, 0.2, 0]

pyplot.pie(values, labels= labels, colors=colors, explode = explode,autopct='%.2f%%', shadow =True)
pyplot.axis('equal')

pyplot.show()
