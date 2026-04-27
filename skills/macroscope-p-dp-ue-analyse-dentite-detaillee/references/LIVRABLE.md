# Référence du livrable P-DP UE Analyse d'entité détaillée

## Source analysée

- Fichier source : `../../../macroscope/livrables/06b145990be1.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

A partir des modèles de facettes utilisateur produits par la technique P-DP-EC Classification et catégorisation des entités, cette technique modélise les entités et les relations (c'est-à-dire les composantes du noyau et de l'interface utilisateur dans la terminologie de Macroscope) requises par les unités de tâche. Il est à noter que le concept d'entité et de relation est pris ici au sens large, représentant une classe d'objets (personnes, lieux, choses...) qui sont décrits à l'aide d'attributs et de services communs. Ce concept peut être utilisé pour représenter autant une entité ou relation traditionelle (appelée aussi composante du noyau dans la terminologie de Macroscope) contenue dans un SGBD, qu'une composante d'interface utilisateur. Les composantes du noyau sont regroupées dans le modèle de facettes et les composantes d'interfaces font partie du modèle de l'interface utilisateur. La technique P-DP-UE attribue les services requis par les unités de tâches aux entités et relations (c'est-à-dire aux composantes du noyau et de l'interface utilisateur), décrit le comportement des services et définit les attributs nécessaires. Les entités qui participent au comportement d'un service sont listées dans la perspective locale du service. La modélisation des composantes d'interface utilisateur est faite de concert avec le groupe de techniques P-UID Conception de l'interface utilisateur. Ces techniques encouragent l'emploi de prototypes pour valider les composantes d'interface. Il est à noter qu'en général, seules les composantes d'interface réutilisables et les composantes d'interface clés ou représentatives nécessitent une description détaillée. Le plus souvent, des impressions d'écrans sont suffisantes et peuvent être annexées aux livrables de spécifications d'unité de tâche ou d'étape de tâche réutilisable. Activités d'analyse détaillée entités-relations

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

- * Attribuer les services aux entités et relations utilisateurs.
- * Décrire le comportement qui fournit le service.
- * Décrire la perspective locale d'un service.
- A partir des modèles de facettes utilisateur produits par la technique P-DP-EC Classification et catégorisation des entités, cette technique modélise les entités et les relations (c'est-à-dire les composantes du noyau et de l'interface utilisateur dans la term
- Il est à noter que le concept d'entité et de relation est pris ici au sens large, représentant une classe d'objets (personnes, lieux, choses...) qui sont décrits à l'aide d'attributs et de services communs.
- Ce concept peut être utilisé pour représenter autant une entité ou relation traditionelle (appelée aussi composante du noyau dans la terminologie de Macroscope) contenue dans un SGBD, qu'une composante d'interface utilisateur.
- Les composantes du noyau sont regroupées dans le modèle de facettes et les composantes d'interfaces font partie du modèle de l'interface utilisateur.
- La technique P-DP-UE attribue les services requis par les unités de tâches aux entités et relations (c'est-à-dire aux composantes du noyau et de l'interface utilisateur), décrit le comportement des services et définit les attributs nécessaires.
- Les entités qui participent au comportement d'un service sont listées dans la perspective locale du service.
- La modélisation des composantes d'interface utilisateur est faite de concert avec le groupe de techniques P-UID Conception de l'interface utilisateur.
- Ces techniques encouragent l'emploi de prototypes pour valider les composantes d'interface.
- Il est à noter qu'en général, seules les composantes d'interface réutilisables et les composantes d'interface clés ou représentatives nécessitent une description détaillée.

## Tableaux, modèles ou diagrammes recommandés

- A partir des modèles de facettes utilisateur produits par la technique P-DP-EC Classification et catégorisation des entités, cette technique modélise les entités et les relations (c'est-à-dire les composantes du noyau et de l'interface utilisateur dans la term
- Les composantes du noyau sont regroupées dans le modèle de facettes et les composantes d'interfaces font partie du modèle de l'interface utilisateur.

## Livrables et références liés

- P-DP-EC Classification et catégorisation des entités
- P-UID Conception de l'interface utilisateur
- P-DP-UE.1 - Attribuer un service à une entité ou relation utilisateur
- P-DP-UE.2 - Établir les spécifications détaillées d'un service utilisateur
- P-DP-UE.3 - Déterminer les attributs d'une entité ou relation utilisateur
- P-DP-UE.4 - Décrire la perspective locale d'un service utilisateur

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase G/H - Gouvernance de mise en œuvre et gestion du changement.
- Livrable TOGAF cible : Plan de transition, exploitation et adoption.
- Domaine d’architecture principal : utilisation.
- Artefacts associés : Procédure d’exploitation, Guide utilisateur, Matériel de transfert.

## Règles particulières de rédaction

- Présenter P-DP UE Analyse d'entité détaillée comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- * Décrire le comportement qui fournit le service.
- * Décrire la perspective locale d'un service.
- Ce concept peut être utilisé pour représenter autant une entité ou relation traditionelle (appelée aussi composante du noyau dans la terminologie de Macroscope) contenue dans un SGBD, qu'une composante d'interface utilisateur.
- * P-DP-UE.4 - Décrire la perspective locale d'un service utilisateur

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

A partir des modèles de facettes utilisateur produits par la technique P-DP-EC Classification et catégorisation des entités, cette technique modélise les entités et les relations (c'est-à-dire les composantes du noyau et de l'interface utilisateur dans la terminologie de Macroscope) requises par les unités de tâche. Il est à noter que le concept d'entité et de relation est pris ici au sens large, représentant une classe d'objets (personnes, lieux, choses...) qui sont décrits à l'aide d'attributs et de services communs. Ce concept peut être utilisé pour représenter autant une entité ou relation traditionelle (appelée aussi composante du noyau dans la terminologie de Macroscope) contenue dans un SGBD, qu'une composante d'interface utilisateur. Les composantes du noyau sont regroupées dans le modèle de facettes et les composantes d'interfaces font partie du modèle de l'interface utilisateur. La technique P-DP-UE attribue les services requis par les unités de tâches aux entités et relations (c'est-à-dire aux composantes du noyau et de l'interface utilisateur), décrit le comportement des services et définit les attributs nécessaires. Les entités qui participent au comportement d'un service sont listées dans la perspective locale du service. La modélisation des composantes d'interface utilisateur est faite de concert avec le groupe de techniques P-UID Conception de l'interface utilisateur. Ces techniques encouragent l'emploi de prototypes pour valider les composantes d'interface. Il est à noter qu'en général, seules les composantes d'interface réutilisables et les composantes d'interface clés ou représentatives nécessitent une description détaillée. Le plus souvent, des impressions d'écrans sont suffisantes et peuvent être annexées aux livrables de spécifications d'unité de tâche ou d'étape de tâche réutilisable. Activités d'analyse détaillée entités-relations

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
