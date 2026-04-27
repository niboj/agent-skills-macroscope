# Référence du livrable P-OO DO.3 Optimiser la navigation dans les modèles de classe réalisateur

## Source analysée

- Fichier source : `../../../macroscope/livrables/6beba47352a0.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

L'optimisation de la navigation à l'intérieur du modèle de classe réalisateur est un facteur clé pour atteindre les objectifs de qualité du système. Cette optimisation est particulièrement importante lorsque les critères de performances sont rigoureux et que les ressources techniques sont limitées par rapport au volume de transactions ainsi qu'à la fréquence et à la complexité des collaborations d'objet. Les objectifs de l'optimisation sont les suivants : * respecter les critères de qualité des cas d'utilisation; * réduire au minimum le temps de réponse ou de calcul; * réduire au minimum le coût total des accès; * réduire au minimum la complexité du développement et de la maintenance du système. Le livrable P510S Structure de l'information persistante (P460C) décrit comment optimiser le sous-ensemble permanent des modèles de classe réalisateur. Celui-ci est développé en transformant la traduction initiale en une traduction satisfaisant aux critères de qualité spécifiés dans le modèle de processus de la vue utilisateur. Le modèle est optimisé afin de satisfaire aux critères de performances anticipés, à l'aide de l'information provenant de la vue utilisateur de l'information et des processus, des critères de qualité, des normes et des configurations utilisateur d'infrastructure (voir la directive «Stratégies d'amélioration de la navigation des modèles de classe»). Les transformations subséquentes dépendent du type de base de données sélectionné par le projet (SGBDR, SGBDO, etc.). Le même processus est utilisé pour chaque sous-système défini dans le P219S Architecture logicielle (P219C). Dans le cas des sous-systèmes du noyau, cela correspond à l'optimisation des éléments non persistants.

## Raison d’être

Aucune raison d’être explicite n’a été extraite. Déduire l’intention du livrable à partir de sa description, de son contenu et des livrables liés.

## Occurrence

Aucune occurrence explicite n’a été extraite du fichier source.

## Structure détaillée du livrable

1. 2 - Optimisation des bases de données * 3.1 - Base de données P460C - Optimisation de l'information persistante *
2. 1 - Optimisation de l'information persistante * 2.1.2.1 - Attribut P510C - Structure de la base de données * 2.1.2 - Attributs de l'enregistrement ou de la table

## Champs ou sections attendus

- 2 - Optimisation des bases de données * 3.1 - Base de données P460C - Optimisation de l'information persistante *
- 1 - Optimisation de l'information persistante * 2.1.2.1 - Attribut P510C - Structure de la base de données * 2.1.2 - Attributs de l'enregistrement ou de la table

## Objets documentés

- L'optimisation de la navigation à l'intérieur du modèle de classe réalisateur est un facteur clé pour atteindre les objectifs de qualité du système.
- * réduire au minimum la complexité du développement et de la maintenance du système.
- Celui-ci est développé en transformant la traduction initiale en une traduction satisfaisant aux critères de qualité spécifiés dans le modèle de processus de la vue utilisateur.
- Le modèle est optimisé afin de satisfaire aux critères de performances anticipés, à l'aide de l'information provenant de la vue utilisateur de l'information et des processus, des critères de qualité, des normes et des configurations utilisateur d'infrastructur
- Les transformations subséquentes dépendent du type de base de données sélectionné par le projet (SGBDR, SGBDO, etc.).
- Le même processus est utilisé pour chaque sous-système défini dans le P219S Architecture logicielle (P219C).
- Dans le cas des sous-systèmes du noyau, cela correspond à l'optimisation des éléments non persistants.
- - Optimisation des bases de données
- * 3.1 - Base de données
- P510C - Structure de la base de données
- #### P555S - Spécifications de composant logiciel
- P555C - Composante, niveau réalisateur

## Tableaux, modèles ou diagrammes recommandés

- L'optimisation de la navigation à l'intérieur du modèle de classe réalisateur est un facteur clé pour atteindre les objectifs de qualité du système.
- Le livrable P510S Structure de l'information persistante (P460C) décrit comment optimiser le sous-ensemble permanent des modèles de classe réalisateur.
- Celui-ci est développé en transformant la traduction initiale en une traduction satisfaisant aux critères de qualité spécifiés dans le modèle de processus de la vue utilisateur.
- Le modèle est optimisé afin de satisfaire aux critères de performances anticipés, à l'aide de l'information provenant de la vue utilisateur de l'information et des processus, des critères de qualité, des normes et des configurations utilisateur d'infrastructur
- #### Notations
- * Diagramme de classe
- * Diagramme de paquetage
- * Harmonisation des modèles de niveau réalisateur

## Livrables et références liés

- P510S Structure de l'information persistante
- P219S Architecture logicielle
- P510S - Structure de l'information persistante
- P460C - Optimisation de l'information persistante
- P510C - Structure de la base de données
- P555S - Spécifications de composant logiciel
- P555C - Composante, niveau réalisateur
- P-OO-UA Modélisation d'analyse utilisateur détaillée

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase A - Vision d’architecture (Architecture Vision).
- Livrable TOGAF cible : Document de définition d’architecture (Architecture Definition Document).
- Domaine d’architecture principal : architecture des données.
- Artefacts associés : Entité de données, Modèle conceptuel de données, Matrice données-fonctions, Demande de travail d’architecture (Request for Architecture Work).

## Règles particulières de rédaction

- Présenter P-OO DO.3 Optimiser la navigation dans les modèles de classe réalisateur comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
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

L'optimisation de la navigation à l'intérieur du modèle de classe réalisateur est un facteur clé pour atteindre les objectifs de qualité du système. Cette optimisation est particulièrement importante lorsque les critères de performances sont rigoureux et que les ressources techniques sont limitées par rapport au volume de transactions ainsi qu'à la fréquence et à la complexité des collaborations d'objet. Les objectifs de l'optimisation sont les suivants : * respecter les critères de qualité des cas d'utilisation; * réduire au minimum le temps de réponse ou de calcul; * réduire au minimum le coût total des accès; * réduire au minimum la complexité du développement et de la maintenance du système. Le livrable P510S Structure de l'information persistante (P460C) décrit comment optimiser le sous-ensemble permanent des modèles de classe réalisateur. Celui-ci est développé en transformant la traduction initiale en une traduction satisfaisant aux critères de qualité spécifiés dans le modèle de processus de la vue utilisateur. Le modèle est optimisé afin de satisfaire aux critères de performances anticipés, à l'aide de l'information provenant de la vue utilisateur de l'information et des processus, des critères de qualité, des normes et des configurations utilisateur d'infrastructure (voir la directive «Stratégies d'amélioration de la navigation des modèles de classe»). Les transformations subséquentes dépendent du type de base de données sélectionné par le projet (SGBDR, SGBDO, etc.). Le même processus est utilisé pour chaque sous-système défini dans le P219S Architecture logicielle (P219C). Dans le cas des sous-systèmes du noyau, cela correspond à l'optimisation des éléments non persistants.

### Intrants

Non disponible.

### Extrants

Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique. Les sections des livrables qui sont applicables sont montrées sous chaque livrable. Les livrables détaillés qui peuvent être utilisés au lieu des livrables succincts, ou en complément à ceux-ci, sont listés directement sous les livrables succincts concernés.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
