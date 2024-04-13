// havia um erro de locação da pasta static em que o caminho não era reconhecido 
// questão a resolver para recuperar objetos e respectivas chaves\valores 
//  a partir de um checkbox 

function myChoice() {

    let cell = "";
    let cells = "";
    let choice = "";

    let rows = document.getElementsByTagName("tr");
    table = document.getElementById("tb_prod"); // aqui tive que navegar na hierarquia de elementos para buscar id fixo;
    query =table.querySelectorAll(".w3-check"); // não pude utilizar o id pois a tabela iterada e javascript não reconhece a tag {{p.id}}

    // não possível: document.getElementById("choice{{p.id}}").checked = true;

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
            cell = table.rows[i].cells + "<br>";
        }*/

    //document.getElementById("demo").innerHTML = cell;
    //document.getElementById("demo").innerHTML = cell[2].innerHTML+" - "+cell[3].innerHTML
    //document.getElementById("demo").innerHTML = cell[0].innerHTML+" - "+cell[1].innerHTML;  
    }

