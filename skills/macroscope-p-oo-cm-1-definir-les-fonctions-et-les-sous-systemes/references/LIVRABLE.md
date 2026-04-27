# Référence du livrable P-OO CM.1 Définir les fonctions et les sous-systèmes d'information

## Source analysée

- Fichier source : `../../../macroscope/livrables/ae117f2c9244.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

Cette activité de technique structure les modèles de processus en définissant des sous-ensembles de système d'information appelés sous-systèmes d'information et fonctions. Cette structure constitue un compromis entre deux aspect complémentaires : * structurel, qui tend à organiser le système d'information selon la structure des modèles d'information (c'est-à-dire en établissant des liens explicites avec les facettes et les classes clé); * dynamique, qui considère la séquence naturelle du déroulement des activités dans un processus. Cette technique se base sur une distinction entre, d'une part, les processus «centrés sur les objets» qui font la mise à jour d'une zone circonscrite du modèle d'information et, d'autre part, les processus «transversaux» qui mettent à jour plusieurs zones. Les processus centrés sur les objets sont intrinsèquement stables et peuvent être groupés en suivant la structure stable des modèles d'information. Les processus transversaux peuvent alors être regroupés séparément, ce qui permet d'isoler les parties du système d'information qui sont davantage susceptibles de changer lorsque l'organisation du travail évolue. Dans un grand système d'information, cette technique est en général appliquée de manière descendante (top-down), en définissant d'abord des sous-systèmes d'information, puis des fonctions. Par après, une approche ascendante (bottom-up) est utilisée pour réviser cette définition initiale. Quant aux systèmes plus petits, il suffit souvent d'appliquer la technique directement en mode ascendant pour définir des fonctions, et d'omettre la définition de sous-systèmes d'information.

## Raison d’être

Aucune raison d’être explicite n’a été extraite. Déduire l’intention du livrable à partir de sa description, de son contenu et des livrables liés.

## Occurrence

Aucune occurrence explicite n’a été extraite du fichier source.

## Structure détaillée du livrable

1. 1 - Structure du système d'information P200O - Structure du système d'information *
2. 1 - Description de la structure du système d'information *
3. 2 - Sous-systèmes d'information

## Champs ou sections attendus

- 1 - Structure du système d'information P200O - Structure du système d'information *
- 1 - Description de la structure du système d'information *
- 2 - Sous-systèmes d'information

## Objets documentés

- Cette activité de technique structure les modèles de processus en définissant des sous-ensembles de système d'information appelés sous-systèmes d'information et fonctions.
- * structurel, qui tend à organiser le système d'information selon la structure des modèles d'information (c'est-à-dire en établissant des liens explicites avec les facettes et les classes clé);
- * dynamique, qui considère la séquence naturelle du déroulement des activités dans un processus.
- Cette technique se base sur une distinction entre, d'une part, les processus «centrés sur les objets» qui font la mise à jour d'une zone circonscrite du modèle d'information et, d'autre part, les processus «transversaux» qui mettent à jour plusieurs zones.
- Les processus centrés sur les objets sont intrinsèquement stables et peuvent être groupés en suivant la structure stable des modèles d'information.
- Les processus transversaux peuvent alors être regroupés séparément, ce qui permet d'isoler les parties du système d'information qui sont davantage susceptibles de changer lorsque l'organisation du travail évolue.
- Dans un grand système d'information, cette technique est en général appliquée de manière descendante (top-down), en définissant d'abord des sous-systèmes d'information, puis des fonctions.
- Quant aux systèmes plus petits, il suffit souvent d'appliquer la technique directement en mode ascendant pour définir des fonctions, et d'omettre la définition de sous-systèmes d'information.
- * Les systèmes d'information, sous-systèmes d'information et fonctions sont tous des «subsystems» au sens d'UML.
- * Un système d'information est illustré comme étant un paquetage de sous-systèmes d'information.
- Chaque système d'information a un modèle d'activité («activity model») associé qui contient les diagrammes d'activité pour les processus de système.
- * Un sous-système d'information est illustré comme étant un paquetage de fonctions.

## Tableaux, modèles ou diagrammes recommandés

- Cette activité de technique structure les modèles de processus en définissant des sous-ensembles de système d'information appelés sous-systèmes d'information et fonctions.
- * structurel, qui tend à organiser le système d'information selon la structure des modèles d'information (c'est-à-dire en établissant des liens explicites avec les facettes et les classes clé);
- Cette technique se base sur une distinction entre, d'une part, les processus «centrés sur les objets» qui font la mise à jour d'une zone circonscrite du modèle d'information et, d'autre part, les processus «transversaux» qui mettent à jour plusieurs zones.
- Les processus centrés sur les objets sont intrinsèquement stables et peuvent être groupés en suivant la structure stable des modèles d'information.
- #### Notations
- Chaque système d'information a un modèle d'activité («activity model») associé qui contient les diagrammes d'activité pour les processus de système.
- Ceci s'ajoute aux autres diagrammes qui servent à illustrer sa portée (voir la technique P-OO-SC Définition de la portée).
- Chaque sous-système d'information a un modèle d'activité connexe qui contient les diagrammes de chacun des processus de travail.
- La dynamique de la fonction peut être décrite avec un Diagramme d'activité pour les unités de tâche de la fonction, mais ceci n'est normalement pas nécessaire.

## Livrables et références liés

- P-OO-SC Définition de la portée
- P200S - Structure propriétaire du système
- P200O - Structure du système d'information
- P250S - Structure utilisateur du système
- P250U - Fonction

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase A - Vision d’architecture (Architecture Vision).
- Livrable TOGAF cible : Plan de transition, exploitation et adoption.
- Domaine d’architecture principal : formation.
- Artefacts associés : Procédure d’exploitation, Guide utilisateur, Matériel de transfert, Demande de travail d’architecture (Request for Architecture Work).

## Règles particulières de rédaction

- Présenter P-OO CM.1 Définir les fonctions et les sous-systèmes d'information comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
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

Cette activité de technique structure les modèles de processus en définissant des sous-ensembles de système d'information appelés sous-systèmes d'information et fonctions. Cette structure constitue un compromis entre deux aspect complémentaires : * structurel, qui tend à organiser le système d'information selon la structure des modèles d'information (c'est-à-dire en établissant des liens explicites avec les facettes et les classes clé); * dynamique, qui considère la séquence naturelle du déroulement des activités dans un processus. Cette technique se base sur une distinction entre, d'une part, les processus «centrés sur les objets» qui font la mise à jour d'une zone circonscrite du modèle d'information et, d'autre part, les processus «transversaux» qui mettent à jour plusieurs zones. Les processus centrés sur les objets sont intrinsèquement stables et peuvent être groupés en suivant la structure stable des modèles d'information. Les processus transversaux peuvent alors être regroupés séparément, ce qui permet d'isoler les parties du système d'information qui sont davantage susceptibles de changer lorsque l'organisation du travail évolue. Dans un grand système d'information, cette technique est en général appliquée de manière descendante (top-down), en définissant d'abord des sous-systèmes d'information, puis des fonctions. Par après, une approche ascendante (bottom-up) est utilisée pour réviser cette définition initiale. Quant aux systèmes plus petits, il suffit souvent d'appliquer la technique directement en mode ascendant pour définir des fonctions, et d'omettre la définition de sous-systèmes d'information.

### Intrants

Non disponible.

### Extrants

Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique. Les sections des livrables qui sont applicables sont montrées sous chaque livrable. Les livrables détaillés qui peuvent être utilisés au lieu des livrables succincts, ou en complément à ceux-ci, sont listés directement sous les livrables succincts concernés.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
