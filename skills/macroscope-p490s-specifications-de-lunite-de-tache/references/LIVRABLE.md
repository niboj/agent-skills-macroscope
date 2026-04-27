# Référence du livrable P490S Spécifications de l'unité de tâche

## Source analysée

- Fichier source : `../../../macroscope/livrables/a277f12bcc92.md`
- Méthode source : Macroscope
- Extraction du titre : premier lien codé du fichier

## Synthèse du livrable

Il y a plusieurs similarités entre un diagramme de collaboration et un diagramme de séquence. Ils peuvent être utilisés tous les deux pour représenter l'échange de messages entre les objets à l'intérieur d'un comportement. Toutefois, ils se concentrent sur différents aspects. Le diagramme de séquence met l'accent sur l'ordre dans lequel les messages sont échangés dans le temps, alors que le diagramme de collaboration met l'accent sur les relations entre les objets, à travers lesquelles les messages sont échangés. Les diagrammes de séquence et de collaboration sont utilisés pour décrire le comportement d'éléments de modèle, tels que les cas d'utilisation, les classes et les opérations. Un diagramme de séquence a deux dimensions. La dimension horizontale montre les participants dans l'interaction, alors que la dimension verticale représente le temps et montre les messages qui sont échangés à travers le temps. Les participants sont représentés dans la partie supérieure du diagramme. Chaque participant possède une ligne de vie qui s'étend vers le bas et qui illustre sa durée de vie. Les participants s'envoient des messages entre eux. Un message connecte deux moments dans le temps (c.-à-d. deux événements), l'un se produisant sur la ligne de vie du participant émetteur du message, et l'autre se produisant sur la ligne de vie du participant récepteur du message. Généralement, un diagramme de séquence représente un seul scénario. Toutefois, il peut aussi être utilisé d'une façon plus abstraite pour exprimer tous les scénarios possibles.

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

- Dans Solution, les diagrammes de séquence peuvent être utilisés pour modéliser la perspective locale des unités de tâche, des étapes de tâche et des services (P490S, P487S, P180S, P186S), la séquence des composantes de niveau réalisateur (P540S) et la perspect
- Il est inutile de donner les détails de toutes les interactions des composantes d'interface utilisateur du dialogue Recherche Simple; cela se fait habituellement dans le livrable P540S Spécifications de la séquence réalisateur.

## Tableaux, modèles ou diagrammes recommandés

- Il y a plusieurs similarités entre un diagramme de collaboration et un diagramme de séquence.
- Le diagramme de séquence met l'accent sur l'ordre dans lequel les messages sont échangés dans le temps, alors que le diagramme de collaboration met l'accent sur les relations entre les objets, à travers lesquelles les messages sont échangés.
- Les diagrammes de séquence et de collaboration sont utilisés pour décrire le comportement d'éléments de modèle, tels que les cas d'utilisation, les classes et les opérations.
- Un diagramme de séquence a deux dimensions.
- Les participants sont représentés dans la partie supérieure du diagramme.
- Généralement, un diagramme de séquence représente un seul scénario.
- La table ci-dessous présente les éléments de notation pouvant être utilisés dans un diagramme de séquence.
- Des contraintes de temps peuvent être spécifiées dans un diagramme de séquence.
- D'autres éléments de notation peuvent aussi être spécifiés (voir la section Éléments de notation généraux).
- Dans Solution, les diagrammes de séquence peuvent être utilisés pour modéliser la perspective locale des unités de tâche, des étapes de tâche et des services (P490S, P487S, P180S, P186S), la séquence des composantes de niveau réalisateur (P540S) et la perspect
- Voir la table des stéréotypes UML de Solution pour la liste des stéréotypes pouvant être utilisés dans un diagramme de séquence.
- #### Exemple 1 - Exemple de diagramme de séquence

## Livrables et références liés

- P490S Spécifications de l'unité de tâche
- P487S Spécifications de l'étape de tâche réutilisable
- P540S Spécifications de la séquence réalisateur

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase G/H - Gouvernance de mise en œuvre et gestion du changement.
- Livrable TOGAF cible : Plan de transition, exploitation et adoption.
- Domaine d’architecture principal : utilisation.
- Artefacts associés : Procédure d’exploitation, Guide utilisateur, Matériel de transfert.

## Règles particulières de rédaction

- Présenter P490S Spécifications de l'unité de tâche comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- Les diagrammes de séquence et de collaboration sont utilisés pour décrire le comportement d'éléments de modèle, tels que les cas d'utilisation, les classes et les opérations.
- #### Exemples
- #### Exemple 1 - Exemple de diagramme de séquence
- Cet exemple montre un diagramme de séquence qui décrit la perspective locale de l'étape de tâche "Lancer une recherche simple" de l'étude de cas de la Bibliothèque ABC.

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Il y a plusieurs similarités entre un diagramme de collaboration et un diagramme de séquence. Ils peuvent être utilisés tous les deux pour représenter l'échange de messages entre les objets à l'intérieur d'un comportement. Toutefois, ils se concentrent sur différents aspects. Le diagramme de séquence met l'accent sur l'ordre dans lequel les messages sont échangés dans le temps, alors que le diagramme de collaboration met l'accent sur les relations entre les objets, à travers lesquelles les messages sont échangés. Les diagrammes de séquence et de collaboration sont utilisés pour décrire le comportement d'éléments de modèle, tels que les cas d'utilisation, les classes et les opérations. Un diagramme de séquence a deux dimensions. La dimension horizontale montre les participants dans l'interaction, alors que la dimension verticale représente le temps et montre les messages qui sont échangés à travers le temps. Les participants sont représentés dans la partie supérieure du diagramme. Chaque participant possède une ligne de vie qui s'étend vers le bas et qui illustre sa durée de vie. Les participants s'envoient des messages entre eux. Un message connecte deux moments dans le temps (c.-à-d. deux événements), l'un se produisant sur la ligne de vie du participant émetteur du message, et l'autre se produisant sur la ligne de vie du participant récepteur du message. Généralement, un diagramme de séquence représente un seul scénario. Toutefois, il peut aussi être utilisé d'une façon plus abstraite pour exprimer tous les scénarios possibles.

### Intrants

Non disponible.

### Extrants

Non disponible.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
