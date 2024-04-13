

function myChoice() {

    let rows = document.getElementsByTagName("tr");
    cell = "";
    cells = "";
    choice = "";

    table = document.getElementById("tb_prod");
    query = table.querySelectorAll(".w3-check");
    let list = "";  

    for (let i=1; i<=query.length; i++) {
        if (query[i] = true) {
            list += "ok"+i+"<br>";
        } else {
            list += "nada encontrado"+i+"<br>";
        }
        document.getElementById("demo").innerHTML = list;
    }
    /*for (let i=1; i<=table.length; i++) {
        for (let j=0; j<3; j++) {
            cell[j] = table.rows[i].cells[j];
        }
        cells[i] = table.rows[i].cells + "<br>";
    }
    document.getElementById("demo").innerHTML = cells;*/

    //document.getElementById("demo").innerHTML = cell;
    //document.getElementById("demo").innerHTML = cell[2].innerHTML+" - "+cell[3].innerHTML
        //document.getElementById("demo").innerHTML = cell[0].innerHTML+" - "+cell[1].innerHTML;  
    }

