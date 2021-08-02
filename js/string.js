
let thename="Faten ";

console.log(thename[2]);
console.log(thename.charAt(2));

console.log(thename.length);
console.log(thename.trim()); //elliminer les espaces
console.log(thename.toUpperCase); //rend majuscule
console.log(thename.toLowerCase); //rend miniscule


console.log(thename.trim().charAt(2).toUpperCase()); 
//rend t majuscule

let a="Faten Frioui";
console.log(a.indexOf("Frioui"));
console.log(a.indexOf("Frioui",8));

console.log(a.indexOf("F"));
console.log(a.lastIndexOf("F")); //il commence à compter à partir de dernier caractere
console.log(a.slice(2,7));//prend une partie de 1 er indice jusqu'à deuxieme indice
console.log(a.slice(-5,-2));
console.log(a.repeat(5));
console.log(a.split(5)); //retourner sous forme de array
console.log(a.split(" ")); //couper sur plusieurs parties et mettre dans un array
console.log(a.split(","));
console.log(a.split(" ",2)); //couper deux mots
console.log(a.substring(2));
console.log(a.substring(2,5));
console.log(a.substring(5,2));
console.log(a.substring(-7,2)); //0-2
console.log(a.substring(a.length)); //afficher dernier caractere
console.log(a.substring(a.length-5,a.length-3));
console.log(a.substr(0,6)); //extraction
console.log(a.substr(17)); 
console.log(a.substr(-3)); 
console.log(a.substr(-5,2)); 
//includes retourne true ou false
console.log(a.includes("oui")); 
console.log(a.includes("oui",10));

console.log(a.startsWith("F")); 
console.log(a.startsWith("F",2));

console.log(a.endsWith("en",5)); //compter length et non index, retourn false si il se fini par....
console.log(a.endsWith("i")); //compter sur toute la chaine

console.log((10=="10")); //compare value only
console.log((10!="10")); //compare value only
console.log((10==="10")); //compare value + type
console.log((10!=="10")); //compare value + type

console.log(typeof "Faten"===typeof "Frioui"); 