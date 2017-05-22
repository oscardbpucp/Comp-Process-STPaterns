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


function convert_3(cad) {

    var arr = cad.split(",");

    var space = 100;
    var sp = new Array();

    var x_tmp = 0;
    var y_tmp = 0;
    var color_tmp;

    var nodo_d = new Array();
    var nodo_d_t = new Array();

    var seq = 0;

    var y_pos = 0;

    for (var i = 0, len = arr.length; i < len; i++) {
        var coor_t;
        var cad_t = arr[i].trim();
        var cad = cad_t.split(" ");
        var color = "black";
        var L = 1;
        nodo_d_t = new Array();
        for (var j = 0, len2 = cad.length; j < len2; j++) {
            var item = cad[j];

            if (item.indexOf("boya-temp") > -1) {
                L = 1;
                if (item.indexOf("<") > -1) {
                    color = "LightBlue";
                } else if (item.indexOf(":") > -1) {
                    color = "rgb(132, 188, 219)";
                } else {
                    color = "RoyalBlue";
                }
            }

            if (item.indexOf("boya-salinidad") > -1) {
                L = 2;
                if (item.indexOf("<") > -1) {
                    color = "Gainsboro";
                } else if (item.indexOf(":") > -1) {
                    color = "#AEAAAA";
                } else {
                    color = "LightSlateGray";
                }
            }

            if (item.indexOf("caudal") > -1) {
                L = 3;
                if (item.indexOf("<") > -1) {
                    color = "Plum";
                } else if (item.indexOf(":") > -1) {
                    color = "BlueViolet";
                } else {
                    color = "DarkMagenta";
                }
            }

            if (item.indexOf("est_temp_min") > -1) {
                L = 4;
                if (item.indexOf("<") > -1) {
                    color = "BurlyWood";
                } else if (item.indexOf(":") > -1) {
                    color = "Peru";
                } else {
                    color = "SaddleBrown";
                }
            }

            sp.push(
                    {p: [{x: (seq * space), y: L * 50}, {x: (space - 20 + seq * (space)), y: L * 50}],
                        w: 20,
                        c: color,
                        v: item,
                        i: y_pos
                    });


            if (seq > 0) {
                /*console.log(nodo_d);*/

                /* Dibujar n-Antiguos-Origen <----> Nuevo-Origen */
                for (var z = 0, len3 = nodo_d.length; z < len3; z++) {
                    sp.push(
                            {p: [{x: nodo_d[z].x, y: nodo_d[z].y}, {x: (seq * space), y: L * 50}],
                                w: 3,
                                c: nodo_d[z].c,
                                i:y_pos
                            });
                }


            }

            y_tmp = L * 50;
            color_tmp = color;
            x_tmp = (space - 20 + seq * (space));

            coor_t = {x: x_tmp, y: y_tmp, w: 2, c: color, i:y_pos};
            nodo_d_t.push(coor_t);


        }
        nodo_d = nodo_d_t;
        seq++;
    }

    return sp;
}

function convert_5(cad) {

    var arr = cad.split(",");

    /*for (var i = 0, len = arr.length; i < len; i++) {
     console.log(arr[i].trim());
     }*/

    var space = 100;
    var sp = new Array();

    var x_tmp = 0;
    var y_tmp = 0;
    var color_tmp;

    var nodo_d = new Array();
    var nodo_d_t = new Array();

    var seq = 0;

    var y_pos = 0;

    for (var i = 0, len = arr.length; i < len; i++) {
        //  var nodo_d = new Array();
        var coor_t;
        var cad_t = arr[i].trim();
        var cad = cad_t.split(" ");
        var color = "black";
        var L = 1;
        nodo_d_t = new Array();
        for (var j = 0, len2 = cad.length; j < len2; j++) {
            var item = cad[j];

            if (item.indexOf("boya-temp") > -1) {
                L = 1;
                if (item.indexOf("<") > -1) {
                    color = "LightBlue";
                } else if (item.indexOf(":") > -1) {
                    if (item.indexOf("24.") > -1 && item.indexOf("25.")) {
                        color = "#8ECDEF";
                    } else if (item.indexOf("25.") > -1 && item.indexOf("26.1")) {
                        color = "rgb(132, 188, 219)";
                    } else if (item.indexOf("26.1") > -1 && item.indexOf("26.7")) {
                        color = "#73A1DB";
                    }

                } else {
                    color = "RoyalBlue";
                }
            }

            if (item.indexOf("boya-salinidad") > -1) {
                L = 2;
                if (item.indexOf("<") > -1) {
                    color = "Gainsboro";
                } else if (item.indexOf(":") > -1) {
                    color = "#AEAAAA";
                } else {
                    color = "LightSlateGray";
                }
            }

            if (item.indexOf("caudal") > -1) {
                L = 3;
                if (item.indexOf("<") > -1) {
                    color = "Plum";
                } else if (item.indexOf(":") > -1) {
                    if (item.indexOf("28.") > -1 && item.indexOf("68.")) {
                        color = "#B47CE3";
                    } else if (item.indexOf("68.") > -1 && item.indexOf("161.")) {
                        color = "#8A2BE3";
                    } else if (item.indexOf("161.") > -1 && item.indexOf("500346.")) {
                        color = "#7022BB";
                    }
                } else {
                    color = "DarkMagenta";
                }
            }

            if (item.indexOf("est_temp_min") > -1) {
                L = 4;
                if (item.indexOf("<") > -1) {
                    color = "BurlyWood";
                } else if (item.indexOf(":") > -1) {
                     if (item.indexOf("67.") > -1 && item.indexOf("69.")) {
                        color = "#EA9849";
                    } else if (item.indexOf("69.") > -1 && item.indexOf("72.")) {
                        color = "Peru";
                    } else if (item.indexOf("72.") > -1 && item.indexOf("76.")) {
                        color = "#AA6F35";
                    }

                } else {
                    color = "SaddleBrown";
                }
            }

            if (item.indexOf("estac-pto-rocio") > -1) {
                L = 4;
                if (item.indexOf("<") > -1) {
                    color = "#E2EFDA";
                } else if (item.indexOf(":") > -1) {
                     if (item.indexOf("64.") > -1 && item.indexOf("67.")) {
                        color = "#C6E0B4";
                    } else if (item.indexOf("67.") > -1 && item.indexOf("69.")) {
                        color = "#A9D08E";
                    } else if (item.indexOf("69.") > -1 && item.indexOf("74.")) {
                        color = "#6CA945";
                    }

                } else {
                    color = "#375623";
                }
            }

            sp.push(
                    {p: [{x: (seq * space), y: L * 50}, {x: (space - 20 + seq * (space)), y: L * 50}],
                        w: 20,
                        c: color,
                        v: item,
                        i: y_pos
                    });


            if (seq > 0) {
                console.log(nodo_d);

                /* Dibujar n-Antiguos-Origen <----> Nuevo-Origen */
                for (var z = 0, len3 = nodo_d.length; z < len3; z++) {
                    sp.push(
                            {p: [{x: nodo_d[z].x, y: nodo_d[z].y}, {x: (seq * space), y: L * 50}],
                                w: 3,
                                c: nodo_d[z].c,
                                i:y_pos
                            });
                }


            }

            y_tmp = L * 50;
            color_tmp = color;
            x_tmp = (space - 20 + seq * (space));

            coor_t = {x: x_tmp, y: y_tmp, w: 2, c: color, i:y_pos};
            nodo_d_t.push(coor_t);


        }
        nodo_d = nodo_d_t;
        seq++;
    }

    return sp;
}

function draw(data, step_sp) {

    var x = d3.scaleLinear(),
            y = d3.scaleLinear();

    /* Initialize tooltip */
    tip = d3.tip()
            .attr('class', 'd3-tip')
            .offset([-14, 0])
            .html(function (d) {
        return d.v;
    });

    var div = d3.select("#graphic-pattern").append("div")
            .attr("class", "tooltip")
            .style("opacity", 0);

    var line = d3.line()
            .x(function (d) {
                return x(d.x/1.6);
            })
            .y(function (d) {
                return y(d.y/1.6 + step_sp);
            });

    var chart = d3.select("#graphic-pattern").append("svg:svg")
            .attr("class", "chart")
            .attr("width", 450)
            .attr("height", 180).append("svg:g")
            .attr("transform", "translate(50,10)");

    var text = chart.append('text').text(step_sp+1)
    .attr('x', -26)
    .attr('y', 35)
    .attr('font-family', 'sans-serif')
    .attr('font-size', '12px')
    .attr('fill', 'white');

    /* Invoke the tip in the context of your visualization */
    chart.call(tip)

    chart.selectAll("path")
            .data(data)
            .enter().append("svg:path")
            .attr("class", "line")
            .attr('d', function (d) {
                return line(d.p);
            })
            .attr('stroke-width', function (d) {
                return d.w/1.8;
            })
            .attr('stroke', function (d) {
                return d.c;
            })
            .on('mouseover', tip.show)
            .on('mouseout', tip.hide);

}

function legend(imagex) {

    var chart = d3.select("#graphic-pattern").append("svg:svg")
            .attr("class", "chart")
            .attr("width", 450)
            .attr("height", 180).append("svg:image")
            .attr("xlink:href", imagex)
            .attr("x", "50")
            .attr("y", "30");
}
