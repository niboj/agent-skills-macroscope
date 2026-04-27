# Référence du livrable P-OO PA Analyse architecturale des processus

## Source analysée

- Fichier source : `../../../macroscope/livrables/a8595e63b596.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

Cette technique distingue trois niveaux de processus : * les processus de système; * les processus de travail; * les unités de tâche. Elle se compose de trois activités : * créer une liste initiale de processus; * réaliser une hiérarchie de processus, en positionnant les processus de système, les processus de travail et les unités de tâche; * ébaucher les unités de tâche. En se basant sur les cas d'utilisation de niveau propriétaire déterminés un utilisant la technique P-OO-SC Définition de la portée, et sur une connaissance des processus du domaine d'affaires modélisé, P-OO-PA Analyse architecturale des processus vise l'identification et l'ébauche des unités de tâche. Les unités de tâche ébauchées sont essentielles à l'estimation et à la planification. Elles seront ensuite analysées comme des cas d'utilisation par la technique P-OO-UC Analyse détaillée de cas d'utilisation. Cette technique aide les conseiller en architectures de système d'information à trouver, à structurer et à décrire les processus en utilisant une combinaison d'approches ascendantes («bottom-up») et descendantes («top-down») : * les principaux processus d'envergure supportés par le système d'information sont un point de départ naturel, et ils correspondent souvent directement aux cas d'utilisation propriétaire. La définition des processus de système sert donc de base pour réaliser la hiérarchie des processus; * il peut arriver que certaines unités de tâche soient identifiées immédiatement, ce qui accélère la réalisation de la hiérarchie des processus en donnant une compréhension concrète de tâches à l'échelle humaine. Cette approche combinée ascendante-descendante est également reflétée dans la seconde activité (P-OO-PA.2 Construire la hiérarchie des processus). Les processus de système ou de travail sont décomposés en processus plus fins tandis que les unités de tâche et les processus de travail sont rattachés à des processus de plus haut niveau. Finalement, les unités de tâche sont ébauchées à l'aide de la troisième activité, (P-OO-PA.3 Ébaucher les unités de tâche). La position de la technique P-OO-PA Analyse architecturale des processus, par rapport aux autres techniques est illustrée dans le diagramme ci-dessous : Le contexte de la technique d'analyse architecturale des processus La technique P-OO-PA Analyse architecturale des processus est effectuée pendant les phases d'analyse préliminaire et d'architecture de système. L'architecture est également revue au début de chaque phase de conception et de réalisation d'une livraison. La technique P-OO-PA Analyse architecturale des processus s'applique aux vues propriétaire et utilisateur. Normalement, seuls les processus de système et les processus de travail ont de l'intérêt pour le propriétaire. Au fur et à mesure que les processus et les unités de tâche sont identifiés par P-OO-PA, les résultats obtenus sont utilisés par le groupe de techniques P-UID Conception de l'interface utilisateur, afin d'analyser les tâches effectuées par les utilisateurs. En particulier, les techniques suivantes sont exécutées conjointement avec P-OO-PA : * P-UIAP Orientations et principes de l'interface utilisateur * P-UIS Conception des règles de fonctionnement de l'interface utilisateur

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

- * Créer une hiérarchie de processus.
- * Décrire les processus.
- Cette technique distingue trois niveaux de processus :
- * les processus de système;
- * les processus de travail;
- * créer une liste initiale de processus;
- * réaliser une hiérarchie de processus, en positionnant les processus de système, les processus de travail et les unités de tâche;
- En se basant sur les cas d'utilisation de niveau propriétaire déterminés un utilisant la technique P-OO-SC Définition de la portée, et sur une connaissance des processus du domaine d'affaires modélisé, P-OO-PA Analyse architecturale des processus vise l'identi
- Cette technique aide les conseiller en architectures de système d'information à trouver, à structurer et à décrire les processus en utilisant une combinaison d'approches ascendantes («bottom-up») et descendantes («top-down») :
- * les principaux processus d'envergure supportés par le système d'information sont un point de départ naturel, et ils correspondent souvent directement aux cas d'utilisation propriétaire.
- La définition des processus de système sert donc de base pour réaliser la hiérarchie des processus;
- * il peut arriver que certaines unités de tâche soient identifiées immédiatement, ce qui accélère la réalisation de la hiérarchie des processus en donnant une compréhension concrète de tâches à l'échelle humaine.

## Tableaux, modèles ou diagrammes recommandés

- La position de la technique P-OO-PA Analyse architecturale des processus, par rapport aux autres techniques est illustrée dans le diagramme ci-dessous : Le contexte de la technique d'analyse architecturale des processus La technique P-OO-PA Analyse architectur
- #### Notations
- * Diagramme d'activité

## Livrables et références liés

- P-OO-SC Définition de la portée
- P-OO-PA Analyse architecturale des processus
- P-OO-UC Analyse détaillée de cas d'utilisation
- P-OO-PA.2 Construire la hiérarchie des processus
- P-OO-PA.3 Ébaucher les unités de tâche
- P-OO-PA.1 - Construire une liste initiale de processus
- P-OO-PA.2 - Construire la hiérarchie des processus
- P-OO-PA.3 - Ébaucher les unités de tâche

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase A - Vision d’architecture (Architecture Vision).
- Livrable TOGAF cible : Document de définition d’architecture (Architecture Definition Document).
- Domaine d’architecture principal : architecture métier.
- Artefacts associés : Service d’affaires (Business Service), Processus métier, Acteur ou rôle métier, Demande de travail d’architecture (Request for Architecture Work).

## Règles particulières de rédaction

- Présenter P-OO PA Analyse architecturale des processus comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- * Décrire les processus.
- Cette technique aide les conseiller en architectures de système d'information à trouver, à structurer et à décrire les processus en utilisant une combinaison d'approches ascendantes («bottom-up») et descendantes («top-down») :

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Cette technique distingue trois niveaux de processus : * les processus de système; * les processus de travail; * les unités de tâche. Elle se compose de trois activités : * créer une liste initiale de processus; * réaliser une hiérarchie de processus, en positionnant les processus de système, les processus de travail et les unités de tâche; * ébaucher les unités de tâche. En se basant sur les cas d'utilisation de niveau propriétaire déterminés un utilisant la technique P-OO-SC Définition de la portée, et sur une connaissance des processus du domaine d'affaires modélisé, P-OO-PA Analyse architecturale des processus vise l'identification et l'ébauche des unités de tâche. Les unités de tâche ébauchées sont essentielles à l'estimation et à la planification. Elles seront ensuite analysées comme des cas d'utilisation par la technique P-OO-UC Analyse détaillée de cas d'utilisation. Cette technique aide les conseiller en architectures de système d'information à trouver, à structurer et à décrire les processus en utilisant une combinaison d'approches ascendantes («bottom-up») et descendantes («top-down») : * les principaux processus d'envergure supportés par le système d'information sont un point de départ naturel, et ils correspondent souvent directement aux cas d'utilisation propriétaire. La définition des processus de système sert donc de base pour réaliser la hiérarchie des processus; * il peut arriver que certaines unités de tâche soient identifiées immédiatement, ce qui accélère la réalisation de la hiérarchie des processus en donnant une compréhension concrète de tâches à l'échelle humaine. Cette approche combinée ascendante-descendante est également reflétée dans la seconde activité (P-OO-PA.2 Construire la hiérarchie des processus). Les processus de système ou de travail sont décomposés en processus plus fins tandis que les unités de tâche et les processus de travail sont rattachés à des processus de plus haut niveau. Finalement, les unités de tâche sont ébauchées à l'aide de la troisième activité, (P-OO-PA.3 Ébaucher les unités de tâche). La position de la technique P-OO-PA Analyse architecturale des processus, par rapport aux autres techniques est illustrée dans le diagramme ci-dessous : Le contexte de la technique d'analyse architecturale des processus La technique P-OO-PA Analyse architecturale des processus est effectuée pendant les phases d'analyse préliminaire et d'architecture de système. L'architecture est également revue au début de chaque phase de conception et de réalisation d'une livraison. La technique P-OO-PA Analyse architecturale des processus s'applique aux vues propriétaire et utilisateur. Normalement, seuls les processus de système et les processus de travail ont de l'intérêt pour le propriétaire. Au fur et à mesure que les processus et les unités de tâche sont identifiés par P-OO-PA, les résultats obtenus sont utilisés par le groupe de techniques P-UID Conception de l'interface utilisateur, afin d'analyser les tâches effectuées par les utilisateurs. En particulier, les techniques suivantes sont exécutées conjointement avec P-OO-PA : * P-UIAP Orientations et principes de l'interface utilisateur * P-UIS Conception des règles de fonctionnement de l'interface utilisateur

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
