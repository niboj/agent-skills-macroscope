# Référence du livrable P-OO DA Modélisation de l'architecture de niveau réalisateur

## Source analysée

- Fichier source : `../../../macroscope/livrables/37c139e8a1ed.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

Les applications de systèmes d'information comportent généralement un grand nombre de classes. Pour faciliter l'analyse, la conception et la réalisation de l'application, cette technique regroupe les composants logiciels et les classes réalisateur qui les composent en sous-systèmes réalisateur. Ce regroupement facilite le développement par incrément et la maintenance des applications en morcelant un gros système en plusieurs sous-systèmes plus petits. Les sous-systèmes sont identifiés sur deux axes : * en premier lieu, les couches permettent de séparer les portions stables de l'application (comme les interrogations) de celles qui sont plus susceptibles d'évoluer (comme l'interface); * le long du deuxième axe, les sections servent à isoler les portions liées à la technologie des portions axées sur l'application, qui devraient demeurer indépendantes de la technologie. L'architecture des sections axées sur l'application est influencée par les cas d'utilisation et les modèles utilisateur alors que les sections axées sur la technologie ont tendance à être organisées différemment. Chaque sous-système est défini par les couches et les sections qu'il couvre. La définition des couches et des sections ne suit pas une série de règles prédéfinies. Différents systèmes d'information peuvent se caractériser par des structures de sous-systèmes différentes. Plusieurs facteurs, dont les normes de l'entreprise relativement à la technologie, l'environnement de développement ou l'utilisation d'armature d'application, peuvent influer sur la structure. Cette technique s'applique à la vue réalisateur et sert à modéliser l'architecture réalisateur. Activités des techniques de modélisation de l'architecture réalisateur Cette technique est composée de trois activités (illustrées par des roues dentées) qui identifient les sous-systèmes et en définissent le contenu et les interactions. La relation avec les techniques utilisateur est aussi indiquée. Cette technique examine : * le contenu des modèles utilisateur (fonctions, catégories de l'interface et facettes); * les normes et modèles réalisateur existants; * les normes technologiques existantes; * les modèles de répartition. À partir de ces éléments, elle définit une structure de sous-systèmes réalisateur distincte à l'appui des modèles utilisateur. Les protocoles et les interfaces publiques sont définis pour chaque sous-système réalisateur.

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

- * Placer les sous-systèmes réalisateur en couches.
- * Regrouper les composants logiciels et les classes réalisateur qui les composent en sous-systèmes réalisateur.
- Les applications de systèmes d'information comportent généralement un grand nombre de classes.
- Pour faciliter l'analyse, la conception et la réalisation de l'application, cette technique regroupe les composants logiciels et les classes réalisateur qui les composent en sous-systèmes réalisateur.
- Ce regroupement facilite le développement par incrément et la maintenance des applications en morcelant un gros système en plusieurs sous-systèmes plus petits.
- Les sous-systèmes sont identifiés sur deux axes :
- * en premier lieu, les couches permettent de séparer les portions stables de l'application (comme les interrogations) de celles qui sont plus susceptibles d'évoluer (comme l'interface);
- Chaque sous-système est défini par les couches et les sections qu'il couvre.
- La définition des couches et des sections ne suit pas une série de règles prédéfinies.
- Différents systèmes d'information peuvent se caractériser par des structures de sous-systèmes différentes.
- Activités des techniques de modélisation de l'architecture réalisateur Cette technique est composée de trois activités (illustrées par des roues dentées) qui identifient les sous-systèmes et en définissent le contenu et les interactions.
- * le contenu des modèles utilisateur (fonctions, catégories de l'interface et facettes);

## Tableaux, modèles ou diagrammes recommandés

- * Faire correspondre les modèles utilisateur à une structure tenant compte des contraintes supplémentaires.
- L'architecture des sections axées sur l'application est influencée par les cas d'utilisation et les modèles utilisateur alors que les sections axées sur la technologie ont tendance à être organisées différemment.
- * le contenu des modèles utilisateur (fonctions, catégories de l'interface et facettes);
- * les normes et modèles réalisateur existants;
- * les modèles de répartition.
- À partir de ces éléments, elle définit une structure de sous-systèmes réalisateur distincte à l'appui des modèles utilisateur.
- #### Notations
- * Diagramme d'état
- * Diagramme de classe
- * Diagramme de paquetage
- À ce stade, l'application de la technique est fortement intuitive et repose sur des modèles utilisateur encore très partiels.
- * Dans la phase de conception et de réalisation d'une livraison, la technique permet d'établir les spécifications détaillées de chaque sous-système réalisateur, de concert avec la technique P-OO-DO Modélisation des objets de niveau réalisateur qui produit les

## Livrables et références liés

- P-OO-DA Modélisation de l'architecture de niveau réalisateur
- P-OO-DO Modélisation des objets de niveau réalisateur
- P-OO-DA.1 - Définir l'architecture de sous-systèmes, niveau réalisateur
- P-OO-DA.2 - Définir un sous-système réalisateur
- P-OO-DA.3 - Définir une interface d'un sous-système réalisateur

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase C - Architecture applicative (Application Architecture).
- Livrable TOGAF cible : Document de définition d’architecture (Architecture Definition Document).
- Domaine d’architecture principal : architecture applicative.
- Artefacts associés : Composant applicatif logique (Logical Application Component), Interface applicative, Bloc constitutif de solution (Solution Building Block).

## Règles particulières de rédaction

- Présenter P-OO DA Modélisation de l'architecture de niveau réalisateur comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
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

Les applications de systèmes d'information comportent généralement un grand nombre de classes. Pour faciliter l'analyse, la conception et la réalisation de l'application, cette technique regroupe les composants logiciels et les classes réalisateur qui les composent en sous-systèmes réalisateur. Ce regroupement facilite le développement par incrément et la maintenance des applications en morcelant un gros système en plusieurs sous-systèmes plus petits. Les sous-systèmes sont identifiés sur deux axes : * en premier lieu, les couches permettent de séparer les portions stables de l'application (comme les interrogations) de celles qui sont plus susceptibles d'évoluer (comme l'interface); * le long du deuxième axe, les sections servent à isoler les portions liées à la technologie des portions axées sur l'application, qui devraient demeurer indépendantes de la technologie. L'architecture des sections axées sur l'application est influencée par les cas d'utilisation et les modèles utilisateur alors que les sections axées sur la technologie ont tendance à être organisées différemment. Chaque sous-système est défini par les couches et les sections qu'il couvre. La définition des couches et des sections ne suit pas une série de règles prédéfinies. Différents systèmes d'information peuvent se caractériser par des structures de sous-systèmes différentes. Plusieurs facteurs, dont les normes de l'entreprise relativement à la technologie, l'environnement de développement ou l'utilisation d'armature d'application, peuvent influer sur la structure. Cette technique s'applique à la vue réalisateur et sert à modéliser l'architecture réalisateur. Activités des techniques de modélisation de l'architecture réalisateur Cette technique est composée de trois activités (illustrées par des roues dentées) qui identifient les sous-systèmes et en définissent le contenu et les interactions. La relation avec les techniques utilisateur est aussi indiquée. Cette technique examine : * le contenu des modèles utilisateur (fonctions, catégories de l'interface et facettes); * les normes et modèles réalisateur existants; * les normes technologiques existantes; * les modèles de répartition. À partir de ces éléments, elle définit une structure de sous-systèmes réalisateur distincte à l'appui des modèles utilisateur. Les protocoles et les interfaces publiques sont définis pour chaque sous-système réalisateur.

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
