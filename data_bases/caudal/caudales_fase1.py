# -*- coding: utf-8 -*-

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

import glob, os
import psycopg2

inputdir = "/Users/oscardiazbarriga/Documents/Maestria/Tesis/Caudal/"

db_user = "USER"
db_host = "IP_ADDRESS"
db_password = "PASSWORD"


depart = "Departamento"
date = "Fecha"
cuenca = "Cuenca"
hidroelect = "Hidroelectrica"
caudal = "Caudal"
anomalia_h = "Anomalia_Hidrica"


_connect = "dbname='elnino' user='%s' host='%s' password='%s'"%(db_user, db_host, db_password)

def database_init():
    try:
        conn = psycopg2.connect(_connect)
    except:
        print "I am unable to connect to the database"

    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE IF EXISTS t_caudal_medicion")
        cur.execute(
            "CREATE TABLE t_caudal_medicion (id_caudal serial primary key, "
            " ano integer, mes integer, dia integer,"
            " region text, cuenca text, hidroelectrica text, "
            " caudal double precision, anomalia_hidrica double precision )")
        conn.commit()
    except Exception, e:
        print "I can't SELECT from bar" + e.pgerror


def database_data(data):
    try:
        conn = psycopg2.connect(_connect)
    except:
        print "I am unable to connect to the database"

    cur = conn.cursor()
    try:
        query = "INSERT INTO t_caudal_medicion ( " \
                " ano, mes, dia, " \
                " region, cuenca, hidroelectrica, " \
                " caudal, anomalia_hidrica ) " \
                " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cur.executemany(query, data)
        conn.commit()
    except Exception, e:
        print "I can't SELECT from bar" + e.pgerror


def search_n(header, find_head):
    header_list = header.split(",")
    n = 0
    for head in header_list:
        n = n + 1
        if head.strip() == find_head:
            break
    if len(header_list) == n:
        n = -1
    # print "%s -> %s"%(find_head, n)
    return n


def extract(line, index):
    return line.split(",")[index-1].strip()


def extract_data(line, header, find_head) :
    value = extract(line, search_n(header, find_head))
    if len(value) == 0:
        value = "9999"
    return value


def struct_line(line, header):
    datos = {}
    datos['depart'] = extract_data(line, header, depart)
    datos['date'] = extract_data(line, header, date)
    datos['cuenca'] = extract_data(line, header, cuenca)
    datos['hidroelect'] = extract_data(line, header, hidroelect)
    datos['caudal'] = extract_data(line, header, caudal)
    datos['anomalia_h'] = extract_data(line, header, anomalia_h)
    return datos


def extract_date(date):
    fecha = date.split("T")[0]
    dfecha = fecha.split("-")
    return "%s%s%s" % (dfecha[0], dfecha[1], dfecha[2])

depart = "Departamento"
date = "Fecha"
cuenca = "Cuenca"
hidroelect = "Hidroelectrica"
caudal = "Caudal"
anomalia_h = "Anomalia_Hidrica"

if __name__ == '__main__':
    database_init()
    os.chdir(inputdir)
    for archivo in sorted(glob.glob("*")):
        filename = inputdir + archivo
        with open(filename) as f:
            header = f.readline()
            # print header
            i = 0
            data_caudal = []
            for line in f.readlines():
                data_day = []
                i += 1
                if i > 0:
                    data_day.append(int(struct_line(line, header)['date'][0:4]))
                    data_day.append(int(struct_line(line, header)['date'][4:6]))
                    data_day.append(int(struct_line(line, header)['date'][6:8]))
                    data_day.append(struct_line(line, header)['depart'])
                    data_day.append(struct_line(line, header)['cuenca'])
                    data_day.append(struct_line(line, header)['hidroelect'])
                    if struct_line(line, header)['caudal'] == "-":
                        tmp = 9999
                    else:
                        tmp = struct_line(line, header)['caudal']
                    data_day.append(tmp)
                    if struct_line(line, header)['anomalia_h'] == "-":
                        tmp = 9999
                    else:
                        tmp = struct_line(line, header)['anomalia_h']
                    data_day.append(tmp)
                    data_caudal.append(tuple(data_day))
            database_data(tuple(data_caudal))



        #     print str(len(content.split(","))) + " - " + str(search_n(content, argos_id))
        # for line in f.readlines():
        #     content = line
        #     # print str(len(content.split(","))) + " - " + str(search_n(content, dox2))
        # #print str(len(content.split(","))) + " - " + str(search_n(content, dox2))
        # print "%s - %s"%(filename, content)





