# Site web dynamique


Projet: Graphe d'une fonction du second degré réalisé sur un site web dynamique, hébergeur PythonanyWhere

Chaque contributeur développe sur son compte PythonanyWhere puis git "push" sur Github.

Enfin, le contenu du site est rechargé sur le site central, résultat des sites PythonAnyWhere de developpement.


# grapheur_v1
VERSION 1 : dans un premier temps (version 1) les constantes a, b et c sont fixées: f(x) = 3x² + 2x -10

(les calculs sont fait à part sous excel puis incorporés dans les scripts Python)

Le contenu du site est envoyé sur Github dans un projet /grapheur à l'adresse https://github.com/

pour la verson 1 l'adresse est : https://arnew.pythonanywhere.com

# grapheur_v2
VERSION 2 : la page d'accueil "home.html" contient des champs de saisie pour les constantes a, b et c ce qui permet de construire 2 listes : axe_X et axe_y par calcul de f(x) = ax² + bx + c

ces listes sont envoyées sur la page d'affichage du graphe "page_1.html"

pour la version 2 l'adresse est : https://isn2src.pythonanywhere.com/

# grapheur_v3
VERSION 3 : la page d'accueil "home.html" ne contient contient de champs de saisie pour les constantes a, b et c.
2 fonctions sont proposées :
f(x) = 3x² + 2x -10    et    f(x) = -3x² -2x +10

Les 3 constantes a, b et c sont envoyées par l'URL qui déclenche la fonction "suite()"
decorateur de la "page_1.html" qui affiche le graphe par Charts.min.js

Les listes correspondantes sont calculées (pour le moment "en dur") sont envoyées sur la page "page_1.html"

pour la version 3 l'adresse est : https://begin.pythonanywhere.com/
