# Référence du livrable P490S Spécifications de l'unité de tâche

## Source analysée

- Fichier source : `../../../macroscope/livrables/f308c8c9b0f9.md`
- Méthode source : Macroscope
- Extraction du titre : premier lien codé du fichier

## Synthèse du livrable

Un diagramme de collaboration décrit comment un but donné peut être atteint grâce à la collaboration de plusieurs participants. Il est typiquement utilisé pour illustrer les messages qui sont échangés entre les objets (c.-à-d. les participants) à l'intérieur d'un comportement. Dans la version 1.5 de UML, de nouvelles fonctionnalités ont été ajoutées au diagramme de collaboration afin de supporter la définition de patterns de collaboration. Il y a plusieurs similarités entre un diagramme de collaboration et un diagramme de séquence. Ils peuvent être utilisés tous les deux pour représenter l'échange de messages entre les objets à l'intérieur d'un comportement. Toutefois, ils se concentrent sur différents aspects. Le diagramme de collaboration met l'accent sur les relations entre les objets, à travers lesquelles les messages sont échangés, alors que le diagramme de séquence met l'accent sur l'ordre dans lequel les messages sont échangés dans le temps. Les diagrammes de séquence et de collaboration sont utilisés pour décrire le comportement d'éléments de modèle, tels que les cas d'utilisation, les classes et les opérations. Dans son utilisation typique, un diagramme de collaboration présente des objets et les liens entre eux. Les messages qui sont échangés par les objets sont montrés au-dessus des liens. Dans la version 1.5, un diagramme de collaboration peut aussi être utilisé pour spécifier un pattern de collaboration. Les patterns sont des solutions à des problèmes de conception qui se produisent souvent. Ces solutions ont été développées et raffinées par des conseiller en architectures expérimentés et peuvent être réutilisées dans de nombreux projets. Un pattern est typiquement spécifié d'une manière générique de façon à permettre son application dans diverses situations. Il est à noter que ce qui est couramment connu sous le nom de modèles de conception (_design pattern_), tel que décrit dans [GOF95], inclut beaucoup plus que ce qui peut être spécifié en utilisant UML. Dans un diagramme de collaboration UML, un pattern de collaboration est spécifié par une entité de collaboration qui contient un ensemble de rôles qui seront joués par des objets à l'exécution, ainsi que leurs relations. Ces éléments réalisent ensemble un but particulier. Un pattern de collaboration peut aussi être appliqué à une situation spécifique et décrit dans un diagramme de collaboration par une instance du pattern. L'instance du pattern fera entrer en jeu des objets particuliers qui joueront les rôles spécifiés dans le pattern.

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

- Dans la version 1.5 de UML, de nouvelles fonctionnalités ont été ajoutées au diagramme de collaboration afin de supporter la définition de patterns de collaboration.
- Dans Solution, les diagrammes de collaboration peuvent être utilisés pour modéliser la perspective locale des unités de tâche, des étapes de tâche et des services (P490S, P487S, P180S, P186S), la séquence des composantes de niveau réalisateur (P540S), et la pe
- Ils peuvent aussi être utilisés pour modéliser les patterns de niveau utilisateur et réalisateur qui sont applicables au système à modéliser (P360S, P380S).
- Il est inutile de donner les détails de toutes les interactions des composantes d'interface utilisateur du dialogue Recherche Simple; cela se fait habituellement dans le livrable P540S Spécifications de la séquence réalisateur.
- Le pattern Observateur définit deux rôles : un observateur et un sujet.
- Les classes "Superviseur" et "Analyste" peuvent jouer le rôle de l'observateur, alors que les classes "Personne" et "Système" peuvent jouer le rôle du sujet.
- Dans l'ellipse "PatternObservateur", deux rôles sont définis : Observateur et Sujet.
- Une association connecte les deux rôles et montre par une multiplicité que plusieurs observateurs peuvent observer le sujet.
- Dans l'instance "ObservationDeGestion", un gestionnaire de carrière et un chef de projet jouent le rôle d'observateur, alors qu'un employé joue le rôle de sujet.
- Dans l'instance "ObservationD'Analyse", un conseiller en architecture de système observe un système d'information.

## Tableaux, modèles ou diagrammes recommandés

- Un diagramme de collaboration décrit comment un but donné peut être atteint grâce à la collaboration de plusieurs participants.
- Dans la version 1.5 de UML, de nouvelles fonctionnalités ont été ajoutées au diagramme de collaboration afin de supporter la définition de patterns de collaboration.
- Il y a plusieurs similarités entre un diagramme de collaboration et un diagramme de séquence.
- Le diagramme de collaboration met l'accent sur les relations entre les objets, à travers lesquelles les messages sont échangés, alors que le diagramme de séquence met l'accent sur l'ordre dans lequel les messages sont échangés dans le temps.
- Les diagrammes de séquence et de collaboration sont utilisés pour décrire le comportement d'éléments de modèle, tels que les cas d'utilisation, les classes et les opérations.
- Dans son utilisation typique, un diagramme de collaboration présente des objets et les liens entre eux.
- Dans la version 1.5, un diagramme de collaboration peut aussi être utilisé pour spécifier un pattern de collaboration.
- Il est à noter que ce qui est couramment connu sous le nom de modèles de conception (_design pattern_), tel que décrit dans [GOF95], inclut beaucoup plus que ce qui peut être spécifié en utilisant UML.
- Dans un diagramme de collaboration UML, un pattern de collaboration est spécifié par une entité de collaboration qui contient un ensemble de rôles qui seront joués par des objets à l'exécution, ainsi que leurs relations.
- Un pattern de collaboration peut aussi être appliqué à une situation spécifique et décrit dans un diagramme de collaboration par une instance du pattern.
- **Utilisation typique** Cette section décrit les éléments de notation qui sont utilisés dans l'utilisation typique d'un diagramme de collaboration, c'est-à-dire pour illustrer les messages qui sont échangés entre objets dans une collaboration.
- La table suivante présente les éléments de notation qui peuvent être utilisés pour représenter les objets.

## Livrables et références liés

- P490S Spécifications de l'unité de tâche
- P487S Spécifications de l'étape de tâche réutilisable

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase B - Architecture métier (Business Architecture).
- Livrable TOGAF cible : Document de définition d’architecture (Architecture Definition Document).
- Domaine d’architecture principal : architecture métier.
- Artefacts associés : Service d’affaires (Business Service), Processus métier, Acteur ou rôle métier.

## Règles particulières de rédaction

- Présenter P490S Spécifications de l'unité de tâche comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- Les diagrammes de séquence et de collaboration sont utilisés pour décrire le comportement d'éléments de modèle, tels que les cas d'utilisation, les classes et les opérations.
- #### Exemples
- #### Exemple 1 - Utilisation typique : Perspective locale de l'étape de tâche
- Cet exemple montre un diagramme de collaboration qui décrit la perspective locale de l'étape de tâche "Lancer une recherche simple" de l'étude de cas de la Bibliothèque ABC.
- #### Exemple 2 - Pattern de collaboration
- Cette section présente un exemple du pattern Observateur décrit dans [GAM95].
- #### Exemple 3 -

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Un diagramme de collaboration décrit comment un but donné peut être atteint grâce à la collaboration de plusieurs participants. Il est typiquement utilisé pour illustrer les messages qui sont échangés entre les objets (c.-à-d. les participants) à l'intérieur d'un comportement. Dans la version 1.5 de UML, de nouvelles fonctionnalités ont été ajoutées au diagramme de collaboration afin de supporter la définition de patterns de collaboration. Il y a plusieurs similarités entre un diagramme de collaboration et un diagramme de séquence. Ils peuvent être utilisés tous les deux pour représenter l'échange de messages entre les objets à l'intérieur d'un comportement. Toutefois, ils se concentrent sur différents aspects. Le diagramme de collaboration met l'accent sur les relations entre les objets, à travers lesquelles les messages sont échangés, alors que le diagramme de séquence met l'accent sur l'ordre dans lequel les messages sont échangés dans le temps. Les diagrammes de séquence et de collaboration sont utilisés pour décrire le comportement d'éléments de modèle, tels que les cas d'utilisation, les classes et les opérations. Dans son utilisation typique, un diagramme de collaboration présente des objets et les liens entre eux. Les messages qui sont échangés par les objets sont montrés au-dessus des liens. Dans la version 1.5, un diagramme de collaboration peut aussi être utilisé pour spécifier un pattern de collaboration. Les patterns sont des solutions à des problèmes de conception qui se produisent souvent. Ces solutions ont été développées et raffinées par des conseiller en architectures expérimentés et peuvent être réutilisées dans de nombreux projets. Un pattern est typiquement spécifié d'une manière générique de façon à permettre son application dans diverses situations. Il est à noter que ce qui est couramment connu sous le nom de modèles de conception (_design pattern_), tel que décrit dans [GOF95], inclut beaucoup plus que ce qui peut être spécifié en utilisant UML. Dans un diagramme de collaboration UML, un pattern de collaboration est spécifié par une entité de collaboration qui contient un ensemble de rôles qui seront joués par des objets à l'exécution, ainsi que leurs relations. Ces éléments réalisent ensemble un but particulier. Un pattern de collaboration peut aussi être appliqué à une situation spécifique et décrit dans un diagramme de collaboration par une instance du pattern. L'instance du pattern fera entrer en jeu des objets particuliers qui joueront les rôles spécifiés dans le pattern.

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
