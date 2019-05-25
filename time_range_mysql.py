#!/usr/bin/python3

import pymysql
import sys
import csv
import os
import datetime


db = pymysql.connect("localhost","user","password","databases" )
cur = db.cursor()

ST = datetime.datetime.now() - datetime.timedelta(minutes = 15) 
L15M = "'" + (ST.strftime('%Y-%m-%d %H:%M:%S')) + "'"

sql = "select ID,CONCAT(field_name,' ',field_name) from table_name where ADD_DATE_TIME > "+L15M+";"

cur.execute(sql)

rows = cur.fetchall()
fp = open('/tmp/file.csv', 'w')
myFile = csv.writer(fp)
myFile.writerow(['id','Full Name'])
myFile.writerows(rows)

fp.close()
db.close()
os.system("""curl -u admin:123456 'http://localhost:8983/solr/user_core/update/csv?commit=true' --data-binary @/tmp/file.csv -H 'Content-type:text/plain; charset=utf-8'""")
