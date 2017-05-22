## Copyright (C) 2017  Oscar Diaz Barriga

## This file is part of Comp-Process-STPatterns.

## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

import psycopg2
import pprint

db_user = "USER"
db_host = "IP_ADDRESS"
db_password = "PASSWORD"

try:
    conn = psycopg2.connect("dbname='elnino' user='%s' host='%s' password='%s'"%(db_user, db_host, db_password))
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
try:
    cur.execute("DROP TABLE IF EXISTS t_boya_medicion")
    cur.execute("CREATE TABLE t_boya_medicion (Id INT PRIMARY KEY, latitud double precision, longitud double precision,"
                " fecha integer, pres integer, temp double precision, psal double precision)")
    query = "INSERT INTO Cars (Id, latitud, longitud, fecha, pres, temp, psal) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cur.executemany(query, cars)
    conn.commit()
except Exception, e:
    print "I can't SELECT from bar" + e.pgerror

# rows = cur.fetchall()
# print "\nRows: \n"
# for row in rows:
#     print "   ", row[1]

#pprint.pprint(rows)
