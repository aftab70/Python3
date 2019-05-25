#!/usr/bin/python3

import datetime

ST = datetime.datetime.now() - datetime.timedelta(minutes = 15) 
ET = datetime.datetime.now()

print("Start time is ")
print(ST.strftime('%Y-%m-%d %H:%M:%S'))
print("end time is ")
print(ET.strftime('%Y-%m-%d %H:%M:%S'))
