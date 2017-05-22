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

inputdir = "./Datos-MinEdicion/"

db_user = "USER"
db_host = "IP_ADDRESS"
db_password = "PASSWORD"

# La temperatura media (0,1 grados Fahrenheit)
# La media del punto de rocío (0,1 grados Fahrenheit)
# La media de la presión a nivel del mar (.1 mb)
# presión de la estación media (.1 mb)
# visibilidad media (.1 millas)
# Velocidad del viento media (.1 nudos)
# La velocidad máxima sostenida del viento (nudos .1)
# ráfaga de viento máxima (.1 nudos)
# La temperatura máxima (0,1 Fahrenheit)
# La temperatura mínima (0,1 grados Fahrenheit)
# cantidad de precipitación (.01 pulgadas)
# Espesor de la nieve (.1 pulgadas)
# Indicador de la presencia de: Niebla
#                                Lluvia o llovizna
#                                Los pellets de hielo o nieve
#                                Granizo
#                                Trueno
#                                Tornado / nubes de embudo

estacion = "STN---"
wban = "WBAN"
date = "YEARMODA"
temp = "TEMP"
temp_ = "TEMP+"
dewp = "DEWP"
dewp_ = "DEWP+"
slp = "SLP"
slp_ = "SLP+"
stp = "STP"
stp_ = "STP+"
visib = "VISIB"
visib_ = "VISIB+"
wdsp = "WDSP"
wdsp_ = "WDSP+"
mxspd = "MXSPD"
gust = "GUST"
max = "MAX"
min = "MIN"
pcrp = "PRCP"
sndp = "SNDP"
frshtt = "FRSHTT"



# Update t_estacionn set id_region = t_estacion.id_region FROM t_estacion WHERE t_estacionn.id_estacion = t_estacion.id_estacion;

def database_init():
    try:
        conn = psycopg2.connect("dbname='elnino' user='%s' host='%s' password='%s'"%(db_user, db_host, db_password))
    except:
        print "I am unable to connect to the database"

    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE IF EXISTS t_estacion_medicion")
        cur.execute(
            "CREATE TABLE t_estacion_medicion (Id serial primary key, id_estacion integer, wban integer, "
            " ano integer, mes integer, dia integer,"
            " temp_m double precision, temp_m_ double precision, "
            " punto_rocio_m double precision, punto_rocio_m_ double precision, "
            " presion_nivel_mar double precision, presion_nivel_mar_ double precision, "
            " presion_est_m double precision, presion_est_m_ double precision, "
            " visibilidad_m double precision, visibilidad_m_ double precision, "
            " veloc_viento_m double precision, veloc_viento_m_ double precision, "
            " veloc_max_sost_viento double precision, "
            " rafag_viento_max double precision, "
            " temp_max double precision, "
            " temp_min double precision, "
            " cant_precipitacion double precision, "
            " espesor_nieve double precision, "
            " indicador_ocurrencia integer )")
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
        query = "INSERT INTO t_estacion_medicion (id_estacion,  wban, " \
                " ano, mes, dia, " \
                " temp_m, temp_m_, " \
                " punto_rocio_m, punto_rocio_m_, " \
                " presion_nivel_mar, presion_nivel_mar_, " \
                " presion_est_m, presion_est_m_, " \
                " visibilidad_m, visibilidad_m_, " \
                " veloc_viento_m, veloc_viento_m_, " \
                " veloc_max_sost_viento, " \
                " rafag_viento_max, " \
                " temp_max, " \
                " temp_min, " \
                " cant_precipitacion, " \
                " espesor_nieve, " \
                " indicador_ocurrencia ) " \
                " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
    datos['estacion'] = extract_data(line, header, estacion)
    datos['wban'] = extract_data(line, header, wban)
    datos['date'] = extract_data(line, header, date)
    datos['temp'] = extract_data(line, header, temp)
    datos['temp_'] = extract_data(line, header, temp_)
    datos['dewp'] = extract_data(line, header, dewp)
    datos['dewp_'] = extract_data(line, header, dewp_)
    datos['slp'] = extract_data(line, header, slp)
    datos['slp_'] = extract_data(line, header, slp_)
    datos['stp'] = extract_data(line, header, stp)
    datos['stp_'] = extract_data(line, header, stp_)
    datos['visib'] = extract_data(line, header, visib)
    datos['visib_'] = extract_data(line, header, visib_)
    datos['wdsp'] = extract_data(line, header, wdsp)
    datos['wdsp_'] = extract_data(line, header, wdsp_)
    datos['mxspd'] = extract_data(line, header, mxspd)
    datos['gust'] = extract_data(line, header, gust)
    datos['max'] = extract_data(line, header, max)
    datos['min'] = extract_data(line, header, min)
    datos['pcrp'] = extract_data(line, header, pcrp)
    datos['sndp'] = extract_data(line, header, sndp)
    datos['frshtt'] = extract_data(line, header, frshtt)
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
            # print header
            i = 0
            data_estacion = []
            for line in f.readlines():
                data_day = []
                i = i + 1
                if i > 0:
                    data_day.append(int(struct_line(line, header)['estacion']))
                    data_day.append(int(struct_line(line, header)['wban']))
                    data_day.append(int(struct_line(line, header)['date'][0:4]))
                    data_day.append(int(struct_line(line, header)['date'][4:6]))
                    data_day.append(int(struct_line(line, header)['date'][6:8]))
                    data_day.append(float(struct_line(line, header)['temp']))
                    data_day.append(float(struct_line(line, header)['temp_']))
                    data_day.append(float(struct_line(line, header)['dewp']))
                    data_day.append(float(struct_line(line, header)['dewp_']))
                    data_day.append(float(struct_line(line, header)['slp']))
                    data_day.append(float(struct_line(line, header)['slp_']))
                    data_day.append(float(struct_line(line, header)['stp']))
                    data_day.append(float(struct_line(line, header)['stp_']))
                    data_day.append(float(struct_line(line, header)['visib']))
                    data_day.append(float(struct_line(line, header)['visib_']))
                    data_day.append(float(struct_line(line, header)['wdsp']))
                    data_day.append(float(struct_line(line, header)['wdsp_']))
                    data_day.append(float(struct_line(line, header)['mxspd']))
                    data_day.append(float(struct_line(line, header)['gust']))
                    data_day.append(float(struct_line(line, header)['max']))
                    data_day.append(float(struct_line(line, header)['min']))
                    tempp = struct_line(line, header)['pcrp']
                    data_day.append(float(tempp[:len(tempp) - 1]))
                    data_day.append(float(struct_line(line, header)['sndp']))
                    data_day.append(float(struct_line(line, header)['frshtt']))
                    data_estacion.append(tuple(data_day))
            database_data(tuple(data_estacion))



        #     print str(len(content.split(","))) + " - " + str(search_n(content, argos_id))
        # for line in f.readlines():
        #     content = line
        #     # print str(len(content.split(","))) + " - " + str(search_n(content, dox2))
        # #print str(len(content.split(","))) + " - " + str(search_n(content, dox2))
        # print "%s - %s"%(filename, content)





