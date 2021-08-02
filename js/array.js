let myfriends=["Sou","Faten","Saida",["Marwa","Sarra"]];

console.log(`Hello ${myfriends[0]}`);
console.log(`Hello ${myfriends[2]}`);
console.log(`Hello ${myfriends[1][2]}`);

console.log(`Hello ${myfriends[3][1]}`);
console.log(`Hello ${myfriends[3][1][2]}`);


console.log(myfriends);
myfriends[2]="Najwa";
console.log(myfriends);
myfriends[3]=["Khalil","Hanen"];
console.log(myfriends);

console.log(Array.isArray(myfriends));

myfriends[myfriends.length]="Najet";// ajouter en fin de array
console.log(myfriends);
myfriends[myfriends.length-1]="chayma";// prendre place le dernier valeur de array
console.log(myfriends);

myfriends.unshift("Baha","Ayoub");// ajouter des elemenets en DEBUT de array
console.log(myfriends);
myfriends.push("Baha","Ayoub");// ajouter des elemenets en FIN de array
console.log(myfriends);

let first=myfriends.shift(); //remove the first element
console.log(myfriends);
console.log(`the first name is ${first}`);

let last=myfriends.pop(); //remove the last element
console.log(myfriends);
console.log(`the last name is ${last}`);

console.log(myfriends);
console.log(myfriends.indexOf("Faten"));
console.log(myfriends.indexOf("Faten",1));

console.log(myfriends.lastIndexOf("Baha"));
console.log(myfriends.lastIndexOf("Baha",-1));

console.log(myfriends.includes("Baha"));
console.log(myfriends.includes("Baha",2));

if(myfriends.indexOf("mama")===-1) //mama n'existe pas dana l array -1
{
    console.log("Not Found"); 
}

console.log(myfriends.sort()); //order by name
console.log(myfriends.reverse()); //order reverse de la derniere
console.log(myfriends.sort().reverse());

console.log(myfriends.slice());
console.log(myfriends.slice(1));
console.log(myfriends.slice(1,3));//ne prend pas en consideration l'element 3

console.log(myfriends.slice(-3));
console.log(myfriends.slice(1,-2));//not included end
console.log(myfriends.slice(-4,-2));
//slice ne change pas l'array
//splice change l'array
let friends=["Sou","Faten","Saida","Marwa","Sarra"];
friends.splice(0,0,"touna","fattouna"); //param start index, nbr d'element à supprimer, elements à ajouter
console.log(friends);

friends.splice(5,1,"fat","fattou"); //commence par indice 5, supprimer 1 element et ajouter les 2 elements
console.log(friends);

let my=["Sou","Faten","Saida","Marwa","Sarra"];
let mynew=["Najet","Chayma"];
let school=["Baha","Ayoub"];

let allfr=my.concat(mynew,school,"mama"); //concatenation

console.log(allfr.join());
console.log(allfr.join(""));
console.log(allfr.join(" @ "));
console.log(allfr.join("|").toUpperCase());



