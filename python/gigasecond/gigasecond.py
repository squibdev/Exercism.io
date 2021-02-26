from datetime import datetime

def add(moment):
    moment = int(moment) + 10**9
    return moment

print(add(datetime(2011, 4, 25, 0, 0)))