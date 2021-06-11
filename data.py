from datetime import datetime, timedelta

#data = datetime(2020, 7, 11, 18, 56, 45)
#print(data.strftime('%d/%m/%Y %H:%M:%S'))

# data = datetime.strptime('11/07/2020', '%d/%m/%Y')
# print(data.timestamp())
# data = datetime.fromtimestamp(1594436400.0)
# print(data)

"""
data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(days=5, seconds=52)
print(data.strftime('%d/%m/%Y %H:%M:%S'))
"""

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 20:33:00', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(dif)
print(d1.time())