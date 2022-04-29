# Matériel supplémentaire pour l'article de Dong, Gambette & Dominguès aux JADT 2022

## Français (English below)

Ce répertoire contient 5 dossiers : Data_example, Models_and_Evaluation, Scripts, Tree_cloud et Typology.

Dans le dossier "Tree_cloud", vous trouverez 3 fichiers, chacun contient repectivement un nuage arboré issu des 3 itérations décrites dans l'article, dont voici le premier : 

<img src="https://raw.githubusercontent.com/DongChuanming/JADT2022_classification_et_enrichissement/main/Tree_cloud/JADT_nuage_arbore_iteration_1.png" alt="drawing" style="width:300px;"/>

Dans le dossier "Typology", vous trouverez une formes listant les déclencheurs d'événements attribués aux chaque classe dans la typologie avec une segmentation par itération, ces déclencheurs sont manuellement extrait à partir des nuages arborés dans le dossier tree_cloud.

Le dossier "Scripts" contient le programme utilisé pour générer les formes fléchies des déclencheurs classés (sous-dossier "inflected_forms_generator"), ainsi qu'un algorithme pour entraîner le classifieur de la typologie (sous dossier "classifior_trainer").

Le dossier "Data_example" contient les fichiers qui font partie du corpus utilisé dans l'algorithme pour entraîner le classifieur. Considérant la taille grande du corpus, les fichiers dans ce dossier représentent seulement une petite portion du corpus utilisé dans le projet.

Le dossier "Models_and_Evaluation" contient les modèle de classifieurs entraînés et leur résultat d'évaluation. Dans le sous-dossier "iteration1" vous trouverez le modèle entraîné après la première itération (clf_iter1.pickle) et son score sur chaque classe de typologie (evaluation_model_1.tsv), et dans le sous-dossier "iteration2" vous trouverez le modèle entraîné à la fin de la deuxième itération (clf_iter2.pickle) et son score sur chaque classe de typologie (evaluation_model_2.tsv).


## English

This directory contains 5 folders: Data_example, Models_and_Evaluation, Scripts, Tree_cloud and Typology.

In the "Tree_cloud" folder, you will find 3 files, each one contains respectively a tree cloud from the 3 iterations described in the article, here is the first one: 

<img src="https://raw.githubusercontent.com/DongChuanming/JADT2022_classification_et_enrichissement/main/Tree_cloud/JADT_nuage_arbore_iteration_1.png" alt="drawing" style="width:300px;"/>

In the "Typology" folder, you will find a form listing the event triggers assigned to each class in the typology with a segmentation by iteration, these triggers are manually extracted from the tree clouds in the tree_cloud folder.

The "Scripts" folder contains the program used to generate the inflected forms of the classified triggers ("inflected_forms_generator" subfolder), as well as an algorithm to train the typology classifier ("classifior_trainer" subfolder).

The "Data_example" folder contains the files that are extracted from the corpus which is used in the algorithm to train the classifier. Considering the large size of the corpus, the files uploaded in this folder represent only a small portion of the corpus used in the project.

The "Models_and_Evaluation" folder contains the trained classifier models and their evaluation result. In the "iteration1" subfolder you will find the trained model after the first iteration (clf_iter1.pickle) and its score on each typology class (evaluation_model_1.tsv), and in the "iteration2" subfolder you will find the trained model at the end of the second iteration (clf_iter2.pickle) and its score on each typology class (evaluation_model_2.tsv).
