#!/usr/bin/python3

import pymysql
import sys
import csv
import os

db = pymysql.connect("localhost","username","password","database_name" )
cur = db.cursor()
sql = 'select * from Table_name;'
cur.execute(sql)

rows = cur.fetchall()
fp = open('/tmp/file.csv', 'w')
myFile = csv.writer(fp)
myFile.writerow(['ID','First_name','last_name','Age'])
myFile.writerows(rows)
fp.close()
db.close()
os.system("""curl 'http://localhost:8983/solr/core_name/update/csv?commit=true' --data-binary @path_of_the_file.csv -H 'Content-type:text/plain; charset=utf-8'""")
