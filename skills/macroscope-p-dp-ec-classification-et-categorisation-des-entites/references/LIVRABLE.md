# Référence du livrable P-DP EC Classification et catégorisation des entités

## Source analysée

- Fichier source : `../../../macroscope/livrables/6f7077f8a092.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

Les systèmes d'information comportent en général un grand nombre d'entités et de relations. Pour faciliter leur analyse, ces entités et relations du domaine d'intérêt sont organisées par affinité sémantique en facettes (telles que les «commandes» ou les «clients»). Les facettes sont aussi organisées et regroupées par affinité sémantique en sujets (des catégories d'entités et de relations par domaine à grande échelle telles que la «comptabilité» ou les «ressources humaines»). Les sujets, les facettes, les entités et les relations forment une hiérarchie à trois niveaux. Le premier niveau, les sujets, est typiquement ébauché lors de la définition de la portée du système d'information. Cette technique aide à découvrir les deux autres niveaux, à savoir les facettes et les entités. Elle se base sur une approche mixte, ascendante («bottom-up») et descendante («top-down») qui peut comprendre, à un moment quelconque, en combinaison : * identification et définition de facettes se basant sur les entités et relations connues (approche ascendante) ou sur une partition du sujet (approche descendante); * identification et définition d'entités et de relations se basant sur le contenu attendu d'une facette (approche descendante) ou sur une analyse directe des entités et relations manipulées par les traitements (approche ascendante). Une approche descendante est habituelle quand le domaine d'affaires modélisé est peu connu tandis que l'inverse peut être vrai si le sujet nous est familier. Trois activités fortement couplées composent cette technique : * définir les facettes; * identifier et catégoriser les entités et les relations; * ébaucher les entités et les relations. Il est à noter que, parallèlement à la technique P-DP-EC, la technique P-UIS Conception des règles de fonctionnement de l'interface utilisateur établit les catégories de composantes d'interface utilisateur à partir desquelles les composantes d'interface seront conçues, et modélise les composantes d'interface clés. Contexte de la technique de classification et de catégorisation des entités Cette technique est largement utilisée durant les phases d'analyse préliminaire et d'architecture de système. Au cours de la phase d'analyse préliminaire, on met l'accent sur les deux premières activités et au cours de la phase d'architecture de système, sur les deux dernières activités. Il faut s'attendre à des rajustements dans la phase de conception et de réalisation d'une livraison. Cette technique est essentiellement de niveau utilisateur.

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

- * Définir le vocabulaire du système.
- Les systèmes d'information comportent en général un grand nombre d'entités et de relations.
- Pour faciliter leur analyse, ces entités et relations du domaine d'intérêt sont organisées par affinité sémantique en facettes (telles que les «commandes» ou les «clients»).
- Les facettes sont aussi organisées et regroupées par affinité sémantique en sujets (des catégories d'entités et de relations par domaine à grande échelle telles que la «comptabilité» ou les «ressources humaines»).
- Les sujets, les facettes, les entités et les relations forment une hiérarchie à trois niveaux.
- Le premier niveau, les sujets, est typiquement ébauché lors de la définition de la portée du système d'information.
- Cette technique aide à découvrir les deux autres niveaux, à savoir les facettes et les entités.
- * identification et définition de facettes se basant sur les entités et relations connues (approche ascendante) ou sur une partition du sujet (approche descendante);
- * identification et définition d'entités et de relations se basant sur le contenu attendu d'une facette (approche descendante) ou sur une analyse directe des entités et relations manipulées par les traitements (approche ascendante).
- Une approche descendante est habituelle quand le domaine d'affaires modélisé est peu connu tandis que l'inverse peut être vrai si le sujet nous est familier.
- * définir les facettes;
- Il est à noter que, parallèlement à la technique P-DP-EC, la technique P-UIS Conception des règles de fonctionnement de l'interface utilisateur établit les catégories de composantes d'interface utilisateur à partir desquelles les composantes d'interface seront

## Tableaux, modèles ou diagrammes recommandés

- #### Notations
- * Diagramme entités-relations

## Livrables et références liés

- P-UIS Conception des règles de fonctionnement de l'interface utilisateur
- P-DP-EC.1 - Définir les facettes
- P-DP-EC.2 - Identifier et catégoriser les entités et relations
- P-DP-EC.3 - Ébaucher les entités et les relations

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase A - Vision d’architecture (Architecture Vision).
- Livrable TOGAF cible : Document de définition d’architecture (Architecture Definition Document).
- Domaine d’architecture principal : architecture des données.
- Artefacts associés : Entité de données, Modèle conceptuel de données, Matrice données-fonctions, Demande de travail d’architecture (Request for Architecture Work).

## Règles particulières de rédaction

- Présenter P-DP EC Classification et catégorisation des entités comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
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

Les systèmes d'information comportent en général un grand nombre d'entités et de relations. Pour faciliter leur analyse, ces entités et relations du domaine d'intérêt sont organisées par affinité sémantique en facettes (telles que les «commandes» ou les «clients»). Les facettes sont aussi organisées et regroupées par affinité sémantique en sujets (des catégories d'entités et de relations par domaine à grande échelle telles que la «comptabilité» ou les «ressources humaines»). Les sujets, les facettes, les entités et les relations forment une hiérarchie à trois niveaux. Le premier niveau, les sujets, est typiquement ébauché lors de la définition de la portée du système d'information. Cette technique aide à découvrir les deux autres niveaux, à savoir les facettes et les entités. Elle se base sur une approche mixte, ascendante («bottom-up») et descendante («top-down») qui peut comprendre, à un moment quelconque, en combinaison : * identification et définition de facettes se basant sur les entités et relations connues (approche ascendante) ou sur une partition du sujet (approche descendante); * identification et définition d'entités et de relations se basant sur le contenu attendu d'une facette (approche descendante) ou sur une analyse directe des entités et relations manipulées par les traitements (approche ascendante). Une approche descendante est habituelle quand le domaine d'affaires modélisé est peu connu tandis que l'inverse peut être vrai si le sujet nous est familier. Trois activités fortement couplées composent cette technique : * définir les facettes; * identifier et catégoriser les entités et les relations; * ébaucher les entités et les relations. Il est à noter que, parallèlement à la technique P-DP-EC, la technique P-UIS Conception des règles de fonctionnement de l'interface utilisateur établit les catégories de composantes d'interface utilisateur à partir desquelles les composantes d'interface seront conçues, et modélise les composantes d'interface clés. Contexte de la technique de classification et de catégorisation des entités Cette technique est largement utilisée durant les phases d'analyse préliminaire et d'architecture de système. Au cours de la phase d'analyse préliminaire, on met l'accent sur les deux premières activités et au cours de la phase d'architecture de système, sur les deux dernières activités. Il faut s'attendre à des rajustements dans la phase de conception et de réalisation d'une livraison. Cette technique est essentiellement de niveau utilisateur.

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
