// Copyright (C) 2017  Oscar Diaz Barriga

// This file is part of Comp-Process-STPatterns.

// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

var mqSatLayer = new ol.layer.Tile({
    source: new ol.source.MapQuest({
        layer: 'sat'
    }),
    name: 'MapQuest',
    visible: false
});

var mqCityLayer = new ol.layer.Tile({
    source: new ol.source.MapQuest({
        layer: 'osm'
    }),
    name: 'MapQuest',
    visible: true
});

var osmLayer = new ol.layer.Tile({
    source: new ol.source.OSM(),
    name: 'OpenStreetMap'
});

var SatLayer = new ol.layer.Tile({
    preload: Infinity,
    source: new ol.source.BingMaps({
        key: 'AsrsZXSBaB6PZKQ3UjgBI_q8gKZyukQgWGIdIJOMHu36KlPBaDfkckF_jCJ-rE69',
        imagerySet: 'Aerial',
        culture: 'es-es'
    }),
    visible: false
});


var CityLayer = new ol.layer.Tile({
    preload: Infinity,
    source: new ol.source.BingMaps({
        key: 'AsrsZXSBaB6PZKQ3UjgBI_q8gKZyukQgWGIdIJOMHu36KlPBaDfkckF_jCJ-rE69',
        imagerySet: 'Road',
        culture: 'es-es'
    }),
    visible: true
});


//var googleLayerSATELLITE = new olgm.layer.Google({
//    mapTypeId: google.maps.MapTypeId.SATELLITE,
//    visible: false
//  });
//
//var googleLayerTERRAIN = new olgm.layer.Google({
//    mapTypeId: google.maps.MapTypeId.TERRAIN,
//    visible: true
//  });


/******************************************************************************/
var styleFunctionPT = function (feature) {

    var style = new ol.style.Style();
    if (feature) {
        if ((feature.get("name") === "Oceanic Spreading Rift")
                || (feature.get("name") === "Oceanic Transform Fault")
                || (feature.get("name") === "Continental Transform Fault")
                || (feature.get("name") === "Continental Rift Boundary")
                || (feature.get("name") === "Subduction Zone")) {
            var style = new ol.style.Style({
                stroke: new ol.style.Stroke({
                    width: 3, color: [254, 86, 50, 0.8]
                })
            });
        }
        if ((feature.get("name") === "Oceanic Convergent Boundary")
                || (feature.get("name") === "Continental Convergent Boundary")) {
            var style = new ol.style.Style({
                stroke: new ol.style.Stroke({
                    width: 3, color: [160, 62, 223, 0.8]
                })
            });
        }
    }
    return style;
};

var routeplacastectonicas = new ol.style.Style({
    stroke: new ol.style.Stroke({
        width: 2, color: [251, 0, 0, 0.4]
    })
});

var vplacastectonicas = new ol.layer.Vector({
    source: new ol.source.Vector({
        url: 'data/kml/placastectonicas.kml',
        format: new ol.format.KML({
            extractStyles: false
        })
    }),
    style: styleFunctionPT,
    visible: false
});

/******************************************************************************/

var day1 = 100;
var day2 = 115;
var dcte = 1422766800; // 02/01/2015 @ 5:00am (UTC)

var year1 = -5000;
var year2 = 2016;
var minVEI = 1;
var maxVEI = 4;
var styleCache = {};
var styleFunction = function (feature) {
    // 2012_Earthquakes_Mag5.kml stores the magnitude of each earthquake in a
    // standards-violating <magnitude> tag in each Placemark.  We extract it from
    // the Placemark's name instead.
    var style = new ol.style.Style();
    if (feature) {

        var name = feature.get('name');
        var magnitude = feature.get('vei');
        var year = feature.get('year');
        var yearInt = parseInt(year);
        if ((year1 <= yearInt) && (yearInt < year2)) {
            if ((minVEI <= magnitude) && (magnitude <= maxVEI)) {
                var radius = Math.exp(magnitude / 3) * 5;
                style = styleCache[radius];
                if (!style) {
                    style = new ol.style.Style({
                        image: new ol.style.RegularShape({
                            points: 3,
                            radius: radius,
                            fill: new ol.style.Fill({
                                color: 'rgba(255, 204, 63, 0.7)'
                            }),
                            stroke: new ol.style.Stroke({
                                color: 'rgba(255, 140, 0, 0.7)',
                                width: 2
                            })
                        })
                    });
                    styleCache[radius] = style;
                }
            }
        }
    }
    return style;
};

var vvolcanes = new ol.layer.Vector({
    source: new ol.source.Vector({
        url: 'data/kml/volerup.kml',
        format: new ol.format.KML({
            extractStyles: false
        })
    }),
    style: styleFunction,
    visible: false
});
/******************************************************/

var minITsunami = 1;
var maxITsunami = 7;
var styleCache1 = {};
var styleFunctionTsunamis = function (feature) {
    var style = new ol.style.Style();
    if (feature) {

        var name = feature.get('location_name');
        var magnitude = 1;
        if (feature.get('primary_magnitude')) {
            magnitude = feature.get('primary_magnitude');
        }else {
            magnitude = feature.get('soloviev');
        }
        var max_water_h = 0;
        if (feature.get('maximum_water_height')) {
            max_water_h = feature.get('maximum_water_height');
        }

        var year = feature.get('year');
        var yearInt = parseFloat(year);
        if ((year1 <= yearInt) && (yearInt < year2)) {
            if ((minITsunami <= magnitude) && (magnitude <= maxITsunami)) {
                var radius = Math.exp((magnitude - 2) / 3) * 3;
                style = styleCache1[radius];
                if (!style) {
                    style = new ol.style.Style({
                        image: new ol.style.Circle({
                            radius: radius,
                            fill: new ol.style.Fill({
                                color: 'rgba(1, 255, 210,' + (max_water_h / 10 + 0.1) + ')'
                            }),
                            stroke: new ol.style.Stroke({
//                                color: 'rgba(0, 153, 255, 0.8)',
                                color: '#03a99e',
                                width: 2
                            })
                        })
                    });
                    styleCache1[radius] = style;
                }
            }
        }
    }
    return style;
};

var vptsunamis = new ol.layer.Vector({
    source: new ol.source.Vector({
        url: 'data/kml/tsevent.kml',
        format: new ol.format.KML({
            extractStyles: false
        })
    }),
    style: styleFunctionTsunamis,
    visible: false
});

/*******************************************************/
/* 1422748800 1464566400 */

var styleFunctionBoyas = function (feature) {
    var style = new ol.style.Style();
    if (feature) {

        var id = feature.get('name');
        var pres = feature.get('pres');
        var temp = feature.get('temp');
        var psal = feature.get('psal');

        var red = parseInt(id.substring(0, 2));
        var green = parseInt(id.substring(3, 5));
        var blue = parseInt(id.substring(5, 7));

        var ano = feature.get('ano');
        var mes = feature.get('mes');
        var dia = feature.get('dia');
        var uxtime = parseInt(Date.parse( mes + "/" + dia + "/" + ano)/1000);
//                console.log("--------");
//        console.log(mes + "/" + dia + "/" + ano);
//        console.log(uxtime);
//            console.log("--------");

        uxtime_ini = day1*3600*24 + dcte;
        uxtime_fin = day2*3600*24 + dcte;

        if ((uxtime_ini <= uxtime) && (uxtime < uxtime_fin)) {
//            console.log("true");
//            console.log(uxtime_ini);
//            console.log(uxtime_fin);
                var radius = 4;
                style = styleCache1[radius];
                if (!style) {
                    style = new ol.style.Style({
                        image: new ol.style.Circle({
                            radius: radius,
                            fill: new ol.style.Fill({
                                color: [red*3, green*5, blue*3, 0.85]
                            }),
                            stroke: new ol.style.Stroke({
                                color: [red*3, green*5, blue*3, 1],
                                width: 2
                            })
                        })
                    });
    //                    styleCache1[radius] = style;
                }
        }
    }
    return style;
};

var vboyas = new ol.layer.Vector({
    source: new ol.source.Vector({
        url: 'data/kml/tboyas.kml',
        format: new ol.format.KML({
            extractStyles: false
        })
    }),
    style: styleFunctionBoyas
});

/*******************************************************/

var color_stroke_departamentos = "red";
var color_fill_departamentos = "rgba(255, 0, 0, 0.2)";
var vescenario_nino = true;
var vescenario_1 = false;
var vescenario_2 = false;

var styleFunctionDepart = function (feature) {

    if (vescenario_1) {
        color_stroke_departamentos = '#FF8000';
        color_fill_departamentos = "rgba(247, 190, 129, 0.2)";
    }else if (vescenario_2){
        color_stroke_departamentos = '#D358F7';
        color_fill_departamentos = "rgba(217, 145, 239, 0.2)";
    }else if (vescenario_nino){
        color_stroke_departamentos = "red";
        color_fill_departamentos =  "rgba(255, 0, 0, 0.1)";
    }else {
        color_stroke_departamentos = "#58FA82";
        color_fill_departamentos =  "rgba(0, 255, 0, 0.1)";
    }

    var style = new ol.style.Style();

    if (feature) {
        if (((feature.get("NOMBDEP") === "TUMBES")
        || (feature.get("NOMBDEP") === "PIURA")
        || (feature.get("NOMBDEP") === "LAMBAYEQUE")
        || (feature.get("NOMBDEP") === "LA LIBERTAD"))
        && vescenario_nino
        ) {
              style = new ol.style.Style({
                            stroke: new ol.style.Stroke({
                color: color_stroke_departamentos,
                width: 2
              }),
              fill: new ol.style.Fill({
                color: color_fill_departamentos
              })
              });
         }
    else if (feature.get("NOMBDEP") === "ANCASH") {
        if (vescenario_1) {

            style = new ol.style.Style({
              stroke: new ol.style.Stroke({
                color: "#58FA82",
                width: 2
              }),
              fill: new ol.style.Fill({
                color: "rgba(0, 255, 0, 0.1)"
              })
         });

        } else if (vescenario_2){
            style = new ol.style.Style({
                            stroke: new ol.style.Stroke({
                color: color_stroke_departamentos,
                width: 2
              }),
              fill: new ol.style.Fill({
                color: color_fill_departamentos
              })
                 })
        } else if (vescenario_nino){
            style = new ol.style.Style({
                            stroke: new ol.style.Stroke({
                color: color_stroke_departamentos,
                width: 2
              }),
              fill: new ol.style.Fill({
                color: color_fill_departamentos
              })
                 })
        }
    }
    else {
        style = new ol.style.Style({
              stroke: new ol.style.Stroke({
                color: "#58FA82",
                width: 1
              }),
              fill: new ol.style.Fill({
                color: "rgba(0, 255, 0, 0.1)"
              })
         });
    }
    }
    return style;
    }

var vdepartamentos = new ol.layer.Vector({
    source: new ol.source.Vector({
        url: 'data/kml/peru-departamentos.kml',
        format: new ol.format.KML({
            extractStyles: false
        })
    }),
    style: styleFunctionDepart,
    visible: true
});

/*******************************************************/

var styleFunctionEstMet = function (feature) {
    var style = new ol.style.Style();
    if (feature) {

        var id = feature.get('id_estacion');
        var fecha_inicio = feature.get('fecha_inicio');
        var fecha_fin = feature.get('fecha_fin');

        var red = parseInt(id.substring(0, 2));
        var green = parseInt(id.substring(3, 5));
        var blue = parseInt(id.substring(5, 7));

        var ano1 = fecha_inicio.substr(0,4);
        var mes1 = fecha_inicio.substr(4,2);
        var dia1 = fecha_inicio.substr(6,2);

        var ano2 = fecha_fin.substr(0,4);
        var mes2 = fecha_fin.substr(4,2);
        var dia2 = fecha_fin.substr(6,2);

        var uxtime1 = parseInt(Date.parse( mes1 + "/" + dia1 + "/" + ano1)/1000);
        var uxtime2 = parseInt(Date.parse( mes2 + "/" + dia2 + "/" + ano2)/1000);
//                console.log("--------");
//        console.log(mes1 + "/" + dia1 + "/" + ano1);
//        console.log(uxtime1);
//            console.log("--------");

        uxtime_ini = day1*3600*24 + dcte;
        uxtime_fin = day2*3600*24 + dcte;

        rangovalido =  ( (uxtime1 <= uxtime_ini) && (uxtime2 > uxtime_ini) && (uxtime2 <= uxtime_fin) ) ||
            ( (uxtime2 > uxtime_fin) && (uxtime1 > uxtime_ini) && (uxtime1 <= uxtime_fin) ) ||
            ( (uxtime2 > uxtime_ini) && (uxtime2 <= uxtime_fin) && (uxtime1 > uxtime_ini) && (uxtime1 <= uxtime_fin) ) ||
            ( (uxtime2 > uxtime_fin) && (uxtime1 <= uxtime_ini) )

        var fill = new ol.style.Fill({color: '#FFFF00'});
        var stroke = new ol.style.Stroke({color: '#4B610B', width: 2});
        if (rangovalido) {
//            console.log("true");
//            console.log(uxtime_ini);
//            console.log(uxtime_fin);
                var radius = 6;
                style = styleCache1[radius];
                if (!style) {
                    style = new ol.style.Style({
                        image: new ol.style.RegularShape({
                        fill: fill,
                        stroke: stroke,
                        points: 3,
                        radius: radius,
                        rotation: Math.PI / 1.5,
                        angle: 0
                        })
                    });
                }
        }
    }
    return style;
};


var vestacion_metereologica = new ol.layer.Vector({
    source: new ol.source.Vector({
        url: 'data/kml/est-met.kml',
        format: new ol.format.KML({
            extractStyles: false
        })
    }),
    style: styleFunctionEstMet
});

