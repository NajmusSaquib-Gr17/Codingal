//Array Sorting 


//Ascending Order

function array_1(){

let array_ascending_order = [5, 2, 9, 1, 7];

    array_ascending_order.sort(function(a, b) {
        return a - b;
    });
    document.getElementById("demo1"). innerHTML = array_ascending_order + " //Ascending Order";
}



//Descending Order

function array_2(){

    let array_descending_order = [5, 2, 9, 1, 7];   

    array_descending_order.sort(function(a,b){
        return b - a;
    })
    document.getElementById("demo2").innerHTML = array_descending_order + " //Decending Order";
}

//Reverse Order 

function array_3(){

    let array_reverse = [5, 2, 9, 1, 7];

    array_reverse.reverse();
    document.getElementById("demo3").innerHTML = array_reverse + " //Reverse Order";
}

function array_4(){

    let array_map = [5, 2, 9, 1, 7];

    doubled = array_map.map(function(a){
        return a * 2;
    })

    document.getElementById("demo4").innerHTML = doubled + " //Doubled Number";
}
