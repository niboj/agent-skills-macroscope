# Référence du livrable P-OO DA.1 Définir l'architecture de sous-systèmes, niveau réalisateur

## Source analysée

- Fichier source : `../../../macroscope/livrables/40e2b275d287.md`
- Méthode source : Macroscope
- Extraction du titre : lien inverse par URL

## Synthèse du livrable

Cette activité de technique permet d'établir la structure de l'architecture de niveau réalisateur en définissant des sous-ensembles du système d'information appelés sous-systèmes réalisateur. Les sous-systèmes sont regroupés en couches et en sections, ce qui permet une plus grande indépendance des sous-systèmes via une interface spécifique. Chaque couche ou section implante des sous-systèmes bien définis qui suivent des règles uniformes pour l'attribution des noms. L'ensemble des sous-systèmes réalisateur et de leurs dépendances est documenté dans la section Description de l'architecture logicielle du P219S Architecture logicielle (P209C). Les couches, les sections et les sous-systèmes sont définis en tenant compte des règles établies par dans le P380S Règles réalisateur (P380C). La définition des couches et des sections est en fait directement reliée au type de plate-forme technologique choisie, aux besoins de répartition, aux normes de conception internes, etc.

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

- Cette activité de technique permet d'établir la structure de l'architecture de niveau réalisateur en définissant des sous-ensembles du système d'information appelés sous-systèmes réalisateur.
- Les sous-systèmes sont regroupés en couches et en sections, ce qui permet une plus grande indépendance des sous-systèmes via une interface spécifique.
- Chaque couche ou section implante des sous-systèmes bien définis qui suivent des règles uniformes pour l'attribution des noms.
- L'ensemble des sous-systèmes réalisateur et de leurs dépendances est documenté dans la section Description de l'architecture logicielle du P219S Architecture logicielle (P209C).
- Les couches, les sections et les sous-systèmes sont définis en tenant compte des règles établies par dans le P380S Règles réalisateur (P380C).
- * Un Diagramme de paquetage UML ou un Diagramme de composant UML peut être utilisé pour représenter l'architecture logicielle.
- La notion UML de sous-système (sorte de paquetage ayant un comportement associé - voir le Diagramme de paquetage UML) peut servir à représenter les sous-systèmes dans le P219S Architecture logicielle (P209C).
- * Un sous-système peut être décrit à l'aide d'un Diagramme de classe UML, d'un Diagramme de composant UML, d'un Diagramme d'activité UML, d'un Diagramme d'état UML, etc.
- * Les sous-systèmes peuvent être imbriqués dans d'autres sous-systèmes.
- * 2.1 - Définition du sous-système, niveau réalisateur
- P219C - Sous-système, niveau réalisateur
- - Description du sous-système, niveau réalisateur

## Tableaux, modèles ou diagrammes recommandés

- #### Notations
- * Un Diagramme de paquetage UML ou un Diagramme de composant UML peut être utilisé pour représenter l'architecture logicielle.
- La notion UML de sous-système (sorte de paquetage ayant un comportement associé - voir le Diagramme de paquetage UML) peut servir à représenter les sous-systèmes dans le P219S Architecture logicielle (P209C).
- * Un sous-système peut être décrit à l'aide d'un Diagramme de classe UML, d'un Diagramme de composant UML, d'un Diagramme d'activité UML, d'un Diagramme d'état UML, etc.
- Un Diagramme de paquetage UML est utilisé pour illustrer l'imbrication.

## Livrables et références liés

- P219S Architecture logicielle
- P380S Règles réalisateur
- P219S - Architecture logicielle
- P209C - Architecture logicielle
- P219C - Sous-système, niveau réalisateur

## Correspondances TOGAF

- Préséance : TOGAF prime sur Macroscope.
- Phase ADM principale : Phase C - Architecture applicative (Application Architecture).
- Livrable TOGAF cible : Document de définition d’architecture (Architecture Definition Document).
- Domaine d’architecture principal : architecture applicative.
- Artefacts associés : Composant applicatif logique (Logical Application Component), Interface applicative, Bloc constitutif de solution (Solution Building Block).

## Règles particulières de rédaction

- Présenter P-OO DA.1 Définir l'architecture de sous-systèmes, niveau réalisateur comme un artefact, une vue spécialisée, un gabarit ou une annexe d’architecture de service alignée sur TOGAF.
- Ne jamais faire primer Macroscope sur TOGAF.
- Documenter les hypothèses et les points à confirmer lorsque la source utilisateur est incomplète.
- Relier les éléments du livrable aux exigences, décisions, vues, composants et risques pertinents.
- Utiliser le terme conseiller en architecture pour désigner la contribution d’architecture.

## Exemples utiles ou indications extraites

- * Un Diagramme de paquetage UML ou un Diagramme de composant UML peut être utilisé pour représenter l'architecture logicielle.
- Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique.
- #### Exemples
- #### Exemple de mode d'architecture à quatre couches
- Par exemple, le logiciel de base de l'interface utilisateur s'étend souvent sur les couches présentation et dialogue.
- Dans l'exemple précédent, le système d'exploitation est modélisé comme un sous-système réalisateur, mais on ne gagne rien au fait qu'il soit divisé en couches.
- #### Un exemple de la combinaison de couches
- L'exemple suivant montre une situation client-serveur classique, avec procédures ajoutées.

## Points de vigilance

- Vérifier que le livrable répond au besoin utilisateur plutôt qu’à une reproduction mécanique du gabarit.
- Éviter les doublons avec les autres livrables Macroscope liés.
- Ne pas transformer une annexe détaillée en décision d’architecture principale.
- Signaler les sections non applicables au lieu de les remplir artificiellement.
- Conserver la traçabilité entre sources, exigences, décisions et artefacts TOGAF.

## Extraits de contexte Macroscope

### Description

Cette activité de technique permet d'établir la structure de l'architecture de niveau réalisateur en définissant des sous-ensembles du système d'information appelés sous-systèmes réalisateur. Les sous-systèmes sont regroupés en couches et en sections, ce qui permet une plus grande indépendance des sous-systèmes via une interface spécifique. Chaque couche ou section implante des sous-systèmes bien définis qui suivent des règles uniformes pour l'attribution des noms. L'ensemble des sous-systèmes réalisateur et de leurs dépendances est documenté dans la section Description de l'architecture logicielle du P219S Architecture logicielle (P209C). Les couches, les sections et les sous-systèmes sont définis en tenant compte des règles établies par dans le P380S Règles réalisateur (P380C). La définition des couches et des sections est en fait directement reliée au type de plate-forme technologique choisie, aux besoins de répartition, aux normes de conception internes, etc.

### Intrants

Non disponible.

### Extrants

Les livrables suivants peuvent être utilisés pour documenter les résultats de cette activité de technique. Les sections des livrables qui sont applicables sont montrées sous chaque livrable. Les livrables détaillés qui peuvent être utilisés au lieu des livrables succincts, ou en complément à ceux-ci, sont listés directement sous les livrables succincts concernés.

### Procédure ou indications de production

Non disponible.

### Rôles mentionnés dans la source

Non disponible.
