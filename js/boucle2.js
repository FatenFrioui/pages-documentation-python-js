

let myfriends=["Sou","Faten","Saida","Marwa","Sarra"];

for(let i=0; i<myfriends.length; i++){
    console.log(myfriends[i]);
}

let myfriends2=[1,2,"Sou","Faten","Saida","Marwa","Sarra"];
let onlyname=[];

for(let i=0; i<myfriends2.length; i++){

    if(typeof myfriends2[i]==='string'){

        onlyname.push(myfriends2[i]);
    }
}
console.log(onlyname);

let products=["key","mouse","pen","pad","monitor"];
let colors=["red","green","black"];
let models=[2020,2021];

for(let i=0; i<products.length; i++){
    
    console.log(`* ${products[i]}`);
    console.log("*".repeat(15));
    for(let j=0; j<colors.length; j++){
        console.log(`- ${colors[j]}`);
    }
    for(let k=0; k<models.length; k++){
        console.log(`@ ${models[k]}`);
    }
}

