<h1>‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎SAE IMAGE</h1>
<h6>ARSAMERZOEV Magomed 11A</h6>


<h3> A.0 </h3>
<p>L'erreure afficher par display est que la longeur et la taille de l'image ne convienne pas.
la raison est que le premier octet était a 99 au lieux que 9A, mais pour que display affiche correctement l'image il faut que que le première octet soient initialiser à 0 donc il faut mettre 9A. </p>

<h3> A.1 </h3>
<p> voici le resultat : </p>
<img src="images/image0.png">
<p>mais bon ce résultat ne prouve rien.<br>Pour pouvoir arriver à cela il à fallu ouvrir le fichier bmp en éditeur héxadécimal <img src="images/mosaique.png"> <br> Les premier octets répresente "BM" la signature de bmp, ensuite la taille de l'image ici 4A pour 74 octets ensuite les coordonée de la ou les pixels commence, ici les pixels commence à l'adresse 1A, après 0C réprente la taille de la seconde partie, le 04 04 représente la longeur et la largeure de pixels ici c'est du 4x4 , pour le 18 c'est la valeur héxadécimal de 24, car pour réprésenter les couleurs RVB chacune des couleurs sont codée sur 1 octet, donc 3 octets, sachant qu'un octet c'est 8 bit il faut faire 3*8 donc 24 donc 18 en héxa <br> Ensuite le reste c'est les pixels qui sont mit en fonction de leurs couleur, puisqu'on on est en little endian on fait bleu vert rouge.
</p>
<h3>A.2</h3>
<p>Voici la représentation dans un éditeur héxadécimal de l'image : <img src="images/image copy 2.png"><br>Donc rien de plus à expliquer car tout à été dit dans la question précédente, j'ai du faire attention de bien tout inverser car je suis en little endian, le vert n'était jamais un problème car il est au milieu.</p>

<h3>A.3</h3>
<p>Après la conversion de mon damier avec imagemagick voici le résultat : <img src="images/image copy 3.png"> <br> 
On peut déjà remarquer que la taille du fichier à naturellement changer, elle est passer à 66(en hexadecimal).<br> 
Le codage des pixels reste le même, c'est à dire du codage RGB mit en little endian donc BGR.<br>
Il y à toujours 24 bits par pixels.<br>
Aucune méthode de compression à été utiliser car dans les octets de l'offset 1E les octets sont à 0<br>
Pour savoir la taille des données pixels il faut voir à l'offset 22, et ici on voit 30 donc 48 en décimale</p>
 
<h3>A.4</h3>
<p>après conversion on obtient : <img src="images/image copy 4.png"></p>
<p><b>1. </b>À l'octet 1C on peut voir que le nombre de bits par pixel est de 1.
<br><b>2. </b>La taille du fichier est de 16 en décimal on peut voir ça à l'offset 22.<br><b>3. </b>Aucune méthode de compression utiliser car les valeur de l'offset 1E sont à 0<br><b>4 et 5. </b>Les palettes sont codées de manière 2^n ou n est est le nombre de bits par pixels, dans notre cas 1, donc 2¹(ou 2) ce qui reste cohérent car on à que 2 couleur dans notre mosaique.
<br><b>6. </b>Oui le codage des pixels on changer, car à l'offset 32 il y a le nombre de couleur importante utiliser, ici 2 pour rouge et blanc.<br>Le codage RGB des pixels reste le même, il y a un "00" à chaque codage de RGB surement pour indiquer le padding(il est possible que ça soit pour R.G.B.A, A étant alpha, les nuance de gris mais dans ce cas la puisqu'on est en little endian il aurait du être tout devant faisant A.B.G.R), ensuite le 50 et le A0, il faut convertir les valeurs en binaire, pour A0 par exemple ca nous fait 1010 0000 ce qui est exactement le patterne de notre damier, blanc, rouge, blanc, rouge(1 c'est blanc et 0 c'est rouge), Il faut couper 1 octet en deux pour pouvoir répartire les couleurs sur une ligne, 50 donne 1010 0000 en binaire ce qui est encore le patterne de notre damier <br>
<b>7. </b>Pour modifier les pixels rouge en bleu il suffisait d'inverser les 2 octets de droite et de gauche(donc inverser le rouge et bleu)
<img src="images/image copy 5.png"><br>
<b>8. </b>Pour inverser le bleu et le blanc il faut faire de même dans le codage de pixel on remplace FF 00 00 avec FF FF FF pour obtenir le damier inverser. Ou encore remplacer F0 et 50 (si on fait les 2 en même temps on reviens sur le damier de départ)<img src="images/image copy 6.png"><br>
<b>9. </b> Voici le resultat de <b>Image3</b><br><img src="images/image copy 7.png"><br>Donc en prenant le même raisonnement expliquer dans la question 6, ici pour d'abord avoir une ranger de blanc il faut 1111 donc convertit en héxadécimal ça donne F0 ensuite 2 lignes de rouge donc on met 0 pour les 2 lignes suivantes, après on veut un cadriage de base donc on prend A0<br>
<b>10. </b>Voici une partie de l'image en indexe de couleur ouvert dans un héditeur héxadécimal<img src="images/image copy 8.png"><br>
<b>11. </b>On peut voir le nombre de couleurs dans la palettes à l'adresse 2E, ici 10 converti en binaire 16 donc 2¹⁶ couleurs possible<br>
<b>12. </b> Le Blanc est retrouver en couleur dominante à l'adresse 66 avec FE FE FD reconvertit en RGB et en big endian ca nous donne 253 254 254, donc pas du blanc pur mais du blanc quand même<br>
<b>13. </b>le tableau de pixel commence à l'adresse 76,on peut le voir car c'est la ou s'arrete la définition des couleurs importantes qui se remarque car il 3 octets puis 1 autre octet avec 00, et aussi car visuellement je sais que l'image commence avec du blanc et le fait que CC soient répété met la puce à l'oreille. Mais concrètement la couleur blanche que j'ai répéré auparavant est à la 12ème position (des couleurs importantes) et 12 en héxa se note C, et donc le fait qu'il y est que des ranger de CC fait que ca commence ici.<br>
<b>14. </b>Pour commencer j'ai répéré qu'une des couleurs de bleu était à l'indice 0. Donc pour avoir cette ranger de bleu j'ai juste mit des 0 un peut comme je le sentais<br>et donc voici le résultat<br><img src="images/image copy 9.png"> et voici ce que ça donne dans un éditeur héxadécimal <img src="images/image copy 10.png"><br>
<b>15.<br> </b><img src="images/image copy 11.png">Visuellement la dimunition de couleur se voit, ici c'est surtout la couleur orange qui à été affecter et queleque nuance de bleu.
<br><img src="images/image copy 12.png">D'un point de vue héxadécimal on voit que les couleurs des palettes on été remplacé par des 0 </p>
<p><h3>A.5</h3><br>
<b>1 et 2. </b>Pour passer de 4 à -4 en héxadécimal voici le calcule que j'ai fait: 4-2⁸ = -252,(4 est la valeur que je veux convertir et 2⁸ sont les bits)je prend la valeur absolue 252, et je converti en héxadécimal donc FC et je rempli le reste avec l'inverse de 0 donc F <br> voici ce que ca donne dans l'interpréteur héxadécimal <img src="images/image copy 13.png"> et voici le résultat :<br><img src="images/image copy 14.png"><br>l'image à donc bien été inverser.<br>
<b>3. </b>Pour cette image la hauter est de 425 car A9 01 en little endian donne 425, 425 - 2¹⁶ = -65 1111, 65 1111 donne FE 57 en héxadécimal, 57 FE en little endian, on remplace les 0 par des F et on est bon, voici la représentation dans un éditeur héxadécimal<img src="images/image copy 15.png"></p>
<p><h3>A.6 </h3>
Voici la représentation dans un éditeur héxadécimal : 
<img src ="images/image copy 16.png"><br>
<b>1. </b>6*16 + 4*16² = 1120, le poid du fichier est de 1120 octets, contre les 74 octets initial.<br>
La raison de ce changement est que la méthode de compréssion RLE fait que quand un certain motif répété la simplifie en mettant un nombre signifiant le nombre de fois que le motif est répété,<b>a la suite</b>, donc dans notre cas ce n'est pas le plus pertinant car on à pas de motif répété à la suite, ca fera qu'on ajoutera plus d'octet que nécessaire.<br>
<b>2. </b>c'est à l'adresse 0x0A ou l'on trouve l'entête de la ou démarre les pixels, ici 36 04, donc 0436, et c'est bien à l'adresse 0x436 qu'on voit apparaître des octets avec des 00 et des 01.
<br><b>3. </b>voici une représentation de la ou les pixels sont représenter: 
<img src="images/image copy 17.png"><br>
Comme je l'ai dit il y'a un chiffre pour représenter le nombre de fois qu'un motif est répété, ici il faut savoir que 0 veut dire rouge et que 1 veux dire blanc car le rouge à été défini en premier et le blanc en deuxième. Ensuite pour lire un pixel il faut prendre 16 bits soit 2 octet, 1 octet pour dire le nombre de répétéition et le 2ème la couleur du pixel. En appliquant cette méthode on peut voir que ca reste cohérent, pour rouge blanc rouge blanc, ca nous fait 1 rouge, 1 blanc, 1 rouge, 1 blanc, 01 00 01 01 01 00 01 00(les 00 00 sont la pour représenter les fin de lignes et le 01 de fin est la pour représenter la fin du bitmap).</p>
<p><h3>A.7</h3>
voici une représentation de l'entête :<img src ="images/image copy 18.png"><br>
<b>1. </b>le poid de l'image est de 1102 octets, donc ici c'est logique que ça soit moins lourd car la compression sera plus utile car on à plusieurs fois des pixels répété, des octets vont donc être économisé, contrairement à l'image 4 qui lui n'avait pas de pixels qui se répétait donc ca utiliser 1 octet pour rien.<br>
<b>2. </b>Voici une représentation sur un éditeur héxadécimal :<img src="images/image copy 19.png"><br>
Donc on commence avec 04 01, ce qui veut dire qu'il y aura 4 pixel de couleur blanche(rappel : 0 rouge 1 blanc) suivit d'un double 00 marquant la fin de la ligne. ensuite 04 00 qui veut dire 4 pixel rouge, 2 fois, ensuite 01 01 donc 1 pixel blanc, 01 00 1 pixel rouge, et ainsi du suite. 
</p>
<h3>A.8</h3>
<p>voici la réprésentation héxadécimal du résultat attendu : <img src="images/image copy 20.png"><br>
donc ici j'ai du d'abord enlever le 04 01 qui signifiat 4 pixel blanc, pour ensuite faire 02 01 pour dire que je veux 2 pixel blanc, 01 00 pour 1 pixel rouge et enfin 01 01 pour 1 pixel blanc(je touche pas au reste). Puisque les modifications ont rendu l'image plus lourde je n'ai pas oublier de mettre la bonne taille dans l'entête.</p>
<h3>A.9</h3>
<p>Pour arrive rau résultat attendu j'ai du d'abord dû définir les couleur bleu et vert 
voici la représentation : <img src ="images/image copy 21.png"><br> donc juste après le rouge et le blanc j'ai mit le bleu et le vert donc FF 00 00 et 00 FF 00, donc maintenant le blanc sera 00 le rouge 01 le bleu 02 le vert 03, correspondant à l'ordre de définition.<br>
ensuite pour le codage des pixels en eux même :
<img src="images/image copy 22.png"><br>
Donc en changement notable, j'ai remplacer 01 00 par 01 02 pour remplacer le rouge en bleu, de même pour 04 00, j'ai changer par 04 03 pour mettre en vert.</p>
<p><h3>A.10</h3>
Voici le résultat attendu dans un éditeur héxadécimal :
<img src ="images/image copy 23.png"><br>
rien de plus à dire vu que tout à déjà été souligner précédamment.<br><br>
Pour la réduction d'image j'ai fait ça: <img src="images/image copy 24.png"><br>
j'utilise VScode pour visuliser les images dans ce cas l'image m'est afficher correctement, mais malheureusement sur imagemagick en utilisant "display", ca me renvoie <code>insufficient image data in file</code><br>je n'arrive pas à arranger le problème sans casser toute mon image.</p>
<h3>B.1</h3>
<p>voici mon script python : 
<pre><code>
def B1changecouleur(img):
    i=Image.open(img)
    sortie = i.copy()
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            c = i.getpixel((x,y))
            sortie.putpixel((y,x),c)
    sortie.save("Imageout.bmp")
</code></pre><br>
Donc l'algorithme est en plusieurs étapes, d'abord je copie l'image dans une variable <code>sortie = i.copy()</code>pour pouvoir transposer la première image sur ma nouvelle.<br>
Ensuite avec mes 2 boucles<code>for</code> je parcours tout les pixels de mon image pour pouvoir recuperer la position ainsi que le pixel avec la méthode <code>.getpixel()</code> qu'on stock dans une variable, pour ensuite placer ce pixel par dessus notre image en inversant les indices x et y avec la méthode<code>.putpixel()</code>pour avoir une image inverser.</p>

<h3>B.2</h3>
<p>voici mon script python : 
<pre><code>
def B2mirror(img):
    i=Image.open(img)
    sortie=Image.new(i.mode, i.size)
    donne= list(i.getdata())
    nouvlist = [[]]
    cpt = 0
    for i in range(len(donne)):
        if len(nouvlist[cpt]) < sortie.size[0]:
            nouvlist[cpt].append(donne[i])
        else:
            nouvlist.append([donne[i]])
            cpt +=1 
    cptg = 0
    cptd = 0
    listgauche = [[]]
    listdroite = [[]]
    for i in range(len(nouvlist)):
        for y in range(len(nouvlist[i])//2):
            listgauche[cptg].append(nouvlist[i][y])
        cptg +=1
        listgauche.append([])
        for z in range(len(nouvlist[i])//2,len(nouvlist[i])):
            listdroite[cptd].append(nouvlist[i][z])
        listdroite.append([])
        cptd +=1
    del listdroite[-1]
    del listgauche[-1]
    maindata = []
    for i in range(len(listdroite)):
        for d in range(len(listdroite[0])-1,-1,-1):
            maindata.append(listdroite[i][d])
        for g in range(len(listgauche[0])-1,-1,-1):
            maindata.append(listgauche[i][g])
    sortie.putdata(maindata)
    sortie.save("Imageout1.bmp")</code></pre><br>
Pour la fonction mirroir j'ai travailler avec des listes, pour résumer plus ou moins ce que fait dans cet algorithme, d'abord je met tout les pixels dans une liste avec <code>.getdata()</code>, ensuite avec la première boucle <code>for</code> je met les pixels dans des listes en fonction de la largeur de l'image, si la largeur est de 8 ca sera des listes de 8 éléments. Ensuite je sépare les éléments en 2 et je met les pixels de la première moitié dans une liste "listgauche" et la deuxième moitié dans une liste "listdroite" et ça dans une liste. Ensuite avec la dernière boucle je met les élément de droite d'abord dans le sens inverse des indices ensuite les élément de gauche aussi dans le sens inverse. 
</p>
<h3>B.3</h3>
<p>Voici le script python :<pre><code>
def B3nivgris(img):
    i=Image.open(img)
    sortie = i.copy()
    donne= list(i.getdata())
    for i in range(len(donne)):
        donne[i] = tuple(list((sum(donne[i])//3,sum(donne[i])//3,sum(donne[i])//3)))
    sortie.putdata(donne)
    sortie.save("imageout2.bmp")</code></pre>
Je prend tout les pixels de l'image et pour je remplace chacune des valeur RGB par 1 valeur à chacune qui est calculer avec cette formule <b>Gris = (R+G+B)/3</b> et je met le resultat dans chacune des valeur du tuple représentant le pixel en RGB, je le met dans une liste,liste qu'on doit transformer en tuple (pas possible autrement sur python) et après avoir modifier chaque pixel de ma liste je remplace les donner avec la méthode <code>putdata()</code></p>
<h3>B.4</h3>
<p>Voici le script python : 
<pre><code>
def B4noirblanc(img):
    i=Image.open(img)
    sortie = i.copy()
    donne= list(i.getdata())
    for y in range(len(donne)):
        if donne[y][0]**2 + donne[y][1]**2 + donne[y][2]**2 > (255*255*3)/2:
            donne[y] = tuple(list((255,255,255)))
        else:
            donne[y] = tuple(list((0,0,0)))
    sortie.putdata(donne)
    sortie.save("imageout3.bmp")</code></pre>
Pour pouvoir transformer une image uniquement en noir et blanc, il faut d'abord pour chaque pixel identifié quelle couleur sera suffisament foncé et celle qui sera claire, pour cela on fait une comparaison composé de 2 formules <b>(R*R+V*V+B*B) > 255*255*3/2</b> si j'amais la somme des carré de chaque valeur de RGB est supérieur au carré du nombre de couleur possible sur 8 bits fois trois(car R G B) et divisé par 2, alors ce pixel est blanc sinon cette valeur est noir.</p>