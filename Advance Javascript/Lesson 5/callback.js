function message(name, callback){
    setTimeout(function(){
        console.log('Hello ' + name);
        callback();
    }, 2000);
}

function done(){
    console.log('Done!');
}

message('John', done);