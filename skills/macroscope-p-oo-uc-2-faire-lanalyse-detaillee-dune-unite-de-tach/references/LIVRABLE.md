# Référence du livrable P-OO UC.2 Faire l'analyse détaillée d'une unité de tâche

## Source analysée

- Fichier source : `../../../macroscope/livrables/ffcf2d82b993.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

Cette activité de technique effectue une analyse détaillée d'une unité de tâche et, en fonction de cette analyse, complète la description de l'unité de tâche. L'analyse détaillée d'une unité de tâche nécessite l'identification et la description des éléments suivants : * les utilisateurs et leurs actions; * la séquence détaillée des actions dans l'unité de tâche et les étapes de tâche connexes; * les services d'interface et les services du noyau requis. Déterminer les actions des utilisateurs, les services d'interface et les services du noyau La séquence d'étapes de tâche de l'unité de tâche est traduite en une séquence d'interactions. Ceci permet de structurer la description du jeu réciproque entre les actions utilisateur, les actions des services d'interface utilisateur utilisés et les actions du noyau. À partir de cette analyse détaillée, une description de l'unité de tâche est établie, de même que les critères de qualité et les conditions de réutilisation. Chaque service d'interface et chaque service du noyau est consigné dans la perspective locale associée. Il est peu probable qu'on utilise des diagrammes de transition d'état à cette étape.

## Raison d’être

Aucune raison d’être explicite n’a été extraite. Déduire l’intention du livrable à partir de sa description, de son contenu et des livrables liés.

## Occurrence

Aucune occurrence explicite n’a été extraite du fichier source.

## Structure détaillée du livrable

1. Synthese
2. Portee
3. Contenu du livrable
4. Decisions et points ouverts
5. Tracabilite TOGAF

## Champs ou sections attendus

- Aucune information explicite extraite du fichier source.

## Objets documentés

- Cette activité de technique effectue une analyse détaillée d'une unité de tâche et, en fonction de cette analyse, complète la description de l'unité de tâche.
- * les services d'interface et les services du noyau requis.
- Déterminer les actions des utilisateurs, les services d'interface et les services du noyau La séquence d'étapes de tâche de l'unité de tâche est traduite en une séquence d'interactions.
- Ceci permet de structurer la description du jeu réciproque entre les actions utilisateur, les actions des services d'interface utilisateur utilisés et les actions du noyau.
- Chaque service d'interface et chaque service du noyau est consigné dans la perspective locale associée.
- * Cette activité de technique est exécutée conjointement avec l'activité P-UIS.5 Modélisation d'ensemble des composantes de l'interface utilisateur, qui participe à la production des spécifications de composantes d'interface clés et représentatives, et avec l'
- * Dans la description de services utilisateur, on peut utiliser une Forme syntaxique simple pour ébaucher les étapes de traitement.
- * Pour décrire la perspective locale d'une unité de tâche : à cette étape, une simple liste des services suffit.
- * 1.2.2 - Service d'interface utilisateur
- * 4.1.2 - Service d'interface utilisateur
- * Conception des composantes de l'interface utilisateur
- * Conception des règles de fonctionnement de l'interface utilisateur

## Tableaux, modèles ou diagrammes recommandés

- Il est peu probable qu'on utilise des diagrammes de transition d'état à cette étape.
- #### Notations
- * Pour décrire la dynamique de l'unité de tâche : on peut utiliser une table d'interaction Macroscope, ou un Diagramme d'activité UML.
- * Pour décrire la dynamique d'une étape de tâche : on peut utiliser une table d'interaction Macroscope, un Diagramme d'activité UML ou un Diagramme de séquence UML.
- * Harmonisation détaillée des modèles de niveau utilisateur
- Une analyse utilisateur détaillée doit être faite pour trouver les services requis des modèles d'objets utilisateur.
- Pour ce faire, on peut utiliser des diagrammes d'interaction de haut niveau, du pseudocode ou d'autres formes syntaxiques simples.

## Livrables et références liés

- P-UIS.3 Analyse des tâches, basée sur les cas d'utilisation de niveau utilisateur
- P-UIS.5 Modélisation d'ensemble des composantes de l'interface utilisateur
- P-UIC.3 Conception des composantes de l'interface utilisateur
- P487S - Spécifications de l'étape de tâche réutilisable
- P490S - Spécifications de l'unité de tâche

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase G/H - Gouvernance de mise en œuvre et gestion du changement.
- Livrable TOGAF cible : Plan de transition, exploitation et adoption.
- Domaine d’architecture principal : utilisation.
- Artefacts associés : Procédure d’exploitation, Guide utilisateur, Matériel de transfert.

## Règles particulières de rédaction

- Présenter P-OO UC.2 Faire l'analyse détaillée d'une unité de tâche comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- * Pour décrire la dynamique de l'unité de tâche : on peut utiliser une table d'interaction Macroscope, ou un Diagramme d'activité UML.
- * Pour décrire la dynamique d'une étape de tâche : on peut utiliser une table d'interaction Macroscope, un Diagramme d'activité UML ou un Diagramme de séquence UML.
- * Dans la description de services utilisateur, on peut utiliser une Forme syntaxique simple pour ébaucher les étapes de traitement.
- * Pour décrire la perspective locale d'une unité de tâche : à cette étape, une simple liste des services suffit.
- Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique.
- #### Exemples
- Pour ce faire, on peut utiliser des diagrammes d'interaction de haut niveau, du pseudocode ou d'autres formes syntaxiques simples.
- L'exemple ci-dessous correspond aux actions d'un «abonné de la bibliothèque» dans le cadre d'une «recherche de livre».

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Cette activité de technique effectue une analyse détaillée d'une unité de tâche et, en fonction de cette analyse, complète la description de l'unité de tâche. L'analyse détaillée d'une unité de tâche nécessite l'identification et la description des éléments suivants : * les utilisateurs et leurs actions; * la séquence détaillée des actions dans l'unité de tâche et les étapes de tâche connexes; * les services d'interface et les services du noyau requis. Déterminer les actions des utilisateurs, les services d'interface et les services du noyau La séquence d'étapes de tâche de l'unité de tâche est traduite en une séquence d'interactions. Ceci permet de structurer la description du jeu réciproque entre les actions utilisateur, les actions des services d'interface utilisateur utilisés et les actions du noyau. À partir de cette analyse détaillée, une description de l'unité de tâche est établie, de même que les critères de qualité et les conditions de réutilisation. Chaque service d'interface et chaque service du noyau est consigné dans la perspective locale associée. Il est peu probable qu'on utilise des diagrammes de transition d'état à cette étape.

### Intrants

Non disponible.

### Extrants

Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique. Les sections des livrables qui sont applicables sont montrées sous chaque livrable. Les livrables détaillés qui peuvent être utilisés au lieu des livrables succincts, ou en complément à ceux-ci, sont listés directement sous les livrables succincts concernés.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
