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

# /* Tumbes */
# select count(*) from t_boya_medicion_minpres
# where latitud < -3.392 and latitud > -4.078
# /* Piura */
# select count(*) from t_boya_medicion_minpres
# where latitud < -4.078 and latitud > -6.382
# /* Lambayeque */
# select count(*) from t_boya_medicion_minpres
# where latitud < -6.382 and latitud > -7.177
# /* La Libertad */
# select count(*) from t_boya_medicion_minpres
# where latitud < -7.177 and latitud > -8.9722
# /* Ancash*/
# select count(*) from t_boya_medicion_minpres
# where latitud < -8.9722 and latitud > -10.593

import glob, os
import psycopg2
import datetime

db_user = "USER"
db_host = "IP_ADDRESS"
db_password = "PASSWORD"
output = "./Output/datos_total_boya3_est7_ca1.csv"

class Departamento (object):

    def __init__(self, nombre, latitud_min, latitud_max):
        self.nombre = nombre
        self.latitud_min = latitud_min
        self.latitud_max = latitud_max


class Zona (object):
    def __init__(self, start_date, end_date, nombre, latitud_min, latitud_max, temperatura, presion, salinidad):
        self.start_date = start_date
        self.end_date = end_date
        self.nombre = nombre
        self.latitud_min = latitud_min
        self.latitud_max = latitud_max
        self.temperatura = temperatura
        self.presion = presion
        self.salinidad = salinidad


class boya_data (object):
    def __init__(self, temperatura, presion, salinidad):
        self.temperatura = temperatura
        self.presion = presion
        self.salinidad = salinidad


class estacion_data (object):
#    def __init__(self, temperatura_m, punto_rocio_m, presion_nivel_mar):
#        self.est_temperatura_m = temperatura_m
#        self.est_punto_rocio_m= punto_rocio_m
#        self.est_presion_nivel_mar = presion_nivel_mar

    def __init__(self, temperatura_m, punto_rocio_m, presion_nivel_mar,
                 presion_est_media, velocidad_viento_media, temperatura_maxima,
                 temperatura_minima):
        self.est_temperatura_m = temperatura_m
        self.est_punto_rocio_m= punto_rocio_m
        self.est_presion_nivel_mar = presion_nivel_mar
        self.est_presion_est_media = presion_est_media
        self.est_temperatura_minima = temperatura_minima
        self.est_temperatura_maxima = temperatura_maxima
        self.est_velocidad_viento_media = velocidad_viento_media


class caudal_data (object):
    def __init__(self, caudal):
        self.caudal = caudal


def database_select_date_between(start_date, end_date):
    try:
        conn = psycopg2.connect("dbname='elnino' user='%s' host='%s' password='%s'"%(db_user, db_host, db_password))
    except Exception, e:
        print "I am unable to connect to the database " + e.pgerror

    cur = conn.cursor()
    try:
        query = "select count(*) from t_boya_medicion_minpres where latitud < -3.392 and latitud > -4.078 AND (" \
                " concat_ws('-',ano,mes,dia)::date  >= '%s'::date" \
                " AND" \
                " concat_ws('-',ano,mes,dia)::date <= '%s'::date);"%(start_date, end_date)
        # print query
        cur.execute(query)

    except Exception, e:
        print "I can't SELECT from bar " + e.pgerror
    rows = cur.fetchall()
    for row in rows:
        print "   ", row


def database_select_date_between_lat(start_latitud, end_latitud, start_date, end_date):
    try:
        conn = psycopg2.connect("dbname='elnino' user='%s' host='%s' password='%s'"%(db_user, host, password))
    except Exception, e:
        print "I am unable to connect to the database " + e.pgerror

    cur = conn.cursor()
    try:
        query = "select count(*) from t_boya_medicion_minpres where  latitud < %s AND latitud > %s AND  (" \
                " concat_ws('-',ano,mes,dia)::date  >= '%s'::date" \
                " AND" \
                " concat_ws('-',ano,mes,dia)::date <= '%s'::date);"%(start_latitud, end_latitud, start_date, end_date)
        # print query
        cur.execute(query)
    except Exception, e:
        print "I can't SELECT from bar " + e.pgerror
    rows = cur.fetchall()
    count = 0
    for row in rows:
        count = row[0]
    return count


def database_select_date_between_lat_avg(start_latitud, end_latitud, start_date, end_date):
    try:
        conn = psycopg2.connect("dbname='elnino' user='%s' host='%s' password='%s'"%(db_user, host, password))
    except Exception, e:
        print "I am unable to connect to the database " + e.pgerror

    cur = conn.cursor()
    try:
        query = "select avg(temp), avg(pres), avg(psal) from t_boya_medicion_minpres " \
                " where  latitud < %s AND latitud > %s AND  (" \
                " concat_ws('-',ano,mes,dia)::date  >= '%s'::date" \
                " AND" \
                " concat_ws('-',ano,mes,dia)::date <= '%s'::date);"%(start_latitud, end_latitud, start_date, end_date)
        # print query
        cur.execute(query)
    except Exception, e:
        print "I can't SELECT from bar " + e.pgerror
    rows = cur.fetchall()
    count = 0

    b_data = None
    for row in rows:
        b_data = boya_data(row[0], row[1], row[2])
    return b_data


def database_select_date_between_lat_avg_estacion(region, start_date, end_date):
    try:
        conn = psycopg2.connect("dbname='elnino' user='%s' host='%s' password='%s'"%(db_user, host. password))
    except Exception, e:
        print "I am unable to connect to the database " + e.pgerror

    cur = conn.cursor()
    try:
        query = "Select avg(em.temp_m), avg(em.punto_rocio_m), avg(em.presion_nivel_mar), " \
                "avg(em.presion_est_m), avg(em.veloc_viento_m), avg(em.temp_max), avg(em.temp_min) " \
                " From t_region r, t_estacion e, t_estacion_medicion em  " \
                " Where e.id_region = r.id_region AND r.nombre like '%s' " \
                " AND em.id_estacion = e.id_estacion " \
                " AND concat_ws('-',ano,mes,dia)::date  >= '%s'::date  " \
                " AND  concat_ws('-',ano,mes,dia)::date <= '%s'::date;"%(region, start_date, end_date)
        # print query
        cur.execute(query)
    except Exception, e:
        print "I can't SELECT from bar " + e.pgerror
    rows = cur.fetchall()
    count = 0

    b_data = None
    for row in rows:
        b_data = estacion_data(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    return b_data


def database_select_date_between_lat_avg_caudal(region, start_date, end_date):
    try:
        conn = psycopg2.connect("dbname='elnino' user='%s' host='%s' password='%s'"%(db_user, host, password))
    except Exception, e:
        print "I am unable to connect to the database " + e.pgerror

    cur = conn.cursor()
    try:
        query = " Select avg(c.caudal) From t_caudal_medicion c  " \
                " Where  c.region like '%s'  AND c.caudal != 9999 " \
                " AND concat_ws('-',ano,mes,dia)::date  >= '%s'::date " \
                " AND concat_ws('-',ano,mes,dia)::date <= '%s'::date;"%(region, start_date, end_date)
        # print query
        cur.execute(query)
    except Exception, e:
        print "I can't SELECT from bar " + e.pgerror
    rows = cur.fetchall()
    count = 0

    c_data = None
    for row in rows:
        c_data = caudal_data(row[0])
    return c_data
# def count_boyas_range_space_and_time(i, start_date_unix, step_date, latitude, longitude):
#     t_start = start_date_unix + i * step_date
#     t_end = start_date_unix + (i + 1) * step_date
#     start_date = datetime.datetime.fromtimestamp(t_start).strftime("%Y-%m-%d")
#     end_date = datetime.datetime.fromtimestamp(t_end).strftime("%Y-%m-%d")
#     count = database_select_date_between_lat(latitude, longitude, start_date, end_date)
#     print "%s -- %s -> %s" % (start_date, end_date, count)
#     return count


if __name__ == '__main__':
    # datebase = 1422766800

    maximo = 1467522000
    periodo = 18


    delta = 0
    toDate = 24*3600*periodo
    #n = 27
        #27
# 26, 16 = 8 8
# 26, 18 = 8 10
# 26, 20 = 10 10
# 24, 20 = 9 10
# 22, 22 = 12, 12 2015-03-18
# 20, 24 = 13, 11
# 14, 34 = 21, 13


    departamentos = []
    departamentos.append(Departamento("Tumbes", "-3.392", "-4.078"))
    departamentos.append(Departamento("Piura", "-4.078", "-6.382"))
    departamentos.append(Departamento("Lambayeque", "-6.382", "-7.177"))
    departamentos.append(Departamento("La Libertad", "-7.177", "-8.9722"))
    departamentos.append(Departamento("Ancash", "-8.9722", "-10.593"))

    rango_fechas = []
    rango_fechas_status = []

    start_date_unix = int(datetime.datetime.strptime("2015-03-05","%Y-%m-%d").strftime("%s"))

    n = (maximo - start_date_unix) / (24 * 3600 * periodo)
    print n
    print "2015-03-05 --- ",
    print datetime.datetime.fromtimestamp(maximo).strftime("%Y-%m-%d")

    for i in range(n):
        t_start = start_date_unix + i * toDate
        t_end = start_date_unix + (i + 1) * toDate
        start_date = datetime.datetime.fromtimestamp(t_start).strftime("%Y-%m-%d")
        end_date = datetime.datetime.fromtimestamp(t_end).strftime("%Y-%m-%d")
        rango_fechas.append([start_date, end_date, 1])
        print (start_date + " - " + end_date)


    for d in range(5):
        print "--------- %s -------------" % departamentos[d].nombre
        t_count = 0
        cero_count = 1
        count = 0
        i = 0
        for r in rango_fechas:
            start_date = r[0]
            end_date = r[1]
            count = database_select_date_between_lat(departamentos[d].latitud_min, departamentos[d].latitud_max, start_date, end_date)
            # print "%s -- %s -> %s" % (start_date, end_date, count)
            if count > 0:
                t_count = t_count + 1
                rango_fechas[i][2] = 1*rango_fechas[i][2]
            else:
                rango_fechas[i][2] = 0*rango_fechas[i][2]
            #     print "*%s -- %s -> %s" % (start_date, end_date, count)
            cero_count = cero_count*count
            i += 1
        print "Fallo %s ,"%(n - t_count),
        print "OK : %s"%t_count


    rango_fechas_ok = []
    for i in rango_fechas:
        if i[2] != 0:
            rango_fechas_ok.append([i[0],i[1]])

    print rango_fechas_ok
    with open(output, 'w') as the_file:
        the_file.write("region, boya_temp, boya_salinidad, est_temp, est_pto_rocio, est_presion, "
                       "est_presion_est_m, est_veloc_viento_m, est_temp_max, est_temp_min, caudal\n")
        for d in range(5):
            print "--------- %s -------------" % departamentos[d].nombre
            t_count = 0
            cero_count = 1
            count = 0
            for r in rango_fechas_ok:
                start_date = r[0]
                end_date = r[1]
                data_boya_avg = database_select_date_between_lat_avg(departamentos[d].latitud_min,
                                                                departamentos[d].latitud_max,
                                                                start_date, end_date)
                data_estacion_avg = database_select_date_between_lat_avg_estacion(departamentos[d].nombre, start_date, end_date)
                data_caudal_avg = database_select_date_between_lat_avg_caudal(departamentos[d].nombre, start_date, end_date)
                print "%s,  boya_temp :%s\tboya_sal :%s\t" \
                      "est_temp: %s\test_pto_rocio :%s\test_presion :%s\t" \
                      "est_presion_est_m :%s\test_veloc_viento_m :%s\test_temp_max :%s\test_temp_min :%s\t" \
                      "caudal:%s" % \
                      (departamentos[d].nombre, data_boya_avg.temperatura, data_boya_avg.salinidad,
                data_estacion_avg.est_temperatura_m, data_estacion_avg.est_punto_rocio_m,
                data_estacion_avg.est_presion_nivel_mar, data_estacion_avg.est_presion_est_media,
                data_estacion_avg.est_velocidad_viento_media, data_estacion_avg.est_temperatura_maxima, data_estacion_avg.est_temperatura_minima,
                data_caudal_avg.caudal)
                linea = "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s\n" % \
                (departamentos[d].nombre, data_boya_avg.temperatura, data_boya_avg.salinidad,
                data_estacion_avg.est_temperatura_m, data_estacion_avg.est_punto_rocio_m,
                data_estacion_avg.est_presion_nivel_mar, data_estacion_avg.est_presion_est_media,
                data_estacion_avg.est_velocidad_viento_media, data_estacion_avg.est_temperatura_maxima, data_estacion_avg.est_temperatura_minima,
                data_caudal_avg.caudal)
                the_file.write(linea)

