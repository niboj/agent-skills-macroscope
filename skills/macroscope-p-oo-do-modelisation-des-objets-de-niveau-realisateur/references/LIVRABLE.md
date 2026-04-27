# Référence du livrable P-OO DO Modélisation des objets de niveau réalisateur

## Source analysée

- Fichier source : `../../../macroscope/livrables/88c0d2c7b330.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

Processus de réalisation de la modélisation d'objets Les modèles utilisateur de classe sont initialement traduits en modèle réalisateur de classes. On révise et met à jour les références d'objet et la navigation en fonction du type d'interaction requis par la technique P-OO-DI Modélisation des interactions de niveau réalisateur. On optimise les modèles de classe réalisateur en tenant compte des aspects performance et accès de volume. Enfin, on ajuste le modèle afin d'accommoder les classes qui ne participent pas directement à la vue utilisateur de l'application. En partant du contenu des livrables P170S Structure de l'information et P250S Structure utilisateur du système (P176U), définis par la technique P-OO-UO Analyse d'objet détaillée et les techniques P-UID Conception de l'interface utilisateur, cette technique traduit les classes et les associations utilisateur en modèles de classe réalisateur. Elle comprend des activités qui augmentent et améliorent les modèles de classe réalisateur avec d'autres types de classe, particulièrement ceux conçus pour coordonner l'exécution des cas d'utilisation et des transactions, ou ceux qui fournissent des interfaces à l'infrastructure technologique. La modélisation réalisateur des classes commence par les classes, les associations et les perspectives locales définies par la technique P-OO-UA Modélisation d'analyse utilisateur détaillée. Lorsqu'elle existe, la perspective locale constitue l'empreinte d'une unité de tâche, d'une étape de tâche ou d'un service dans le modèle de classe utilisateur. Initialement, les liens et attributs de niveau réalisateur sont dérivés des livrables P170S Structure de l'information, P180S Spécifications de composante du noyau, P186S Spécifications de composante réutilisable d'interface, P487S Spécifications de l'étape de tâche réutilisable, et P490S Spécifications de l'unité de tâche. Le choix des attributs est ensuite revu pour mieux répondre aux besoins des opérations et de nouveaux attributs peuvent être suggérés par la technique P-OO-DI Modélisation des interactions de niveau réalisateur. Les opérations de classe réalisateur sont d'abord dérivées des services de classes utilisateur (voir la technique P-OO-UO Analyse d'objet détaillée). De nouvelles opérations peuvent être suggérées par la technique P-OO-DI Modélisation des interactions de niveau réalisateur au cours d'une des activités suivantes : * spécification de la dynamique du séquencement réalisateur (traduction des cas d'utilisation utilisateur), documentée dans le P540S Spécifications de la séquence réalisateur); * définition des règles d'appel des opérations (signatures, préconditions et postconditions), documentées dans le P555S Spécifications de composant logiciel (P555C); * spécification détaillée de la dynamique de l'opération (soit l'interaction des objets à l'intérieur de l'opération), documentées dans le P555S Spécifications de composant logiciel (P555C). Les modèles d'état des classes qui passent par des transitions d'état importantes sont élaborés et les décisions relatives à la persistance des classes sont prises. Cette technique définit également les interfaces comme étant des groupes d'opérations publiques d'une classe, avec les protocoles connexes (contraintes d'utilisation de ces opérations, voir le livrable P555S Spécifications de composant logiciel (P560C)).

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

- * Définir les classes réalisateur et leurs interfaces.
- Processus de réalisation de la modélisation d'objets Les modèles utilisateur de classe sont initialement traduits en modèle réalisateur de classes.
- On révise et met à jour les références d'objet et la navigation en fonction du type d'interaction requis par la technique P-OO-DI Modélisation des interactions de niveau réalisateur.
- En partant du contenu des livrables P170S Structure de l'information et P250S Structure utilisateur du système (P176U), définis par la technique P-OO-UO Analyse d'objet détaillée et les techniques P-UID Conception de l'interface utilisateur, cette technique tr
- Elle comprend des activités qui augmentent et améliorent les modèles de classe réalisateur avec d'autres types de classe, particulièrement ceux conçus pour coordonner l'exécution des cas d'utilisation et des transactions, ou ceux qui fournissent des interfaces
- Lorsqu'elle existe, la perspective locale constitue l'empreinte d'une unité de tâche, d'une étape de tâche ou d'un service dans le modèle de classe utilisateur.
- Initialement, les liens et attributs de niveau réalisateur sont dérivés des livrables P170S Structure de l'information, P180S Spécifications de composante du noyau, P186S Spécifications de composante réutilisable d'interface, P487S Spécifications de l'étape de
- Les opérations de classe réalisateur sont d'abord dérivées des services de classes utilisateur (voir la technique P-OO-UO Analyse d'objet détaillée).
- * définition des règles d'appel des opérations (signatures, préconditions et postconditions), documentées dans le P555S Spécifications de composant logiciel (P555C);
- * spécification détaillée de la dynamique de l'opération (soit l'interaction des objets à l'intérieur de l'opération), documentées dans le P555S Spécifications de composant logiciel (P555C).
- Cette technique définit également les interfaces comme étant des groupes d'opérations publiques d'une classe, avec les protocoles connexes (contraintes d'utilisation de ces opérations, voir le livrable P555S Spécifications de composant logiciel (P560C)).
- Pendant la phase d'architecture de système, elle sert à élaborer les prototypes d'infrastructure et de comportement.

## Tableaux, modèles ou diagrammes recommandés

- * Traduire les modèles de classe utilisateur en modèles de classe réalisateur.
- * Optimiser les modèles réalisateur de classe et de l'information persistante.
- * Établir les aspects structurels des modèles de classe réalisateur : définition complète de l'héritage, de la délégation, de l'agrégation, de la composition, des références, etc.
- Processus de réalisation de la modélisation d'objets Les modèles utilisateur de classe sont initialement traduits en modèle réalisateur de classes.
- On optimise les modèles de classe réalisateur en tenant compte des aspects performance et accès de volume.
- Enfin, on ajuste le modèle afin d'accommoder les classes qui ne participent pas directement à la vue utilisateur de l'application.
- En partant du contenu des livrables P170S Structure de l'information et P250S Structure utilisateur du système (P176U), définis par la technique P-OO-UO Analyse d'objet détaillée et les techniques P-UID Conception de l'interface utilisateur, cette technique tr
- Elle comprend des activités qui augmentent et améliorent les modèles de classe réalisateur avec d'autres types de classe, particulièrement ceux conçus pour coordonner l'exécution des cas d'utilisation et des transactions, ou ceux qui fournissent des interfaces
- Lorsqu'elle existe, la perspective locale constitue l'empreinte d'une unité de tâche, d'une étape de tâche ou d'un service dans le modèle de classe utilisateur.
- Les modèles d'état des classes qui passent par des transitions d'état importantes sont élaborés et les décisions relatives à la persistance des classes sont prises.
- #### Notations
- * Diagramme d'état

## Livrables et références liés

- P170S Structure de l'information
- P250S Structure utilisateur du système
- P-OO-UO Analyse d'objet détaillée
- P-UID Conception de l'interface utilisateur
- P-OO-UA Modélisation d'analyse utilisateur détaillée
- P180S Spécifications de composante du noyau
- P186S Spécifications de composante réutilisable d'interface
- P487S Spécifications de l'étape de tâche réutilisable
- P490S Spécifications de l'unité de tâche
- P-OO-DI Modélisation des interactions de niveau réalisateur
- P540S Spécifications de la séquence réalisateur
- P555S Spécifications de composant logiciel
- P-OO-DO Modélisation des objets de niveau réalisateur
- P-OO-DO.1 - Traduire le modèle utilisateur
- P-OO-DO.2 - Déterminer les références d'objet et la navigation
- P-OO-DO.3 - Optimiser la navigation dans les modèles de classe réalisateur
- P-OO-DO.4 - Ajuster les modèles de classe réalisateur

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase C - Architecture des données (Data Architecture).
- Livrable TOGAF cible : Document de définition d’architecture (Architecture Definition Document).
- Domaine d’architecture principal : architecture des données.
- Artefacts associés : Entité de données, Modèle conceptuel de données, Matrice données-fonctions.

## Règles particulières de rédaction

- Présenter P-OO DO Modélisation des objets de niveau réalisateur comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- Aucune information explicite extraite du fichier source.

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Processus de réalisation de la modélisation d'objets Les modèles utilisateur de classe sont initialement traduits en modèle réalisateur de classes. On révise et met à jour les références d'objet et la navigation en fonction du type d'interaction requis par la technique P-OO-DI Modélisation des interactions de niveau réalisateur. On optimise les modèles de classe réalisateur en tenant compte des aspects performance et accès de volume. Enfin, on ajuste le modèle afin d'accommoder les classes qui ne participent pas directement à la vue utilisateur de l'application. En partant du contenu des livrables P170S Structure de l'information et P250S Structure utilisateur du système (P176U), définis par la technique P-OO-UO Analyse d'objet détaillée et les techniques P-UID Conception de l'interface utilisateur, cette technique traduit les classes et les associations utilisateur en modèles de classe réalisateur. Elle comprend des activités qui augmentent et améliorent les modèles de classe réalisateur avec d'autres types de classe, particulièrement ceux conçus pour coordonner l'exécution des cas d'utilisation et des transactions, ou ceux qui fournissent des interfaces à l'infrastructure technologique. La modélisation réalisateur des classes commence par les classes, les associations et les perspectives locales définies par la technique P-OO-UA Modélisation d'analyse utilisateur détaillée. Lorsqu'elle existe, la perspective locale constitue l'empreinte d'une unité de tâche, d'une étape de tâche ou d'un service dans le modèle de classe utilisateur. Initialement, les liens et attributs de niveau réalisateur sont dérivés des livrables P170S Structure de l'information, P180S Spécifications de composante du noyau, P186S Spécifications de composante réutilisable d'interface, P487S Spécifications de l'étape de tâche réutilisable, et P490S Spécifications de l'unité de tâche. Le choix des attributs est ensuite revu pour mieux répondre aux besoins des opérations et de nouveaux attributs peuvent être suggérés par la technique P-OO-DI Modélisation des interactions de niveau réalisateur. Les opérations de classe réalisateur sont d'abord dérivées des services de classes utilisateur (voir la technique P-OO-UO Analyse d'objet détaillée). De nouvelles opérations peuvent être suggérées par la technique P-OO-DI Modélisation des interactions de niveau réalisateur au cours d'une des activités suivantes : * spécification de la dynamique du séquencement réalisateur (traduction des cas d'utilisation utilisateur), documentée dans le P540S Spécifications de la séquence réalisateur); * définition des règles d'appel des opérations (signatures, préconditions et postconditions), documentées dans le P555S Spécifications de composant logiciel (P555C); * spécification détaillée de la dynamique de l'opération (soit l'interaction des objets à l'intérieur de l'opération), documentées dans le P555S Spécifications de composant logiciel (P555C). Les modèles d'état des classes qui passent par des transitions d'état importantes sont élaborés et les décisions relatives à la persistance des classes sont prises. Cette technique définit également les interfaces comme étant des groupes d'opérations publiques d'une classe, avec les protocoles connexes (contraintes d'utilisation de ces opérations, voir le livrable P555S Spécifications de composant logiciel (P560C)).

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
