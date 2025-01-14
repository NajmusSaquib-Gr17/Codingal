let array = [1, 2, 3, 4 , 5];
console.log(array);

let array_1 = [1, 2, 3, 4 , 5];
console.log(array_1[3]);


let array_2 = [1, 2, 3, 4 , 5];
array_2.push(6);
console.log(array_2);


let array_3 = [1, 2, 3, 4 , 5];
array_3.push(7);
array_3.pop();
console.log(array_3);


let array_4 = [1, 2, 3, 4 , 5];
array_4.unshift(7);
console.log(array_4);



let array_5 = [1, 2, 3, 4 , 5];
array_5.unshift(7);
array_5.shift();
console.log(array_5);


let array_6 = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10];
console.table(array_6);

let array_7 = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10];

for (let i=0; i < array_7.length; i++){
    console.log("Element " + i + ":" + array_7[i]);
}


array_8 = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10];
doubled = array_8.map(function(element){
    return element * 2;
})
console.log(doubled);

