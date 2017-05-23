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

/**
 * Define a namespace for the application.
 */
window.app = {};
var app = window.app;


/**
 * @constructor
 * @extends {ol.control.Control}
 * @param {Object=} opt_options Control options.
 */
app.MenuControl = function (opt_options) {


    var options = opt_options || {};

    var anchor = document.createElement('a');
    anchor.href = '#rotate-north';
    anchor.className = 'glyphicon glyphicon-menu-hamburger';


    var this_ = this;
    var handleMenu = function (e) {
        // prevent #rotate-north anchor from getting appended to the url
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    };

    anchor.addEventListener('click', handleMenu, false);
    anchor.addEventListener('touchstart', handleMenu, false);

    var element = document.createElement('div');
    element.className = 'rotate-north ol-unselectable';
    element.appendChild(anchor);

    ol.control.Control.call(this, {
        element: element,
        target: options.target
    });
};

ol.inherits(app.MenuControl, ol.control.Control);



var coordinates = [[-80, -3.38], [-90, -3.38], [-90, -10], [-80, -10], [-80, -3.38]];
/*var geometry = new ol.geom.LineString(coordinates);
geometry.transform('EPSG:4326', 'EPSG:3857');

var layerLines = new ol.layer.Vector({
      source: new ol.source.Vector({
          features: [new ol.Feature({
              geometry: geometry,
              name: 'Line'
          })]
      }),
      style: new ol.style.Style({
          fill: new ol.style.Fill({
            color: 'rgba(0, 0, 255, 1)'
          }),
          stroke: new ol.style.Stroke({
            color: '#ff0c03',
            width: 2
          })
          }),
      visible: true
}); */

var feature_nino = new ol.Feature({
            geometry: new ol.geom.Polygon([coordinates])
        });

feature_nino.getGeometry().transform('EPSG:4326', 'EPSG:3857');

var layerLines = new ol.layer.Vector({
      source: new ol.source.Vector({
          features: [feature_nino]
      }),
      style: new ol.style.Style({
          fill: new ol.style.Fill({
            color: 'rgba(255, 0, 0, 0.1)'
          }),
          stroke: new ol.style.Stroke({
            color: 'red',
            width: 2
          })
          }),
      visible: true
});


var coord_escenario_1 = [[-80, -3.38], [-90, -3.38], [-90, -8.9722], [-80, -8.9722], [-80, -3.38]];
//geometry = new ol.geom.LineString(coord_escenario_1);
//geometry.transform('EPSG:4326', 'EPSG:3857');

var feature_1 = new ol.Feature({
            geometry: new ol.geom.Polygon([coord_escenario_1])
        });

feature_1.getGeometry().transform('EPSG:4326', 'EPSG:3857');

var layerLines_escenario_1 = new ol.layer.Vector({
      source: new ol.source.Vector({
          features: [feature_1]
      }),
      style: new ol.style.Style({
          fill: new ol.style.Fill({
            color: 'rgba(250, 172, 8, 0.1)'
          }),
          stroke: new ol.style.Stroke({
            color: '#FF8000',
            width: 2
          })
          }),
      visible: false
});

coord_escenario_2 = [[-80, -3.38], [-90, -3.38], [-90, -10.593], [-80, -10.593], [-80, -3.38]];
//geometry = new ol.geom.LineString(coord_escenario_1);
//geometry.transform('EPSG:4326', 'EPSG:3857');

feature_2 = new ol.Feature({
            geometry: new ol.geom.Polygon([coord_escenario_2])
        });

feature_2.getGeometry().transform('EPSG:4326', 'EPSG:3857');

var layerLines_escenario_2 = new ol.layer.Vector({
      source: new ol.source.Vector({
          features: [feature_2]
      }),
      style: new ol.style.Style({
          fill: new ol.style.Fill({
            color: 'rgba(217, 145, 239, 0.1)'
          }),
          stroke: new ol.style.Stroke({
            color: '#D358F7',
            width: 2
          })
          }),
      visible: false
});


coordinates = [[-80, -4.078], [-90, -4.078]];
geometry = new ol.geom.LineString(coordinates);
geometry.transform('EPSG:4326', 'EPSG:3857');

var layerLines_S1S2_1 = new ol.layer.Vector({
      source: new ol.source.Vector({
          features: [new ol.Feature({
              geometry: geometry,
              name: 'Line'
          })]
      }),
      style: new ol.style.Style({
          fill: new ol.style.Fill({
            color: 'rgba(0, 0, 255, 1)'
          }),
          stroke: new ol.style.Stroke({
            color: '#FF8000',
            width: 2,
            lineDash: [.1, 5]
          })
          }),
      visible: false
});

var layerLines_S1S2_2 = new ol.layer.Vector({
      source: new ol.source.Vector({
          features: [new ol.Feature({
              geometry: geometry,
              name: 'Line'
          })]
      }),
      style: new ol.style.Style({
          fill: new ol.style.Fill({
            color: 'rgba(0, 0, 255, 1)'
          }),
          stroke: new ol.style.Stroke({
            color: '#D358F7',
            width: 2,
            lineDash: [.1, 5]
          })
          }),
      visible: false
});

coordinates = [[-80, -6.382], [-90, -6.382]];
geometry = new ol.geom.LineString(coordinates);
geometry.transform('EPSG:4326', 'EPSG:3857');

var layerLines_S2S3_1 = new ol.layer.Vector({
      source: new ol.source.Vector({
          features: [new ol.Feature({
              geometry: geometry,
              name: 'Line'
          })]
      }),
      style: new ol.style.Style({
          fill: new ol.style.Fill({
            color: 'rgba(0, 0, 255, 1)'
          }),
          stroke: new ol.style.Stroke({
            color: '#FF8000',
            width: 2,
            lineDash: [.1, 5]
          })
          }),
      visible: false
});

var layerLines_S2S3_2 = new ol.layer.Vector({
      source: new ol.source.Vector({
          features: [new ol.Feature({
              geometry: geometry,
              name: 'Line'
          })]
      }),
      style: new ol.style.Style({
          fill: new ol.style.Fill({
            color: 'rgba(0, 0, 255, 1)'
          }),
          stroke: new ol.style.Stroke({
            color: '#D358F7',
            width: 2,
            lineDash: [.1, 5]
          })
          }),
      visible: false
});

coordinates = [[-80, -7.177], [-90, -7.177]];
geometry = new ol.geom.LineString(coordinates);
geometry.transform('EPSG:4326', 'EPSG:3857');

var layerLines_S3S4_1 = new ol.layer.Vector({
      source: new ol.source.Vector({
          features: [new ol.Feature({
              geometry: geometry,
              name: 'Line'
          })]
      }),
      style: new ol.style.Style({
          fill: new ol.style.Fill({
            color: 'rgba(0, 0, 255, 1)'
          }),
          stroke: new ol.style.Stroke({
            color: '#FF8000',
            width: 2,
            lineDash: [.1, 5]
          })
          }),
      visible: false
});

var layerLines_S3S4_2 = new ol.layer.Vector({
      source: new ol.source.Vector({
          features: [new ol.Feature({
              geometry: geometry,
              name: 'Line'
          })]
      }),
      style: new ol.style.Style({
          fill: new ol.style.Fill({
            color: 'rgba(0, 0, 255, 1)'
          }),
          stroke: new ol.style.Stroke({
            color: '#D358F7',
            width: 2,
            lineDash: [.1, 5]
          })
          }),
      visible: false
});

coordinates = [[-80, -8.9722], [-90, -8.9722]];
geometry = new ol.geom.LineString(coordinates);
geometry.transform('EPSG:4326', 'EPSG:3857');

var layerLines_S4S5_2 = new ol.layer.Vector({
      source: new ol.source.Vector({
          features: [new ol.Feature({
              geometry: geometry,
              name: 'Line'
          })]
      }),
      style: new ol.style.Style({
          fill: new ol.style.Fill({
            color: 'rgba(0, 0, 255, 1)'
          }),
          stroke: new ol.style.Stroke({
            color: '#D358F7',
            width: 2,
            lineDash: [.1, 5]
          })
          }),
      visible: false
});

var layers = [
    SatLayer,
    CityLayer,
    vdepartamentos,
    vestacion_metereologica,
    vplacastectonicas,
    vboyas,
    layerLines,
    layerLines_escenario_1,
    layerLines_S1S2_1,
    layerLines_S2S3_1,
    layerLines_S3S4_1,
    layerLines_escenario_2,
    layerLines_S1S2_2,
    layerLines_S2S3_2,
    layerLines_S3S4_2,
    layerLines_S4S5_2
];


function init_map() {
    map = null;
    map = new ol.Map({
//        interactions: olgm.interaction.defaults(),
        controls: ol.control.defaults().extend([
            new ol.control.ZoomSlider(),
            new ol.control.FullScreen(),
            new app.MenuControl()
        ]),
        layers: layers,
        target: 'map',
        view: new ol.View({
            center: [-9397148, -789099],
            zoom: 6.6
        })
    });
}
init_map();
/*var olGM = new olgm.OLGoogleMaps({map: map}); // map is the ol.Map instance
olGM.activate(); */

