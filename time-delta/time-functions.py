import datetime
import time
def datetimestrptime(date_string,frmt):
    t = datetime.datetime.strptime(date_string,frmt)
    return t
test = int(input())
for _ in range(0,test):
    t1 = input()
    t2 = input()
    frmt = '%a %d %b %Y %H:%M:%S %z'
    a = datetimestrptime(t1,frmt)
    b = datetimestrptime(t2,frmt)
    print(abs(int(datetime.timedelta.total_seconds(a - b))))
