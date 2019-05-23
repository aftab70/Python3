#!/usr/bin/python3

import pymysql
import sys
import csv

db = pymysql.connect("localhost","user","password","Database_name" )
cur = db.cursor()
sql = 'select * from table_name;'
cur.execute(sql)

rows = cur.fetchall()
fp = open('/tmp/file.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()
db.close()

import os
cmd = "'curl 'http://localhost:8983/solr/user_core/update/csv?commit=true' --data-binary @file.csv -H 'Content-type:text/plain; charset=utf-8'"
os.system(cmd)


