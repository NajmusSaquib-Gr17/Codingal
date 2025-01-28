//Array Sorting 


//Ascending Order

function array_1(){

let array_ascending_order = [5, 2, 9, 1, 7];

    array_ascending_order.sort(function(a, b) {
        return a - b;
    });
    document.getElementById("demo1"). innerHTML = array_ascending_order;
}



//Descending Order

function array_2(){

    let array_descending_order = [5, 2, 9, 1, 7];   

    array_descending_order.sort(function(a,b){
        return b - a;
    })
    document.getElementById("demo2").innerHTML = array_descending_order;
}

//Reverse Order 

function array_3(){

    let array_reverse = [5, 2, 9, 1, 7];

    array_reverse.reverse();
    document.getElementById("demo3").innerHTML = array_reverse;
}
