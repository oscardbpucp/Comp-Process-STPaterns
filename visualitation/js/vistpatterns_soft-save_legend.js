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

 $("#save-sequences").click(function(){

        var disclevel = parseInt($("#disc-level").val());
        var savesequences = $("textarea#message-text").val();
        var savesequences_t = savesequences;

        $('#myModal').modal('hide');
        $('#graphic-pattern' ).empty();

        var array_sequence = new Array();

        var ndiv_i = 0;

        var array_sc_t = savesequences_t.split('",');
        var array_sc = new Array();

        for (var i = 0; i < array_sc_t.length; i++) {
            var sc_t = array_sc_t[i].trim();

            if ( sc_t.substr(0,1) === '"') {
                sc_t = sc_t.substring(1,sc_t.length);
            }

            if ( sc_t.substr(sc_t.length - 1, 1) === '"') {
                sc_t = sc_t.substring(0, sc_t.length - 1);
            }

            array_sc.push(sc_t);
        }

        console.log(array_sc);


        if (disclevel === 3) {
            for (var i = 0, len = array_sc.length; i < len; i++) {
                sp = convert_3(array_sc[i]);
                draw(sp, i);
            }
            legend("images/leyenda-patrones-escenario-1_div-3_sup-4.png");
            }else{
            for (var i = 0, len = array_sc.length; i < len; i++) {
                sp = convert_5(array_sc[i]);
                draw(sp, i);
            }
            legend("images/leyenda-patrones-escenario-2_div-5_sup-4.png");
            }
        }

);