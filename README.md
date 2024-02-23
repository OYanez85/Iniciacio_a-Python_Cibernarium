# Iniciacio_a-Python_Cibernarium
**1. Les variables**

Ha arribat el moment de fer ús de les variables amb Python. Primer, veurem com escriure-les correctament i de què es componen, quin tipus d’informació emmagatzemen i quines accions podem fer servir per operar amb les seves dades o contingut.

Les variables són les entitats que permeten emmagatzemar la informació dels programes. Són, doncs, principalment, espai de memòria on podem accedir per fer ús de les dades que hi guardem. En aquest curs, però, no ens aturarem a analitzar la gestió de la memòria, sinó que ens centrarem a saber treballar amb les variables des d’un punt de vista pràctic i molt orientat a la redacció de codi.

La sintaxi de les variables amb Python és molt senzilla i neta. Començarem per gestionar els tipus de variables més bàsics i, després, veurem algunes variables menys intuïtives que, potser, requeriran més atenció si mai abans no hem après cap llenguatge de programació.

**Exercici 1: Ara et toca a tu: Repte. Calcula el valor de x**

Suposem que fem diverses compres a l’any, en total quatre, a una empresa proveïdora que ens ven els seus productes en dòlars. Els imports de les compres són: 356.75 $, 487.45 $, 295.83 $ i 532.00 $. Haurem de convertir el valor de dòlars a euros. 

Part 1: Calcula i imprimeix per pantalla les dades següents:

Suma total de les compres en euros
Mitjana de les quatre compres en euros
 

Nota: procura que la variable que necessitaràs per tenir el canvi de dòlars a euros rebi la dada a través d’una entrada per teclat.

Part 2: Imagina que l’última comanda (la de 532.00 $) ha tingut un problema i només arriba el 80 % del gènere en bones condicions i, per tant, diem al proveïdor que només li pagarem el 80 % de l’import acordat prèviament.

Calcula, ara, els mateixos resultats que en el cas anterior i imprimeix-los per pantalla.
Podries dir quin tipus de dada (informació) és la suma total de qualsevol dels dos casos?
Sabries canviar-la a una dada del tipus string?
 

Procura esforçar-te per resoldre les dues parts de l’exercici sense necessitat de mirar la solució. Si no te’n surts, llavors consulta-la.

Endavant!

**Idees clau: Les variables**

A continuació, farem un repàs de les idees més importants que hem tractat.

Què és realment una variable.
Com declarar-la en el codi.
Quins tipus d’informació poden guardar les variables.
Quines operacions podem fer amb els diversos tipus de dades.
Com podem passar un tipus de dada a un altre.
 

També hem après a entrar una dada per teclat i guardar-la en una variable. A continuació, hem estat capaços d’imprimir resultats en pantalla i, fins i tot, especificar quants decimals volem mostrar.

I, no menys important, ara sabem escriure comentaris en el nostre codi.

**2.Estructura de dades. Llistes i diccionaris**

Ha arribat el moment de treballar amb aquests dos tipus d’estructures de dades: les llistes i els diccionaris. També aprofundirem sobre les accions que podem fer amb elles, com ara afegir o treure elements, accedir a la informació, etc.

**Exercici 2: Ara et toca a tu: Repte. La cistella de la compra**

Fixa’t bé en l’enunciat i completa l’exercici següent:

Suposem que hem fet una compra en un fruiteria. Les fruites i el seu import ens apareix en el tiquet de la manera següent:

Pomes: 3,56 €
Mandarines: 4,35 €
Síndria: 6,23 €
Maduixes: 4,28 €
Peres: 2,86
Taronges: 3,48 €
 

Guarda la llista de la compra en forma de diccionari (pots ometre les unitats). Escriu el codi per tal de resoldre les qüestions següents:

Podries calcular la mitjana de la compra accedint als valors de les claus? Procura posar només dos decimals.
Podries copiar i guardar en una nova variable la llista dels imports sense tenir en compte els dos últims?
Podries saber com comprovar si hem comprat llimones?
 

Endavant!

Les llistes són les entitats (objectes) que permeten guardar una col·lecció de dades dins d’una mateixa variable. Els diccionaris també ho són, però en aquest cas necessitem una clau per accedir a la informació.

Durant la redacció de codi és molt habitual fer ús d’aquestes estructures, així que aquest mòdul és prou important per tal que, una vegada haguem entès com treballar-hi, fem un salt significatiu com a futurs programadors i programadores. 

**Idees clau: Estructura de dades. Llistes i diccionaris**


En aquest mòdul has après a treballar amb llistes i diccionaris, que són les estructures de dades més utilitzades en Python.

Les llistes són una col·lecció de dades del mateix tipus o no, a les quals es pot accedir mitjançant un index de posició. Cada dada a la llista té assignat el seu propi index. Hi ha una particularitat i és que el primer index sempre és 0 i no pas 1.  A més a més, amb les llistes, has après a fer les accions següents:

- Saber si una dada forma part de la llista mitjançant la sentència in, la qual torna un valor veritable o fals, depenent de si en forma part o no.
- Afegir una nova dada amb append().
- Treure l’última dada amb pop().
- Saber quina posició té una dada amb index().
- Sumar els valors que conté la llista amb sum().
- Saber el número de dades que conté una llista amb len().
 

Els diccionaris són una col·lecció de dades formades per parelles clau-valor. Per accedir a la informació d’una dada, cal saber la clau associada i no la seva posició, com es fa amb les llistes. Amb els diccionaris, has après a:

- Afegir una nova parella clau-valor.
- Saber quantes parelles clau-valor té el diccionari.
- Fer ús de la funció get() per accedir a una informació.
- Extreure una llista del conjunt de les claus.
- Generar una llista del conjunt dels valors.
- Generar una llista del conjunt de parelles clau-valor.
- Eliminar una parella clau-valor.
 

També hem vist que els objectes, les funcions i les estructures de dades estan connectades entre elles i no són entitats aïllades.

**3. Estructures condicionals i cicles**

En les properes activitats  faràs realment un pas endavant per convertir-te en programador o programadora i aconseguiràs les habilitats que et permetran dissenyar el teu primer algoritme. Veurem les sentències condicionals i els cicles.

Les sentències condicionals són blocs de codi que ens serveixen per executar una sèrie d’accions o unes altres, depenent d’unes determinades condicions. Aquestes estructures, doncs, fan possible dissenyar algoritmes capaços de resoldre problemes molt complexos.

El cicles són blocs de codi que es repeteixen sempre que es compleixi una condició. Aquesta eina permet repetir una sèrie d’accions sense necessitat de repetir les mateixes línies de codi.

Les condicions i els cicles ens esperen. Comencem!

**3.1. Exercici: Ara et toca a tu: Repte. Ser o no ser**
Genera una seqüència iterable formada per una llista de 10 números enters majors que 0 i menors que 20. Procura que tots els números d’aquesta llista els entris per teclat. Una vegada tinguis la llista, realitza les accions següents:

Fes que tots els elements siguin multiplicats per 3, si són menors que 10, o per 2, si són majors que 10. Fes ús de l’estructura for.
Imprimeix la llista. Fes ús de l’estructura for.
A continuació, imprimeix només els cinc primers números. Fes ús de l’estructura while.
 

Si vols, i de manera opcional, intenta fer aquest últim pas:

Torna a fer les accions anteriors, però en lloc d’introduir els números per teclat, fes-ho important el mòdul random i fent ús de la funció randint().

**Idees clau: Estructures condicionals i cicles**
En aquest mòdul hem après a fer ús dels cicles for i while. Per una banda, els cicles for ens permeten repetir blocs de codi a través d’una seqüència iterable. Per altra banda, podem executar el codi que hi ha a dins de l’estructura while repetidament, sempre que la condició que marquem sigui certa.

Els blocs de codi, tant per als cicles for com per als cicles while, són aquelles línies de codi que van després dels : –dos punts– i que estan indexades una posició a la dreta. De fet, qualsevol bloc de codi en Python que formi part d’una estructura sempre s’escriurà així.

La funció range() ens permet generar una seqüència iterable per ser utilitzada en els cicles for. El primer valor marca l’inici de la seqüència, el segon marca el final (el valor no està inclòs) i el tercer marca l’avanç a través d’aquesta seqüència.

La sentència in és la que ens indica sobre quina seqüència s’executarà el cicle for. De fet, l’expressió in també pot referir-se directament a una llista i tractar-la com una seqüència iterable.

També hem après a generar una seqüència de valors enters de manera aleatòria fent ús de la funció randint() del mòdul random.

La funció while avalua la condició només a l’inici del cicle. Això vol dir que, si durant el bloc de codi no es compleix la condició, primer s’executarà tot el bloc i s’aturarà la repetició només quan el cicle torni a començar.

**Construcció de funcions**

Les funcions permeten replicar blocs de codi allà on els necessitem. Això vol dir que només les haurem de definir una vegada per fer-les servir després sense límit de rèpliques. Les funcions poden contenir, dins dels seus blocs, totes les sentències i estructures que hem après durant el curs.

Les funcions poden ser simples o molt complexes i, fins i tot, es poden fer servir una dins d’una altra. Imagina que vols crear un joc en el qual el protagonista és un avatar que ha de superar diverses aventures. Totes les accions que podrà fer aquest avatar estaran definides per les funcions que tu defineixis. Saltar, anar a l’esquerra, atacar… tot això són funcions.

Les funcions es poden emmagatzemar en una variable. Sí, i també són objectes. Recorda: a Python, tot són objectes.

