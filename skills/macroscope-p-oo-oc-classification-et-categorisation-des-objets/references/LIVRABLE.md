# Référence du livrable P-OO OC Classification et catégorisation des objets

## Source analysée

- Fichier source : `../../../macroscope/livrables/d99bf6fc45de.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

Les systèmes d'information comportent en général un grand nombre de classes. Pour faciliter leur analyse, ces classes du domaine d'intérêt sont organisées par affinité sémantique en facettes (telles que les «commandes» ou les «clients»), et en sujets (des catégories de classes par domaine à grande échelle tel que la «comptabilité» ou les «ressources humaines»). Les sujets, les facettes et les classes forment une hiérarchie à trois niveaux. Le premier niveau, les sujets, est typiquement ébauché lors de la définition de la portée du système d'information. Cette technique aide à découvrir les deux autres niveaux, à savoir les facettes et les classes. Elle est basée sur une approche mixte, ascendante («bottom-up») et descendante («top-down») qui peut comprendre, à un moment quelconque, la combinaison suivante : * identification et définition de facettes basées sur les classes connues (approche ascendante) ou sur une partition du sujet (approche descendante); * identification et de définition de classes basée sur le contenu attendu d'une facette (approche descendante) ou sur une analyse directe des processus (approche ascendante). Une approche descendante est habituelle quand le domaine d'affaires modélisé est peu connu tandis que l'inverse peut être vrai si le sujet nous est familier. Trois activités fortement couplées composent cette technique : * définir les facettes; * identifier et catégoriser les classes et les associations; * ébaucher les classes et les associations. Cette technique est largement utilisée durant les phases d'analyse préliminaire et d'architecture de système. Dans la phase d'analyse préliminaire, l'accent porte sur les deux premières activités et dans la phase d'architecture de système, sur les deux dernières activités. Il faut s'attendre à des rajustements durant la phase de conception et de réalisation d'une livraison. Il est à noter que les classes d'interface utilisateur ne sont pas considérées par la technique OO-OC. La technique P-UIS Conception des règles de fonctionnement de l'interface utilisateur, qui est exécutée conjointement avec la technique OO-OC, établit les catégories de classes d'interface utilisateur à partir desquelles les classes d'interface seront conçues, et modélise les classes d'interface clés. Le contexte de la technique de classification et de catégorisation des objets Cette technique est essentiellement de niveau utilisateur.

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
- Les systèmes d'information comportent en général un grand nombre de classes.
- Pour faciliter leur analyse, ces classes du domaine d'intérêt sont organisées par affinité sémantique en facettes (telles que les «commandes» ou les «clients»), et en sujets (des catégories de classes par domaine à grande échelle tel que la «comptabilité» ou l
- Les sujets, les facettes et les classes forment une hiérarchie à trois niveaux.
- Le premier niveau, les sujets, est typiquement ébauché lors de la définition de la portée du système d'information.
- Cette technique aide à découvrir les deux autres niveaux, à savoir les facettes et les classes.
- * identification et définition de facettes basées sur les classes connues (approche ascendante) ou sur une partition du sujet (approche descendante);
- * identification et de définition de classes basée sur le contenu attendu d'une facette (approche descendante) ou sur une analyse directe des processus (approche ascendante).
- Une approche descendante est habituelle quand le domaine d'affaires modélisé est peu connu tandis que l'inverse peut être vrai si le sujet nous est familier.
- * définir les facettes;
- Cette technique est largement utilisée durant les phases d'analyse préliminaire et d'architecture de système.
- Dans la phase d'analyse préliminaire, l'accent porte sur les deux premières activités et dans la phase d'architecture de système, sur les deux dernières activités.

## Tableaux, modèles ou diagrammes recommandés

- #### Notations
- * Diagramme de classe
- * Diagramme de paquetage

## Livrables et références liés

- P-OO-OC.1 - Définir les facettes
- P-OO-OC.2 - Identifier et catégoriser les classes et les associations
- P-OO-OC.3 - Ébaucher les classes et les associations

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase A - Vision d’architecture (Architecture Vision).
- Livrable TOGAF cible : Document de définition d’architecture (Architecture Definition Document).
- Domaine d’architecture principal : architecture des données.
- Artefacts associés : Entité de données, Modèle conceptuel de données, Matrice données-fonctions, Demande de travail d’architecture (Request for Architecture Work).

## Règles particulières de rédaction

- Présenter P-OO OC Classification et catégorisation des objets comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
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

Les systèmes d'information comportent en général un grand nombre de classes. Pour faciliter leur analyse, ces classes du domaine d'intérêt sont organisées par affinité sémantique en facettes (telles que les «commandes» ou les «clients»), et en sujets (des catégories de classes par domaine à grande échelle tel que la «comptabilité» ou les «ressources humaines»). Les sujets, les facettes et les classes forment une hiérarchie à trois niveaux. Le premier niveau, les sujets, est typiquement ébauché lors de la définition de la portée du système d'information. Cette technique aide à découvrir les deux autres niveaux, à savoir les facettes et les classes. Elle est basée sur une approche mixte, ascendante («bottom-up») et descendante («top-down») qui peut comprendre, à un moment quelconque, la combinaison suivante : * identification et définition de facettes basées sur les classes connues (approche ascendante) ou sur une partition du sujet (approche descendante); * identification et de définition de classes basée sur le contenu attendu d'une facette (approche descendante) ou sur une analyse directe des processus (approche ascendante). Une approche descendante est habituelle quand le domaine d'affaires modélisé est peu connu tandis que l'inverse peut être vrai si le sujet nous est familier. Trois activités fortement couplées composent cette technique : * définir les facettes; * identifier et catégoriser les classes et les associations; * ébaucher les classes et les associations. Cette technique est largement utilisée durant les phases d'analyse préliminaire et d'architecture de système. Dans la phase d'analyse préliminaire, l'accent porte sur les deux premières activités et dans la phase d'architecture de système, sur les deux dernières activités. Il faut s'attendre à des rajustements durant la phase de conception et de réalisation d'une livraison. Il est à noter que les classes d'interface utilisateur ne sont pas considérées par la technique OO-OC. La technique P-UIS Conception des règles de fonctionnement de l'interface utilisateur, qui est exécutée conjointement avec la technique OO-OC, établit les catégories de classes d'interface utilisateur à partir desquelles les classes d'interface seront conçues, et modélise les classes d'interface clés. Le contexte de la technique de classification et de catégorisation des objets Cette technique est essentiellement de niveau utilisateur.

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
