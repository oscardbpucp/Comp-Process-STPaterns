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

# import re
# import sys
# import numpy as np
# import time
import glob, os
import psycopg2

inputdir = "./Mar/DataSelection_20160804_050058_3472903/"
db_user = "USER"
db_host = "IP_ADDRESS"
db_password = "PASSWORD"
outputfile = "./Nino12f.txt"

platform = "PLATFORM"
argos_id = "ARGOS_ID"
date = "DATE (YYYY-MM-DDTHH:MI:SSZ)"
latitude = "LATITUDE (degree_north)"
longitude = "LONGITUDE (degree_east)"
pres = "PRES (decibar)"
temp = "TEMP (degree_Celsius)"
psal = "PSAL (psu)"
qc="QC"
dox2 = "DOX2 (micromole/kg)"


# Update t_estacionn set id_region = t_estacion.id_region FROM t_estacion WHERE t_estacionn.id_estacion = t_estacion.id_estacion;

def database_init():
    try:
        conn = psycopg2.connect("dbname='elnino' user='%s' host='%s' password='%s'"%(db_user, db_host, db_password))
    except:
        print "I am unable to connect to the database"

    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE IF EXISTS t_boya_medicion")
        cur.execute(
            "CREATE TABLE t_boya_medicion (Id serial primary key, boya integer, ano integer, mes integer, dia integer,"
            " latitud double precision, longitud double precision,"
            " pres double precision, temp double precision,"
            " psal double precision,"
            " qc integer,"
            " ok integer)")
        conn.commit()
    except Exception, e:
        print "I can't SELECT from bar" + e.pgerror


def database_data(data):
    try:
        conn = psycopg2.connect("dbname='elnino' user='%s' host='%s' password='%s'"%(db_user, db_host, db_password))
    except:
        print "I am unable to connect to the database"

    cur = conn.cursor()
    try:
        query = "INSERT INTO t_boya_medicion (boya, ano, mes, dia, latitud, longitud, pres, temp, psal, qc, ok) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.executemany(query, data)
        conn.commit()
    except Exception, e:
        print "I can't SELECT from bar" + e.pgerror


def database_alter_table(table_name):
    try:
        conn = psycopg2.connect("dbname='elnino' user='%s' host='%s' password='%s'"%(db_user, db_host, db_password))
    except:
        print "I am unable to connect to the database"

    cur = conn.cursor()
    try:
        query = "ALTER TABLE %s ADD COLUMN the_geom geometry ( POINT, 4326 );" % table_name
        cur.execute(query)
        conn.commit()
    except Exception, e:
        print "I can't SELECT from bar" + e.pgerror


def database_transform_table(table_name):
    try:
        conn = psycopg2.connect("dbname='elnino' user='%s' host='%s' password='%s'"%(db_user, db_host, db_password))
    except:
        print "I am unable to connect to the database"

    cur = conn.cursor()
    try:
        query = "UPDATE %s SET the_geom = ST_SetSRID (ST_MakePoint(\"longitud\",\"latitud\"), 4326);" % table_name
        cur.execute(query)
        conn.commit()
    except Exception, e:
        print "I can't SELECT from bar" + e.pgerror


def search_n(header, find_head):
    header_list = header.split(",")
    n = 0
    for head in header_list:
        n = n + 1
        if head == find_head:
            break
    if len(header_list) == n:
        n = -1
    return n


def extract(line, index):
    return line.split(",")[index-1]


def extract_data(line, header, find_head) :
    value = extract(line, search_n(header, find_head))
    if len(value) == 0:
        value = "9999"
    return value


def struct_line(line, header):
    datos = {}
    datos['platform'] = extract_data(line, header, platform)
    datos['argos_id'] = extract_data(line, header, argos_id)
    datos['date'] = extract_data(line, header, date)
    datos['latitude'] = extract_data(line, header, latitude)
    datos['longitude'] = extract_data(line, header, longitude)
    datos['pres'] = extract_data(line, header, pres)
    datos['temp'] = extract_data(line, header, temp)
    datos['psal'] = extract_data(line, header, psal)
    datos['qc'] = extract_data(line, header, qc)
    if (len(datos['qc']) > 0) and not(datos['qc'].find("9") >= 0):
        datos['ok'] = 1
    else:
        datos['ok'] = 0
    datos['dox2'] = extract_data(line, header, dox2)
    return datos


def extract_date(date):
    fecha = date.split("T")[0]
    dfecha = fecha.split("-")
    return "%s%s%s" % (dfecha[0], dfecha[1], dfecha[2])

# 2015-11-22T23:41:00Z

# CREATE EXTENSION postgis;
# CREATE EXTENSION postgis_sfcgal;
# CREATE EXTENSION fuzzystrmatch; --needed for postgis_tiger_geocoder
# --optional used by postgis_tiger_geocoder, or can be used standalone
# CREATE EXTENSION address_standardizer;
# CREATE EXTENSION address_standardizer_data_us;
# CREATE EXTENSION postgis_tiger_geocoder;
# CREATE EXTENSION postgis_topology;




# CREATE table t_boya_medicion_minpres
#  AS
# Select b.*  from t_boya_medicion  b
# Inner Join (
# Select boya, ano, mes, dia, Min(pres) presion
# FROM t_boya_medicion where ok = 1
# Group by boya, ano, mes, dia
# ) x on x.boya = b.boya
# and x.ano = b.ano
# and x.mes = b.mes
# and x.dia = b.dia
# and x.presion = b.pres
# Order By b.ano, b.mes, b.dia
# ;


if __name__ == '__main__':
    database_init()
    os.chdir(inputdir)
    for archivo in sorted(glob.glob("*")):
        filename = inputdir + archivo
        with open(filename) as f:
            header = f.readline()
            i = 0
            data_boya = []
            for line in f.readlines():
                data_day = []
                i = i + 1
                if i > 0:
                    #print filename + " - " + str(extract(line, search_n(content, platform)))
                    #print filename + " - " + struct_line(line, header)['temp']
                    # print "INSERT INTO boya_data  VALUES  (%s, %s, %s, %s, %s, %s, %s)"%(
                    #     struct_line(line, header)['platform'],
                    #     extract_date(struct_line(line, header)['date']),
                    #     struct_line(line, header)['latitude'],
                    #     struct_line(line, header)['longitude'],
                    #     struct_line(line, header)['pres'],
                    #     struct_line(line, header)['temp'],
                    #     struct_line(line, header)['psal'])
                    data_day.append(int(struct_line(line, header)['platform']))
                    data_day.append(int(extract_date(struct_line(line, header)['date'])[0:4]))
                    data_day.append(int(extract_date(struct_line(line, header)['date'])[4:6]))
                    data_day.append(int(extract_date(struct_line(line, header)['date'])[6:8]))
                    data_day.append(float(struct_line(line, header)['latitude']))
                    data_day.append(float(struct_line(line, header)['longitude']))
                    data_day.append(float(struct_line(line, header)['pres']))
                    data_day.append(float(struct_line(line, header)['temp']))
                    data_day.append(float(struct_line(line, header)['psal']))
                    data_day.append(float(struct_line(line, header)['qc']))
                    data_day.append(float(struct_line(line, header)['ok']))
                    data_boya.append(tuple(data_day))
            database_data (tuple(data_boya))



        #     print str(len(content.split(","))) + " - " + str(search_n(content, argos_id))
        # for line in f.readlines():
        #     content = line
        #     # print str(len(content.split(","))) + " - " + str(search_n(content, dox2))
        # #print str(len(content.split(","))) + " - " + str(search_n(content, dox2))
        # print "%s - %s"%(filename, content)
    database_alter_table("t_boya_medicion")
    database_transform_table("t_boya_medicion")





