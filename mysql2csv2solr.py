#!/usr/bin/python3

import pymysql
import sys
import csv
import os

db = pymysql.connect("localhost","user_name","password","Databases" )
cur = db.cursor()
sql = "select ID,CONCAT(LastName,' ',FirstName) FROM Persons;"
cur.execute(sql)

rows = cur.fetchall()
fp = open('/tmp/file.csv', 'w')
myFile = csv.writer(fp)
myFile.writerow(['id','Full Name'])
myFile.writerows(rows)

fp.close()
db.close()
os.system("""curl -u user:password 'http://localhost:8983/solr/user_core/update/csv?commit=true' --data-binary @/tmp/file.csv -H 'Content-type:text/plain; charset=utf-8'""")
