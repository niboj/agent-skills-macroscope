# Référence du livrable P-OO UH.3 Revoir les responsabilités des classes

## Source analysée

- Fichier source : `../../../macroscope/livrables/0678f5cf2003.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

Pour accroître la cohérence entre les classes utilisateur, on révise leurs services par une revue systématique de type CRC des responsabilités des classes collaboratrices. Les fonctions servent à structurer le processus : tous les cas d'utilisation dans une fonction tendent à utiliser les services des mêmes classes. Il en résulte une plus grande optimisation car les services les plus utilisés tendront à provenir de l'intérieur de la fonction. Une fois ce point de départ stable établi, il est beaucoup plus facile de traiter les unités de tâche à l'extérieur de la fonction. Les perspectives locales du comportement de service d'interface et de service du noyau ainsi que des étapes de tâche sont révisées en conséquence. Revue des responsabilités des modèles utilisateur de classe Cette technique constitue en outre une vérification explicite de la cohérence, qui revoit la perspective locale des unités de tâche et des étapes de tâche, et qui vérifie si tous les services ont été attribués à des classes. Elle recherche également les classes qui ne participent pas (directement ou indirectement) à une unité de tâche ou à une étape de tâche. Elle facilite l'élimination des classes et services utilisateur qui ne sont pas requis, directement ou indirectement, par un cas d'utilisation.

## Raison d’être

Aucune raison d’être explicite n’a été extraite. Déduire l’intention du livrable à partir de sa description, de son contenu et des livrables liés.

## Occurrence

Aucune occurrence explicite n’a été extraite du fichier source.

## Structure détaillée du livrable

1. * 1.3 - Composante de la facette

## Champs ou sections attendus

- * 1.3 - Composante de la facette

## Objets documentés

- Pour accroître la cohérence entre les classes utilisateur, on révise leurs services par une revue systématique de type CRC des responsabilités des classes collaboratrices.
- Les fonctions servent à structurer le processus : tous les cas d'utilisation dans une fonction tendent à utiliser les services des mêmes classes.
- Il en résulte une plus grande optimisation car les services les plus utilisés tendront à provenir de l'intérieur de la fonction.
- Une fois ce point de départ stable établi, il est beaucoup plus facile de traiter les unités de tâche à l'extérieur de la fonction.
- Les perspectives locales du comportement de service d'interface et de service du noyau ainsi que des étapes de tâche sont révisées en conséquence.
- Revue des responsabilités des modèles utilisateur de classe Cette technique constitue en outre une vérification explicite de la cohérence, qui revoit la perspective locale des unités de tâche et des étapes de tâche, et qui vérifie si tous les services ont été
- Elle facilite l'élimination des classes et services utilisateur qui ne sont pas requis, directement ou indirectement, par un cas d'utilisation.
- * Classes d'interface et classes du noyau :
- * Définition des services d'interface et des services du noyau :
- * 1.3 - Composante de la facette
- #### P180S - Spécifications de composante du noyau
- * 1.1 - Service du noyau

## Tableaux, modèles ou diagrammes recommandés

- Revue des responsabilités des modèles utilisateur de classe Cette technique constitue en outre une vérification explicite de la cohérence, qui revoit la perspective locale des unités de tâche et des étapes de tâche, et qui vérifie si tous les services ont été
- #### Notations
- * Diagramme de classe UML
- * Diagramme de collaboration UML

## Livrables et références liés

- P170S - Structure de l'information
- P180S - Spécifications de composante du noyau
- P186S - Spécifications de composante réutilisable d'interface
- P487S - Spécifications de l'étape de tâche réutilisable
- P490S - Spécifications de l'unité de tâche

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase B - Architecture métier (Business Architecture).
- Livrable TOGAF cible : Document de définition d’architecture (Architecture Definition Document).
- Domaine d’architecture principal : architecture métier.
- Artefacts associés : Service d’affaires (Business Service), Processus métier, Acteur ou rôle métier.

## Règles particulières de rédaction

- Présenter P-OO UH.3 Revoir les responsabilités des classes comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- Les fonctions servent à structurer le processus : tous les cas d'utilisation dans une fonction tendent à utiliser les services des mêmes classes.
- Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique.

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Pour accroître la cohérence entre les classes utilisateur, on révise leurs services par une revue systématique de type CRC des responsabilités des classes collaboratrices. Les fonctions servent à structurer le processus : tous les cas d'utilisation dans une fonction tendent à utiliser les services des mêmes classes. Il en résulte une plus grande optimisation car les services les plus utilisés tendront à provenir de l'intérieur de la fonction. Une fois ce point de départ stable établi, il est beaucoup plus facile de traiter les unités de tâche à l'extérieur de la fonction. Les perspectives locales du comportement de service d'interface et de service du noyau ainsi que des étapes de tâche sont révisées en conséquence. Revue des responsabilités des modèles utilisateur de classe Cette technique constitue en outre une vérification explicite de la cohérence, qui revoit la perspective locale des unités de tâche et des étapes de tâche, et qui vérifie si tous les services ont été attribués à des classes. Elle recherche également les classes qui ne participent pas (directement ou indirectement) à une unité de tâche ou à une étape de tâche. Elle facilite l'élimination des classes et services utilisateur qui ne sont pas requis, directement ou indirectement, par un cas d'utilisation.

### Intrants

Non disponible.

### Extrants

Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique. Les sections des livrables qui sont applicables sont montrées sous chaque livrable. Les livrables détaillés qui peuvent être utilisés au lieu des livrables succincts, ou en complément à ceux-ci, sont listés directement sous les livrables succincts concernés.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
