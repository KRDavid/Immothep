# Immothep


## Informations générales

La société Immothep, nouveau fleuron de l'immobilier Français, souhaite créer un module d'estimation de biens basé sur l'intelligence artificielle pour enrichir sa plateforme et acquérir de nouveaux acheteurs/vendeurs.


## Démarrage

Nous utilisons deux NoteBooks au sein de ce projet.

Le premier, "NoteBookBordeaux.ipynb" présente l'ensemble des étapes nécessaires au nettoyage de notre jeu de données ainsi que les différents algorithmes utilisés afin d'effectuer une étude de la valeur des biens immobiliers de la ville de Bordeaux.

Le second, "NoteBookFrance.ipynb" présente le même déroulé (Sans explications, pour les explications se référer au premier NoteBook) pour l'ensemble de la France, il sera à executer afin de faire fonctionner notre API.

Notre dossier "functions" contient nos différents modules utilitaires tels que "split.py" permettant de filtrer notre jeu de données selon certaines valeurs, "download.py" permettant de télécharger les données via le site data-gouv.fr, "isolation_forest.py" permettant d'utiliser un algorithme de foret d'isolement afin de mettre en valeur les données aberrantes de notre jeu de données, "randomforestclass.py permettant de stocker notre modèle, "zip_dictionnary.py" et "predict.py" permettant de récupérer les prix moyens par ville et de faire la prédiction pour notre API.

L'ensemble des CSV créés au sein des NoteBooks sont placés dans le dossier data/CURATED.

Notre jeu de données brut est quant à lui contenu dans le dossier data/RAW.


## Utilisation

Pour lancer le serveur, lancez une invite de commande et placez vous à la racine du dossier principal.

Executez la commande :
```
uvicorn main:app --reload
```

Après une petite attente, le serveur est lancé, ouvrez un navigateur et rendez vous à l'adresse suivante :
"127.0.0.1:8000/api/estimate/code_po=***code postal***&surface_t=***Surace terrain***&surface_b=***Surface batiment***&nb_pieces=***Nombre de pièces***"

Bingo ! L'estimation du bien est devant vos yeux !


## Auteurs

Maxime Veysseyre

David Krygier