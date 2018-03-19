import datetime

now = datetime.datetime.now()
print("Current hour:{} h".format(now.hour))
print("Current hour:", now.strftime('%I %p'))
