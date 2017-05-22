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

i = 0
#region, boya_temp, boya_salinidad, est_temp, est_pto_rocio, est_presion, caudal
cad = ""
for row in in_data:
    boya_temp = str(row[0]).replace(" ", "").replace("≥",">=").replace("-", ":")
    boya_salinidad = str(row[1]).replace(" ", "").replace("≥",">=").replace("-", ":")
    estac_temp = str(row[2]).replace(" ", "").replace("≥",">=").replace("-", ":")
    estac_pto_rocio = str(row[3]).replace(" ", "").replace("≥",">=").replace("-", ":")
    est_presion = str(row[4]).replace(" ", "").replace("≥",">=").replace("-", ":")
    caudal = str(row[5]).replace(" ", "").replace("≥",">=").replace("-", ":")
    tmp = "boya-temp_%s boya-salinidad_%s estac-temp_%s estac-pto-rocio_%s est_presion_%s caudal_%s"%(boya_temp, boya_salinidad ,estac_temp ,estac_pto_rocio ,est_presion ,caudal)
   
    if i <= 13:
        cad = cad + " -1 " + tmp
        i = i + 1 
    else:
        cad = cad + " -1 -2\n" + tmp
        i = 1
        
print(cad)
 #array_data = row.split(",")[0]
out_data =  in_data