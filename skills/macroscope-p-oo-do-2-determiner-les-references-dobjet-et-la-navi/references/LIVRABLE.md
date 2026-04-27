# Référence du livrable P-OO DO.2 Déterminer les références d'objet et la navigation

## Source analysée

- Fichier source : `../../../macroscope/livrables/079ff83ccc03.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

Cette activité de technique détermine la nature des attributs de référence d'une classe qui activent la navigation entre les objets. Les références correspondent aux attributs réalisateur. Elles proviennent de : * l'analyse des interactions documentées dans le P540S Spécifications de la séquence réalisateur par la technique P-OO-DI Modélisation des interactions de niveau réalisateur; * la traduction initiale des associations utilisateur, effectuée par l'activité P-OO-DO.1 Traduire le modèle utilisateur; * des besoins définis par les perspectives locales de la vue utilisateur, spécifiés dans la section Perspective locale de l'unité de tâche du P490S Spécifications de l'unité de tâche, la section Perspective locale de l'étape de tâche du P487S Spécifications de l'étape de tâche réutilisable, et la section Perspective locale du service du P180S Spécifications de composante du noyau. Au besoin, une perspective locale peut être spécifiée pour un service associé à une composante d'interface utilisateur, dans les livrables P186S Spécifications de composante réutilisable d'interface, P487S Spécifications de l'étape de tâche réutilisable, et P490S Spécifications de l'unité de tâche. Cela implique la définition des éléments suivants : * chemins de navigation; * direction de navigation; * types de référence requis; * contraintes d'intégrité des liens interobjets.

## Raison d’être

Aucune raison d’être explicite n’a été extraite. Déduire l’intention du livrable à partir de sa description, de son contenu et des livrables liés.

## Occurrence

Aucune occurrence explicite n’a été extraite du fichier source.

## Structure détaillée du livrable

1. * 3.1 - Base de données P510C - Structure de la base de données * 2.1.2 - Attributs de l'enregistrement ou de la table

## Champs ou sections attendus

- * 3.1 - Base de données P510C - Structure de la base de données * 2.1.2 - Attributs de l'enregistrement ou de la table

## Objets documentés

- * des besoins définis par les perspectives locales de la vue utilisateur, spécifiés dans la section Perspective locale de l'unité de tâche du P490S Spécifications de l'unité de tâche, la section Perspective locale de l'étape de tâche du P487S Spécifications de
- Au besoin, une perspective locale peut être spécifiée pour un service associé à une composante d'interface utilisateur, dans les livrables P186S Spécifications de composante réutilisable d'interface, P487S Spécifications de l'étape de tâche réutilisable, et P4
- * Diagramme de classe (avec interfaces), y compris les associations qualifiées pour exprimer les chemins d'accès;
- * 3.1 - Base de données
- P510C - Structure de la base de données
- #### P555S - Spécifications de composant logiciel
- P555C - Composante, niveau réalisateur

## Tableaux, modèles ou diagrammes recommandés

- * la traduction initiale des associations utilisateur, effectuée par l'activité P-OO-DO.1 Traduire le modèle utilisateur;
- #### Notations
- * Diagramme de classe (avec interfaces), y compris les associations qualifiées pour exprimer les chemins d'accès;
- * Diagramme de paquetage pour les dépendances.
- * Harmonisation des modèles de niveau réalisateur

## Livrables et références liés

- P540S Spécifications de la séquence réalisateur
- P-OO-DI Modélisation des interactions de niveau réalisateur
- P-OO-DO.1 Traduire le modèle utilisateur
- P490S Spécifications de l'unité de tâche
- P487S Spécifications de l'étape de tâche réutilisable
- P180S Spécifications de composante du noyau
- P186S Spécifications de composante réutilisable d'interface
- P510S - Structure de l'information persistante
- P510C - Structure de la base de données
- P555S - Spécifications de composant logiciel
- P555C - Composante, niveau réalisateur
- P-OO-UA Modélisation d'analyse utilisateur détaillée

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase G/H - Gouvernance de mise en œuvre et gestion du changement.
- Livrable TOGAF cible : Plan de transition, exploitation et adoption.
- Domaine d’architecture principal : utilisation.
- Artefacts associés : Procédure d’exploitation, Guide utilisateur, Matériel de transfert.

## Règles particulières de rédaction

- Présenter P-OO DO.2 Déterminer les références d'objet et la navigation comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique.

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Cette activité de technique détermine la nature des attributs de référence d'une classe qui activent la navigation entre les objets. Les références correspondent aux attributs réalisateur. Elles proviennent de : * l'analyse des interactions documentées dans le P540S Spécifications de la séquence réalisateur par la technique P-OO-DI Modélisation des interactions de niveau réalisateur; * la traduction initiale des associations utilisateur, effectuée par l'activité P-OO-DO.1 Traduire le modèle utilisateur; * des besoins définis par les perspectives locales de la vue utilisateur, spécifiés dans la section Perspective locale de l'unité de tâche du P490S Spécifications de l'unité de tâche, la section Perspective locale de l'étape de tâche du P487S Spécifications de l'étape de tâche réutilisable, et la section Perspective locale du service du P180S Spécifications de composante du noyau. Au besoin, une perspective locale peut être spécifiée pour un service associé à une composante d'interface utilisateur, dans les livrables P186S Spécifications de composante réutilisable d'interface, P487S Spécifications de l'étape de tâche réutilisable, et P490S Spécifications de l'unité de tâche. Cela implique la définition des éléments suivants : * chemins de navigation; * direction de navigation; * types de référence requis; * contraintes d'intégrité des liens interobjets.

### Intrants

Non disponible.

### Extrants

Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique. Les sections des livrables qui sont applicables sont montrées sous chaque livrable. Les livrables détaillés qui peuvent être utilisés au lieu des livrables succincts, ou en complément à ceux-ci, sont listés directement sous les livrables succincts concernés.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
