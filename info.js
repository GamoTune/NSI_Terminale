//Du commentaire

/*
EN FIN DE LIGNES : ;
Si tu le fait pas c'est pas grave parce que le JS va le mettre tout seul mais c'est mieux de le mettre

*/





//--------------------------------------- LES VARIABLES

//Pour déclarer une variable, on utilise 'var' et non 'let' ou 'const'.
//Il en existe plusieurs types

//Les variables globales : modifiable partout dans le code
var variable1 = 0;

//Les constantes : non modifiable partout dans le code
const VARIABLE2 = 0; //btw le bleu est plus foncée que les variables
//Et par convention les constantes sont en majuscule

//Les variables local : elle ne sont accessibles que dans une partie du code (par exemple une boucle for)
let variable3 = 0;

//Les variables non définies : elle ne sont pas définies (= undefined)
var variable4;

//Pour les liste et les dico c pareil :

//Liste
var liste1 = [];

//Dico
var dico1 = {};


//Une petite diff avec Python c pour l'ajout et la suppression de 1
//En python tu est obliger de faire i += 1 ou i -= 1
//Alors que en JS : i++ ou i-- fonctionne aussi





//--------------------------------------- LES FONCTIONS

//Pour définir une fonction, on utilise 'function' et non 'def'.
//Il faut aussi utilsier des accolades pour définir ce qui est DANS la fonction, du coup on ce fous de l'indendation.

function fonction1() {
    //Faire quelque chose
}

//On passe les paramètres dans les parentheses

function function2(parametre1, parametre2) {
    //Faire quelque chose
}






//--------------------------------------- LES CONDITIONS ET LES BOUCLES

//Pour les conditions c'est un peu différent de Python
//Il faut mettre des parenteses autour de la condition
//Et il fait les accollades pour définir ce qui est DANS la condition

var condition1;
var condition2;

if (condition1 == condition2) {
    //Faire quelque chose
}

//Si tu veux mettre plusieurs conditions, 'and' ou 'or' ne fonctionne pas.
// Il faut utiliser '&&' pour 'and' et '||' pour 'or' (altgr + 6)

if (condition1 == undefined && condition2 == undefined) {
    //Faire quelque chose
}

//Pour les boucles c'est plus tricky que en python.
//Il faut comme pour les conditions, mettre des parenthese
//La syntaxe chanque aussi, je te donne quelques exemples


//Pour faire un 'for i in range(valeur):' cela donne :
let valeur = 5
for (let i; i < valeur; i++) {
    //Faire quelque chose
}
//'Let i' c'est pour definir 'i'
//'i < valeur' c'est la condition pour sortir de la boucle
//'i++' c'est pour ajouter 1 a chaque iteration de la boucle
//ATTENTION A NE PAS OUBLIER LES ';' 


//Pour faire un 'for i in liste:' cela donne:
let liste = [0, 1, 2, 3, 4]
for (let i of liste) {
    //Faire quelque chose
}


//Pour faire un 'while condition:' cela donne:
let condition = true
while (condition) {
    //Faire quelque chose
}





//--------------------------------------- LES LISTES ET LES DICO

var element = 0

//Pour les listes et les dico c'est un peu différent de Python

//Pour les listes

//Pour ajouter un élément a la fin de la liste
liste1.push(element)

//Pour ajouter un élément au début de la liste
liste1.unshift(element)

//Pour supprimer le dernier élément de la liste
liste1.pop()

//Pour supprimer le premier élément de la liste
liste1.shift()

//Pour supprimer un élément a une position précise
liste1.splice(0, 1) //Le premier paramètre est la position de l'élément et le deuxième est le nombre d'élément a supprimer

//Pour acceder a un élément de la liste
liste1[0] //La position de l'élément dans la liste

//Pour connaitre la taille de la liste
liste1.length


//Pour les dico

//Pour ajouter un élément au dico
dico1['cle'] = element

//Pour supprimer un élément du dico
delete dico1['cle']

//Pour acceder a un élément du dico
dico1['cle']

//Pour connaitre la taille du dico
Object.keys(dico1).length //Il faut utiliser Object.keys() pour connaitre la taille d'un dico (oui c'est chiant)





//--------------------------------------- LES CLASSES

//Pour les classes c'est un peu différent de Python (encore une fois)

//Pour déclarer une classe
class Classe1 {
    constructor(parametre1, parametre2) {
        //Faire quelque chose
    }
}
//Il faut utiliser 'constructor' pour définir ce qui est éxecuter quand on crée un objet de la classe a la place de 'def __init__' en Python
//Les paramètres de la classe sont défini dans le constructor

//Pour créer une propriété dans une classe
class Classe1 {
    constructor(parametre1, parametre2) {
        this.propriete1 = parametre1
        this.propriete2 = parametre2
    }
}
//Il faut utiliser 'this' pour définir une propriété dans une classe a la place de 'self' en Python
//Il est tout a fait possible de définir une propriété sans paramètre ou de la définir plus tard (sans le constructor)

//Pour définir une fonction dans une classe
class Classe1 {
    constructor(parametre1, parametre2) {
        //Faire quelque chose
    }

    fonction1() {
        //Faire quelque chose
    }
}

//Pour créer un objet de la classe
var objet1 = new Classe1(parametre1, parametre2)
//Il faut utiliser 'new' pour créer un objet de la classe a la place de 'Classe1()' en Python

//Pour acceder a une propriété de l'objet
objet1.propriete1 //Comment en Python

//Pour acceder a une fonction de l'objet
objet1.fonction1() //Comment en Python

//Pour supprimer une propriété de l'objet
delete objet1.propriete1 //Comment en Python

//Pour supprimer un objet
delete objet1 //Comment en Python





//--------------------------------------- LES EVENEMENTS

//Pour les événements c'est un peu différent de Python (encore une fois)

//Pour définir un événement
element.addEventListener('click', function1)
//Il faut utiliser 'addEventListener' pour définir un événement a la place de 'bind' en Python

//Pour définir une fonction qui est éxecuter quand l'événement est déclencher
function function1() {
    //Faire quelque chose
}

//Pour supprimer un événement
element.removeEventListener('click', function1)
//Il faut utiliser 'removeEventListener' pour supprimer un événement a la place de 'unbind' en Python


/*

Bon y a pas tout evidement ici mais c'est les bases
Pour plus d'info : https://developer.mozilla.org/fr/docs/Web/JavaScript (mdr merci copilot pour le lien)
Pour la gestion des document HTML je sais pas faire donc je te laisse chercher mais je sais que c'est de la forme : document.getElementById('id') ou document.getElementsByClassName('class') ou document.getElementsByTagName('tag')
Si tu a des questions n'hésite pas a me demander

*/