.. TNSI

.. _tri fusion: https://fr.wikipedia.org/wiki/Tri_fusion

TP : le tri fusion
===================

Le **tri fusion** d’un tableau de nombres est une application du principe **diviser pour régner**.

-  L’algorithme consiste à diviser ce tableau de nombres en 2 tableaux, puis chaque tableau en 2 nouveaux tableaux, etc.
-  Une fois les tableaux divisés jusqu’à avoir qu’une seule valeur, on recompose les tableaux par assemblage en triant les éléments.

Vous trouverez des informations sur la page wikipedia du `tri fusion`_. 

Diviser des tableaux
--------------------

On souhaite créer un tableau de valeurs à partir d’un autre tableau plus grand. Les valeurs sélectionnées se suivent dans le grand tableau ou sont séparées par un même nombre de valeurs.

Le **slice** est une technique en Python qui permet de sélectionner des éléments d’un tableau et se note avec les deux points.

Par exemple, pour extraire les valeurs d’un tableau t, on utilise la syntaxe : ``t[indice début:indice fin:écart]``.

.. note:: 

   Voici trois règles utiles pour les **slice** des list Python:

   -  Si l’indice de début est 0, on peut ne pas l’écrire.
   -  Si l’indice de fin correspond à la dernière valeur, on peut laisser vide.
   -  Si les valeurs à sélectionner se suivent, l’écart n’est pas nécessaire.

Soit t un tableau de 8 valeurs. Créer à partir de ce tableau :

#. Un tableau sans la première et la dernière valeur;
#. Un tableau composé de la première moitié de tableau;
#. Un tableau composé de la seconde moitié de tableau;
#. Un tableau avec les deux valeurs centrales;
#. Un tableau avec les valeurs d’indices pairs;
#. Un tableau avec les valeurs d’indices impairs;

Fusionner des tableaux
----------------------

La fusion de 2 tableaux peut se réaliser de plusieurs façons.

#. La concaténation est une opération consistant à assembler deux tableaux en un seul. Le signe d’addition ``+`` est utilisé pour la concaténation.

   a. Concaténer les tableaux ``[3]`` et ``[5]``.
   b. Concaténer les tableaux ``[5]`` et ``[3]``.
   c. Concaténer les tableaux ``[3,7]`` et ``[5,8]``.
   d. Les tableaux obtenus par concaténation ont-ils leurs valeurs triées ? Pourquoi ?

#. Il est possible de fusionner deux tableaux triés en un seul tableau trié. Pour y parvenir, il faut parcourir chaque tableau et insérer dans un nouveau tableau les valeurs en respectant l’ordre.

   a. En réalisant des schémas, décrire la fusion des tableaux ``[1,6,8]`` et ``[3,5]``.
   #. Écrire en Python une fonction fusion_tableaux qui prend en paramètre 2 tableaux triés et renvoie un tableau trié avec les valeurs des 2 tableaux passés en argument.

Le tri fusion
-------------

L’algorithme se décompose en 2 temps. Le premier temps consiste à **diviser** le tableau en tableaux vides ou à 1 valeur. Le second temps consiste à **fusionner** les tableaux triés jusqu’à obtenir le tableau initial trié.

#. Appliquer le tri fusion sur la liste ``L=[7,4,9,1,3,5,8]`` en donnant précisément les différentes étapes.
#. On donne le script de la division: 

   .. figure:: ../img/tri_fusion.png
      :alt: image
      :align: center
      :width: 520

   Saisir et compléter ce code dans votre script Python.

#. Écrire la fonction fusion qui effectue la fusion de 2 tableaux triés.
#. Créer des listes aléatoires de nombres entiers puis vérifier que le tri fusion est réalisé.

Complexité du tri fusion
------------------------

On va comparer l’efficacité du tri fusion par rapport au tri par sélection et tri par insertion en mesurant les temps d'exécution de ces tris.

On donne le fichier Python ``mesure_tris.py`` qui contient:

-  La fonction 

a. Reprendre le TP sur la mesure du temps d'exécution des tris par sélection et insertion.
   b. Importer la fonction ``tri_fusion`` puis effectuer des mesures de temps d'exécution de ce tri.
   c. Comparer la complexité des tris en comparant vos mesures.
