#!/usr/bin/python3

import pymysql
import sys
import csv
import os

db = pymysql.connect("localhost","admin","123456","aftab" )
cur = db.cursor()
sql = 'select * from EMPLOYEE;'
cur.execute(sql)

rows = cur.fetchall()
fp = open('/tmp/file.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()
db.close()
os.system("""curl 'http://localhost:8983/solr/user_core/update/csv?commit=true' --data-binary @/tmp/file.csv -H 'Content-type:text/plain; charset=utf-8'""")




